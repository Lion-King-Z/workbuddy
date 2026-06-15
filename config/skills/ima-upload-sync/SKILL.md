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

| 项 | 值 |
|------|------|
| 聚宝盆 KB_ID | `9P9LfmFJRFwLidUrzKQu0cZZ5QMVxtv61QA9iFoV90g=` |
| 深度研究 文件夹 ID | `folder_7471884144740883` |
| 浑水调研 文件夹 ID | `folder_7471884757106786` |

## 工作流

### Step 1：确定上传路径

根据本地文件路径判断目标 IMA 文件夹：

| 本地前缀 | IMA 目标文件夹 |
|---------|--------------|
| `深度研究/MMDD-MMDD/` | `深度研究/` 下的周文件夹 |
| `浑水调研/MMDD-MMDD/` | `浑水调研/` 下的周文件夹 |
| `深度研究/` 根目录 | `深度研究/` |
| `浑水调研/` 根目录 | `浑水调研/` |

### Step 2：检查文件夹路径并创建

```bash
# 获取文件夹下已有内容
SKILL_DIR="C:/Users/Administrator/.workbuddy/skills/ima-skill"
KB_ID="9P9LfmFJRFwLidUrzKQu0cZZ5QMVxtv61QA9iFoV90g="
FOLDER_ID="folder_7471884144740883"  # 父文件夹ID
IMA_OPENAPI_CLIENTID=$(cat ~/.config/ima/client_id)
IMA_OPENAPI_APIKEY=$(cat ~/.config/ima/api_key)
OPTS=$(printf '{"clientId":"%s","apiKey":"%s"}' "$IMA_OPENAPI_CLIENTID" "$IMA_OPENAPI_APIKEY")

# 查找目标子文件夹是否存在
node "$SKILL_DIR/ima_api.cjs" "openapi/wiki/v1/get_knowledge_list" "{\"knowledge_base_id\":\"$KB_ID\",\"folder_id\":\"$FOLDER_ID\",\"cursor\":\"\",\"limit\":50}" "$OPTS"
```

**从返回的 `knowledge_list` 中查找 `media_type=99` 且 `title` 匹配目标周文件夹名的条目。** 如果找到，记录其 `media_id` 作为目标文件夹 ID。如果未找到，调用 `create_folder` API 创建：

```bash
node "$SKILL_DIR/ima_api.cjs" "openapi/wiki/v1/create_folder" "{\"knowledge_base_id\":\"$KB_ID\",\"folder_id\":\"$FOLDER_ID\",\"name\":\"0615-0621\"}" "$OPTS"
# 返回的 media_id 即为新创建的文件夹 ID
```

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

### Step 4：验证

上传完成后，通过 `get_knowledge_list` 验证文件确实在预期文件夹中：

```bash
node "$SKILL_DIR/ima_api.cjs" "openapi/wiki/v1/get_knowledge_list" "{\"knowledge_base_id\":\"$KB_ID\",\"folder_id\":\"$TARGET_FOLDER_ID\",\"cursor\":\"\",\"limit\":50}" "$OPTS"
```

## 常见错误处理

| 错误 | 处理 |
|------|------|
| `check_repeated_names` 返回 `is_repeated=true` | 询问用户：保留两者（追加时间戳 `_YYYYMMDDHHmmss`）还是取消 |
| COS 上传非 0 退出 | 停止流程，向用户报告错误，不调用 `add_knowledge` |
| `create_folder` 失败 | 检查父文件夹 ID 是否正确，知识库 ID 是否正确 |
| API 返回 `code≠0` | 直接将 `msg` 内容展示给用户 |
