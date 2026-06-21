---
name: 项目结构规范
description: 锅师项目文件夹管理规范 + IMA 自动同步。基于时间容器思维，定义2目录（深度研究+浑水调研）+N文件结构、文件命名规则和放置决策表。当需要创建新文件、移动文件、检查结构是否合规、或用户提到「文件夹」「目录」「结构」「放哪里」「归类」「同步」时触发。
agent_created: true
---

# 项目结构规范

基于「时间容器 > 类型容器」的思维设计。按产出时间归入周文件夹。

## 🖥️ 环境自检（每次启动时先跑）

GitHub 同步 Skill 是跨电脑的，但路径可能不同。每次操作前强制检测：

```python
import os, socket, platform

# 1. 识别电脑
hostname = socket.gethostname()
print(f"🖥️ {hostname} ({platform.node()})")

# 2. 检验项目根目录
ROOT = os.getcwd()  # WorkBuddy 会自动 cd 到工作区
if not os.path.isdir(f"{ROOT}/深度研究"):
    print("❌ 当前不在锅师项目根目录！请确认 workspace 设置")
    exit(1)
print(f"✅ 项目根目录: {ROOT}")

# 3. 检验 IMA 凭证
creds = os.path.expanduser("~/.config/ima")
if os.path.exists(f"{creds}/client_id") and os.path.exists(f"{creds}/api_key"):
    print("✅ IMA凭证就绪")
else:
    print("⚠️ IMA凭证缺失，需配置：https://ima.qq.com/agent-interface")
```

**不要硬编码 `G:\锅师`**，用相对路径或变量。不同电脑路径不同时上述检测会报错提示。

## 文件命名铁律（从上一次出错教训中凝结）

**所有文件名必须使用下划线 `_`，禁止使用点号 `.` 作为字段分隔符。**

| 文件类型 | 命名格式 | 示例 |
|---------|---------|------|
| 产业链深度研究 | `YYYY-MM-DD_题材名产业链深度研究.md` | `2026-06-14_国产AI芯片产业链深度研究.md` |
| 电话会分析 | `YYYY-MM-DD_电话会_关键词.md` | `2026-06-11_电话会_硅片_CCL电子布.md` |
| 每日简报 | `YYYY-MM-DD_每日简报.md` | `2026-06-13_每日简报.md` |
| 每周研判 | `YYYYWWw_每周研判.md` | `2026W24_每周研判.md` |
| 月报 | `YYYY-MM_月报.md` | `2026-06_月报.md` |
| 紧缺总结 | `YYYY-MM-DD_浑水研报紧缺总结.md` | `2026-06-11_浑水研报紧缺总结.md` |
| 紧缺度分析 | `YYYY-MM-DD_供应紧缺度分析.md` | `2026-06-11_供应紧缺度分析.md` |
| 浑水跟踪 | `浑水跟踪_YYYY-MM.md` | `浑水跟踪_2026-06.md` |
| 追踪总表 | `紧缺度追踪总表_YYYYMMDD.md` | `紧缺度追踪总表_20260612.md` |
| 信号时间线 | `紧缺信号时间线_范围.html` | `紧缺信号时间线_5月至6月.html` |
| 个人成长（周） | `YYYYWww_个人成长.md` | `2026W24_个人成长.md` |
| 个人成长（月） | `YYYY-MM_个人成长.md` | `2026-06_个人成长.md` |
| 年报 | `年报_YYYY.md` | `年报_2026.md` |
| 信息源清单 | `信息源清单.md` | — |
| 聚宝盆索引 | `聚宝盆索引.md` | — |

**检查清单（每次新建文件时强制对照）：**
1. ✅ 日期格式：`YYYY-MM-DD`（不是 `YYYY-MM-DD.`、`YYYY.MM.DD`）
2. ✅ 分隔符：只使用 `_`（不是 `.`、`-`、空格）
3. ✅ 文件扩展名：`.md`（小写）
4. ✅ **周文件夹检查**：确认当天日期对应的周文件夹（MMDD-MMDD），禁止放入上周文件夹
5. ✅ **本地文件夹存在性**：检查 `深度研究/MMDD-MMDD/` 和 `浑水调研/MMDD-MMDD/` 是否存在，不存在则创建
6. ✅ **IMA文件夹存在性**：同步前先检查聚宝盆中是否有对应周文件夹，没有则先 `create_folder` 创建
7. ✅ **先改好文件名→再同步到IMA**，顺序不可颠倒

