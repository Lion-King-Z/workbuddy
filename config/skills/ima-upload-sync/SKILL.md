---
name: ima-upload-sync
description: 上传本地研报/文件到IMA聚宝盆知识库。上传前自动检查文件夹路径是否存在（如"深度研究/0615-0621"），不存在则自动创建。适用于所有需同步本地投研产出到IMA聚宝盆的场景。
agent_created: true
---

# IMA 知识库上传同步 Skill

上传本地文件到 IMA 聚宝盆知识库时使用。自动校验文件夹路径，路径不存在则自动创建。

## 前置条件

- IMA OpenAPI 凭证：`~/.config/ima/client_id` 和 `~/.config/ima/api_key`
- SKILL_DIR=`C:/Users/Administrator/.workbuddy/skills/ima-skill`
- `ima_api.cjs`：`$SKILL_DIR/ima_api.cjs`
- COS 上传脚本：`$SKILL_DIR/knowledge-base/scripts/cos-upload.cjs`

## 核心常量

| 项 | 值 | 状态 |
|------|------|------|
| 聚宝盆 KB_ID | `9P9LfmFJRFwLidUrzKQu0cZZ5QMVxtv61QA9iFoV90g=` | ✅ 有效 |
| 深度研究 文件夹 ID | `folder_7471884144740883` | ✅ 有效（2026-06-15 确认） |
| 浑水调研 文件夹 ID | `folder_7471884757106786` | ✅ 有效（2026-06-15 确认） |
| 0615-0621（深度研究下） | `folder_7472132342687156` | ✅ 当前周 |
| 0615-0621（浑水调研下） | `folder_7472255344848188` | ✅ 当前周 |

### ⛔ 文件夹搜索铁律

**search_knowledge API 返回结构**（不是 `media_list`！）：

```json
{
  "data": {
    "info_list": [  // ← 字段名是 info_list，不是 media_list
      {
        "media_id": "folder_xxx",
        "title": "深度研究",       // ← 字段名是 title，不是 name
        "media_type": 99,          // ← 99 表示文件夹
        "parent_folder_id": "xxx"
      }
    ]
  }
}
```

**查找文件夹的正确代码**：
```python
def find_folder(name):
    resp = api("openapi/wiki/v1/search_knowledge", {
        "knowledge_base_id": KB_ID, "query": name, "limit": 50
    })
    for m in resp["data"]["info_list"]:  # ← info_list!
        if m["media_type"] == 99 and m["title"] == name:  # ← title!
            return m["media_id"]
    return None
```

### ⛔ create_folder 必须传 folder_id

**创建子文件夹时 `folder_id` 参数必须传父文件夹ID**，否则创建到根目录！

```python
# ✅ 正确：创建 深度研究/0615-0621
api("create_folder", {
    "knowledge_base_id": KB_ID,
    "name": "0615-0621",
    "folder_id": "folder_7471884144740883"  # ← 深度研究的ID
})

# ❌ 错误：漏掉 folder_id → 创建到根目录
api("create_folder", {
    "knowledge_base_id": KB_ID,
    "name": "0615-0621"
    # ↑ 缺少 folder_id！
})
```

## 工作流

### Step 0（前置）：确定当前周文件夹

**每次操作前先根据今天日期计算所属周文件夹，禁止使用上周文件夹。**

```python
from datetime import date
today = date.today()  # 获取当天日期
# 周文件夹格式 MMDD-MMDD，从周一起算
# 例：2026-06-15（周一）→ 0615-0621
week_start = today - timedelta(days=today.weekday())
week_end = week_start + timedelta(days=6)
week_folder = f"{week_start:%m%d}-{week_end:%m%d}"
```

检查清单：
1. ✅ 今天日期 → 计算对应周文件夹名
2. ✅ 本地 `深度研究/{周文件夹}/` 和 `浑水调研/{周文件夹}/` 是否存在？不存在则创建
3. ✅ IMA 聚宝盆中是否有同名文件夹？没有则先 `create_folder`

### Step 1：确定上传路径

根据本地文件路径判断目标 IMA 文件夹：

| 本地前缀 | IMA 目标文件夹 |
|---------|--------------|
| `深度研究/MMDD-MMDD/` | `深度研究/` 下的周文件夹 |
| `浑水调研/MMDD-MMDD/` | `浑水调研/` 下的周文件夹 |
| `深度研究/` 根目录 | `深度研究/` |
| `浑水调研/` 根目录 | `浑水调研/` |

### Step 2：检查文件夹路径并创建

**使用 `search_knowledge` API 查找子文件夹，返回字段是 `info_list` + `title`。**

```python
# 查找目标子文件夹
resp = api("search_knowledge", {"knowledge_base_id": KB_ID, "query": "0615-0621", "limit": 50})
target_id = None
for m in resp["data"]["info_list"]:  # ← 字段名
    if m["media_type"] == 99 and m["title"] == "0615-0621" \  # ← 字段名
       and m.get("parent_folder_id") == deep_parent_id:
        target_id = m["media_id"]
        break
```

如果未找到，调用 `create_folder`（**必须传 `folder_id` 参数指定父文件夹**）：
```python
resp = api("create_folder", {
    "knowledge_base_id": KB_ID,
    "name": "0615-0621",
    "folder_id": deep_parent_id  # ← 必须传！
})
target_id = resp["data"]["media_id"]
```