```
G:\锅师\
├── 深度研究/                          ← 产业链研报 + 周期产出
│   ├── MMDD-MMDD/                    ← 周文件夹（周一-周日）
│   │   ├── YYYY-MM-DD_每日简报.md    ← 含宏观读数+判断
│   │   ├── YYYY-MM-DD_主题深研.md
│   │   └── YYYYWww_每周研判.md       ← 周报在对应周文件夹
│   └── YYYY-MM_月报.md               ← 月报在根目录
├── 浑水调研/                          ← 浑水生态（电话会+景气度+紧缺度+跟踪）
│   ├── MMDD-MMDD/                    ← 周文件夹
│   │   ├── 电话会_*.md
│   │   ├── 浑水研报紧缺总结_*.md
│   │   └── 供应紧缺度分析_*.md
│   ├── 浑水跟踪_YYYY-MM.md           ← 月度跟踪（跨周期，根目录）
│   ├── 紧缺度追踪总表_YYYYMMDD.md    ← 跨周期追踪表
│   └── 紧缺信号时间线_*.html         ← 可视化
├── 信息源清单.md
├── 年报_YYYY.md
└── 聚宝盆索引.md

G:\个人成长\                           ← 独立文件夹（不在项目内）
├── YYYYWww_个人成长.md
└── YYYY-MM_个人成长.md
```

## 核心原则

| 原则 | 说明 |
|------|------|
| **深度研究 = 产业链** | 仅放产业链研报+周期产出（日报/周报/月报） |
| **浑水调研 = 浑水生态** | 电话会、景气度扫描、紧缺度分析、月度跟踪——凡浑水相关全进此处 |
| **时间容器** | 日报/周报/深研/电话会按产出日期归入周文件夹 |
| **文件名自解释** | 文件名含日期+主题，脱离目录名独立理解 |
| **跨周期放根目录** | 追踪总表、信号时间线、月度跟踪等跨周期文件放对应目录根 |
| **个人成长在项目外** | `G:\个人成长\` 独立管理，不混入研究项目 |
| **宏观不独立沉淀** | 读数+判断融入每日简报，公开可查数据不存独立文件 |

## 文件放置决策表

| 判断条件 | 目标位置 |
|----------|----------|
| 包含「浑水」「电话会」「紧缺度」「景气度」「供应紧缺」→ | 浑水调研/对应周文件夹 |
| 是产业链/宏观/专题/个股等深度研究 → | 深度研究/对应周文件夹 |
| 是每日简报/每周研判 → | 深度研究/对应周文件夹 |
| 是月报 → | 深度研究/根目录 |
| 是浑水月度跟踪/跨周期追踪表/信号时间线 → | 浑水调研/根目录 |
| 是信息源清单 → | 根目录 |
| 是个人成长 → | G:\个人成长\ |
| 是年度索引 → | 根目录（年报/聚宝盆索引） |

**不确定时：按内容主题判断。产业链→深度研究，浑水相关→浑水调研。**

## IMA 自动同步

本地每产生一个 .md 文件后，**自动上传到 IMA 聚宝盆知识库**，无需用户手动操作。

### 聚宝盆配置

| 项目 | 值 |
|------|-----|
| KB_ID | `9P9LfmFJRFwLidUrzKQu0cZZ5QMVxtv61QA9iFoV90g=` |
| KB 名称 | 聚宝盆 |
| IMA SDK | `~/.workbuddy/skills/ima-skill/ima_api.cjs` |

### 本地 → IMA 目录映射

| 本地位置 | IMA 文件夹 |
|----------|-----------|
| 深度研究/ | 深度研究 |
| 浑水调研/ | 浑水调研 |

## 违规自检

创建或移动文件后，自动检查：
1. 是否创建了深度研究/和浑水调研/之外的目录？→ 违规
2. 是否在两目录内创建了非「MMDD-MMDD」格式的文件夹？→ 违规
3. 浑水相关内容是否误放入深度研究？→ 违规，移回浑水调研
4. 产业链研报是否误放入浑水调研？→ 违规，移回深度研究
5. 文件名是否含日期+主题？→ 如否，补日期前缀
6. 个人成长文件是否出现在锅师项目内？→ 违规，移回 G:\个人成长\

## ⛔ 双端预检（写文件前强制执行，先算对再落子）

**核心铁律：文件名里的日期 = 本地所在周文件夹 = IMA所在周文件夹。三者先对齐，再动笔。**

**⛔ 为什么是预检不是后检：IMA API 无法删除文件。上传到错误文件夹后无法修正，老大需手动到IMA客户端删。所以必须在落盘前就算对目标路径。**

### 预检执行时机

**每次写文件之前**（本地 Write 前 + IMA upload 前），各跑一次。不是落盘后！

### 预检流程

```python
from datetime import date, timedelta
import os, re