### Step 0.5：上传前预检（⛔ create_media 之前强制执行）

**IMA API 无法删除文件。上传到错误文件夹后不可逆，老大需手动到IMA客户端删除。所以必须在 create_media 之前就锁定正确目标。**

```python
from datetime import date, timedelta
import re

# 1. 从文件名提取日期，计算正确周文件夹
filename = "2026-06-15_电话会_磷化铟光芯片.md"
match = re.match(r"(\d{4}-\d{2}-\d{2})_", filename)
assert match, "❌ 文件名无日期前缀，🛑 禁止上传！"
file_date = date.fromisoformat(match.group(1))
week_start = file_date - timedelta(days=file_date.weekday())
week_end = week_start + timedelta(days=6)
correct_week = f"{week_start:%m%d}-{week_end:%m%d}"

# 2. 确认 target_week_folder_name 就是 correct_week
assert correct_week == target_week_folder_name, \
    f"❌ IMA目标周文件夹错误！文件日期={file_date}，正确周={correct_week}，实际目标={target_week_folder_name}"
# → 🛑 阻断上传，修正 TARGET_FOLDER_ID 后重试

# 3. 确认目标周文件夹在IMA中存在（不存在则创建）
# 在父文件夹下搜索
resp = search_knowledge(kb_id, correct_week, folder_id=parent_folder_id)
if not found:
    resp = create_folder(kb_id, correct_week, folder_id=parent_folder_id)  # ← 必须带 folder_id！
    assert resp["code"] == 0, f"❌ IMA文件夹创建失败: {correct_week}"

# 4. 输出预检结果
print(f"""
🔍 IMA上传预检 — {filename}
├── 文件名日期: {file_date} → 正确周: {correct_week}
├── 目标 folder_id: {TARGET_FOLDER_ID}
├── 周文件夹匹配: ✅
└── IMA文件夹就绪: ✅
预检通过 → 允许执行 create_media。
""")
```

**预检不通过 = 🛑 阻断上传链。先修正 target 变量，绝不用错误 folder_id 调 create_media。**

### Step 3：执行文件上传流程

按照 IMA skill 的标准文件上传流程：

1. **preflight-check.cjs** — 检测文件类型和大小

```bash
PREFLIGHT=$(node "$SKILL_DIR/knowledge-base/scripts/preflight-check.cjs" --file "$FILE_PATH")
# 提取 FILE_NAME, FILE_EXT, FILE_SIZE, MEDIA_TYPE, CONTENT_TYPE
```

2. **check_repeated_names** — 检查目标文件夹中是否已存在同名文件

```bash
node "$SKILL_DIR/ima_api.cjs" "openapi/wiki/v1/check_repeated_names" "{\"params\":[{\"name\":\"$FILE_NAME\",\"media_type\":$MEDIA_TYPE}],\"knowledge_base_id\":\"$KB_ID\",\"folder_id\":\"$TARGET_FOLDER_ID\"}" "$OPTS"
```

3. **create_media** — 创建媒体条目，获取 COS 上传凭证

```bash
CREATE_RESP=$(node "$SKILL_DIR/ima_api.cjs" "openapi/wiki/v1/create_media" "{\"file_name\":\"$FILE_NAME\",\"file_size\":$FILE_SIZE,\"content_type\":\"$CONTENT_TYPE\",\"knowledge_base_id\":\"$KB_ID\",\"file_ext\":\"$FILE_EXT\"}" "$OPTS")
# 从响应提取 media_id 和 cos_credential 各字段
```

4. **cos-upload.cjs** — 上传文件到腾讯云 COS

```bash
node "$SKILL_DIR/knowledge-base/scripts/cos-upload.cjs" \
  --file "$FILE_PATH" \
  --secret-id "$SECRET_ID" \
  --secret-key "$SECRET_KEY" \
  --token "$TOKEN" \
  --bucket "$BUCKET" \
  --region "$REGION" \
  --cos-key "$COS_KEY" \
  --content-type "$CONTENT_TYPE" \
  --start-time "$START_TIME" \
  --expired-time "$EXPIRED_TIME" \
  --timeout 300000
```

5. **add_knowledge** — 添加到知识库，指定文件夹

```bash
node "$SKILL_DIR/ima_api.cjs" "openapi/wiki/v1/add_knowledge" "{\"media_type\":$MEDIA_TYPE,\"media_id\":\"$MEDIA_ID\",\"title\":\"$FILE_NAME\",\"knowledge_base_id\":\"$KB_ID\",\"folder_id\":\"$TARGET_FOLDER_ID\",\"file_info\":{\"cos_key\":\"$COS_KEY\",\"file_size\":$FILE_SIZE,\"file_name\":\"$FILE_NAME\"}}" "$OPTS"
```

## 常见错误处理

| 错误 | 处理 |
|------|------|
| `check_repeated_names` 返回 `is_repeated=true` | 询问用户：保留两者（追加时间戳 `_YYYYMMDDHHmmss`）还是取消 |
| COS 上传非 0 退出 | 停止流程，向用户报告错误，不调用 `add_knowledge` |
| `create_folder` 失败 | 检查父文件夹 ID 是否正确，知识库 ID 是否正确 |
| API 返回 `code≠0` | 直接将 `msg` 内容展示给用户 |