# ===== Step 0: 从文件名提取日期，计算正确周文件夹 =====
filename = "2026-06-15_电话会_磷化铟光芯片.md"
match = re.match(r"(\d{4}-\d{2}-\d{2})_", filename)
if not match:
    raise Exception("❌ 文件名无日期前缀！禁止继续，先修正文件名。")
file_date = date.fromisoformat(match.group(1))
week_start = file_date - timedelta(days=file_date.weekday())
week_end = week_start + timedelta(days=6)
correct_week = f"{week_start:%m%d}-{week_end:%m%d}"

# ===== Step 1: 本地预检 — 写文件之前 =====
# 判断文件类型 → 确定目标目录
if "电话会" in filename:
    target_dir = f"浑水调研/{correct_week}/"
elif "每日信息推送" in filename:
    target_dir = f"深度研究/{correct_week}/"
else:
    target_dir = f"深度研究/{correct_week}/"  # 产业链研报默认深度研究

target_path = f"{target_dir}{filename}"

# 逐项打勾
assert correct_week in target_path, f"❌ 本地目标路径错误！应为{correct_week}，实际目标={target_path}"
assert target_dir.startswith(("深度研究/","浑水调研/")), f"❌ 不属于2目录！"
print(f"✅ 本地预检通过 → {target_path}")
# → 确保文件夹存在（不存在则 mkdir）→ 然后 Write

# ===== Step 2: IMA预检 — 上传之前 =====
# 确定 IMA 父文件夹 ID（不是周文件夹ID！）
if target_dir.startswith("深度研究/"):
    ima_parent_id = "folder_7471884144740883"
elif target_dir.startswith("浑水调研/"):
    ima_parent_id = "folder_7471884757106786"

# 在父文件夹下搜索 correct_week 子文件夹
resp = search_knowledge(kb_id, correct_week, folder_id=ima_parent_id)
week_folder_id = None
for item in resp["data"]["info_list"]:
    if item["media_type"] == 99 and item["title"] == correct_week:
        week_folder_id = item["media_id"]
        break

# 不存在则创建（必须带 folder_id 指向父文件夹！）
if not week_folder_id:
    resp = create_folder(kb_id, correct_week, folder_id=ima_parent_id)
    week_folder_id = resp["data"]["media_id"]

assert week_folder_id, f"❌ IMA周文件夹创建失败！{correct_week}"
print(f"✅ IMA预检通过 → 目标 folder_id={week_folder_id} (聚宝盆/{target_dir})")
# → 确认 folder_id 正确后，才执行 create_media → COS upload → add_knowledge

# ===== Step 3: 预检输出 =====
print(f"""
🔍 双端预检 — {filename}
├── 日期: {file_date} → 周文件夹: {correct_week}
├── 本地目标: {target_path} ✅
└── IMA目标: folder_id={week_folder_id} ✅
预检通过，允许落盘。
""")
```

### ⛔ 预检不通过的阻断规则

| 预检项不通过 | 阻断动作 | 修正方式 |
|------------|---------|---------|
| 文件名无日期前缀 | 🛑 禁止继续 | 先改名 |
| 日期计算出错 | 🛑 禁止继续 | 检查 today 日期 |
| 本地目标路径含错误周文件夹 | 🛑 禁止写文件 | 修正 target_dir 变量 |
| IMA周文件夹不存在且创建失败 | 🛑 禁止上传 | 检查 folder_id 和 API 权限 |
| IMA parent_folder_id 用错 | 🛑 禁止上传 | 核对常量表 |

**预检不通过 = 绝不落盘。先修路径，再操作。**

---

## ⛔ 产后收尾清单（每次产出后强制打勾，遗漏即违规）

**任何一项产出（电话会分析/产业链研报/简报/研判）落地后，必须完成以下全部动作才能收工：**

| # | 动作 | 说明 |
|---|------|------|
| 1 | ✅ 文件名合规 | 对照命名铁律检查清单逐条确认 |
| 2 | ✅ 本地文件落盘确认 | 文件在预检通过的目标路径，size > 0 |
| 3 | ✅ IMA同步确认 | add_knowledge 返回 code=0 + media_id 非空 |
| 4 | ✅ 更新浑水跟踪 | 浑水研报产出后，更新 `浑水调研/浑水跟踪_YYYY-MM.md`（信号频次/景气度/新S级） |
| 5 | ✅ 更新聚宝盆索引 | 新增文件记录到 `聚宝盆索引.md` |
| 6 | ✅ Skill变更同步到GitHub | 改了任何Skill → 同步到 config/ → git add/commit/push |
| 7 | ✅ 清理IMA重复笔记 | 同一文件因重命名/重同步产生的旧笔记，确认新笔记OK后删除旧的 |

**违反后果**：少做任何一条，等于没完成。下次老大发现之前自己先查一遍清单。
