---
name: git-sync
description: |
  Auto-sync self-built WorkBuddy skills and global memory to Git repository.
  Trigger when user says "git同步"/"同步git"/"sync git", or after SkillManage creates/modifies a skill,
  or after updating ~/.workbuddy/MEMORY.md.
  This skill handles identifying self-built vs marketplace skills, syncing config/ to the Git repo,
  and pushing to remote.
agent_created: true
---

# Git Sync Skill

Sync self-built WorkBuddy skills and global memory to the Git repository at `G:\锅师`.

## When to Execute

Execute automatically after:
1. Any SkillManage operation (create/modify a skill)
2. Updating `~/.workbuddy/MEMORY.md`
3. User explicitly says "git同步" / "同步git" / "sync git"

## Repository Structure

```
config/
├── MEMORY.md           # Copy of ~/.workbuddy/MEMORY.md (global)
├── project-memory.md   # Copy of G:\锅师\.workbuddy\memory\MEMORY.md (project rules)
├── PERSONA.md          # Copy of G:\锅师\.workbuddy\PERSONA.md (persona)
└── skills/             # Self-built skills only (no marketplace skill_* dirs)
    └── <skill-name>/

Remote: `https://github.com/Lion-King-Z/workbuddy.git`
Branch: `auto-optimize/20260619-2112`

## Self-Built Skill Identification

Self-built skills are those in `~/.workbuddy/skills/` whose directory names do NOT start with `skill_` (which are marketplace-installed). Project-level skills in `G:\锅师\.workbuddy\skills/` are also self-built.

Exclude the following:
- Directories named `skill_<digits>`
- Files (non-directory items like `.zip`, `.json`, etc.)

## Sync Workflow

### Step 1 — Mirror Self-Built Skills

**⛔ 禁止全局 `rm -rf config/skills/`**（Windows git bash 下非原子操作，残留空壳导致后续 cp 嵌套）。

正确做法：先收集源目录列表，再**逐项删除目标 + 复制**。

#### 1a — 收集 Self-Built Skill 列表

从两个来源扫描，合并去重（用 bash for 循环，禁用 xargs——MCP 注入的环境变量过大会导致 xargs 直接报错）：

```bash
# 源1：用户级 ~/.workbuddy/skills/
# 源2：项目级 G:\锅师\.workbuddy\skills/
# 过滤：排除 skill_ 前缀、排除非目录
# 合并去重
```

#### 1b — 逐项复制（防嵌套）

对每个 skill，**先确保目标不存在**再复制。带 `/` 的源路径要先 strip 尾随 `/`，避免 cp 行为歧义：

```bash
for d in /c/Users/Administrator/.workbuddy/skills/*/ /g/锅师/.workbuddy/skills/*/; do
  name=$(basename "$d")
  [[ "$name" != skill_* ]] || continue      # 跳过 marketplace skill
  [[ -d "$d" ]] || continue                 # 只处理目录
  rm -rf "/g/锅师/config/skills/$name"       # ⛔ 逐项删除，不留空壳
  cp -r "${d%/}" "/g/锅师/config/skills/"    # strip尾随/，创建 config/skills/<name>/
done
```

关键：`cp -r src_name config/skills/`（src 不带尾随 `/`）→ 创建 `config/skills/src_name/`。如果目标已存在则**放入目标内部**造成嵌套——所以前面的 `rm -rf` 是强制性前置。

#### 1c — 嵌套自检

复制完成后验证无嵌套：

```bash
cd "/g/锅师/config/skills"
for d in */; do
  outer=${d%/}
  if [ -d "$outer/$outer" ]; then
    echo "❌ 嵌套残留: $outer → 需修复!"
  fi
done
```

#### 1d — 清理 .git / .gitignore

部分 skill 源含 `.git` 子目录（如 submodule），复制后必须删除，否则会被 Git 主 repo 误判为 submodule（160000 模式）：

```bash
find "/g/锅师/config/skills/" -name ".git" -type d -exec rm -rf {} + 2>/dev/null
find "/g/锅师/config/skills/" -name ".gitignore" -type f -delete 2>/dev/null
```

#### 嵌套成因速查

| 场景 | cp 行为 | 结果 |
|:---|:---|:---|
| `config/skills/tdx` **不存在** | `cp -r src/tdx config/skills/` → 创建 `tdx/` | ✅ 正常 |
| `config/skills/tdx` **已存在**（空壳残留） | `cp -r src/tdx config/skills/` → 放入已存在的 `tdx/` 内部 | ❌ `tdx/tdx/` 嵌套 |

全局 `rm -rf config/skills/` 在 Windows git bash 下非原子——部分子目录（只读文件/长路径）可能残留空壳。

### Step 2 — Mirror Global Memory

Copy `~/.workbuddy/MEMORY.md` → `G:\锅师\config\MEMORY.md`.

### Step 2.5 — Mirror Project Memory & Persona

Copy `G:\锅师\.workbuddy\memory\MEMORY.md` → `G:\锅师\config\project-memory.md`.

Copy `G:\锅师\.workbuddy\PERSONA.md` → `G:\锅师\config\PERSONA.md`.

### Step 2.6 — Mirror Identity Files

Copy `~/.workbuddy/SOUL.md` → `G:\锅师\config\SOUL.md`.

Copy `~/.workbuddy/IDENTITY.md` → `G:\锅师\config\IDENTITY.md`.

### Step 3 — Git Commit & Push

```bash
cd "G:/锅师" && git add config/ && git commit -m "<描述>" && GIT_TERMINAL_PROMPT=0 git push
```

Commit message format: describe what changed, e.g.:
- `chore: sync all self-built skills` (periodic full sync)
- `chore: update 浑水电话会深度分析 Skill` (specific skill change)
- `chore: update global memory (IMA sync rules)` (memory update)

### Step 4 — Push Fallback

If `git push` hangs (HTTPS auth), use GitHub MCP `push_files` tool with `owner: "Lion-King-Z"`, `repo: "workbuddy"`, `branch: "auto-optimize/20260619-2112"`.

## Cross-Device Sync（跨设备同步）

当一台电脑上更新了 skill 并推送到 GitHub 后，另一台电脑需要拉取并覆盖本机 skill。

### 完整流程

```text
公司电脑（F盘）                   GitHub                   家用电脑（G盘）
                    ← push ←
                                        pull →
    config/skills/<name>/SKILL.md
        │
        │ cp 覆盖
        ▼
    ~/.workbuddy/skills/<name>/SKILL.md
```

### 操作步骤（复制到另一台电脑的 WorkBuddy 执行）

```
1. git pull 拉最新代码
   仓库: https://github.com/Lion-King-Z/workbuddy
   分支: auto-optimize/20260619-2112

2. 把仓库里 config/skills/<skill名>/SKILL.md 复制覆盖到
   ~/.workbuddy/skills/<skill名>/SKILL.md
   （更新本机 skill 到最新版）

3. 同步git
```

如果是新 skill（config/skills 里有但 ~/.workbuddy/skills 里没有），则复制整个目录：

```
cp -r config/skills/<新skill> ~/.workbuddy/skills/<新skill>
```

### 注意事项

- `~/.workbuddy/skills/` 在 Windows 上对应 `C:\Users\<用户名>\.workbuddy\skills\`
- 项目级 skill 在 `G:\锅师\.workbuddy\skills\`（或公司电脑对应的项目路径）
- 覆盖后 WorkBuddy 无需重启，下次触发即用新版

## One-Shot Full Sync

When user says "全部同步git", execute all steps. Report count: number of skills synced, files changed.

## Rules

- Never sync business content (浑水调研/, 深度研究/) — excluded by .gitignore
- Never sync marketplace skills (skill_* prefix)
- Never sync .workbuddy/ internal data
- After successful push, confirm URL: https://github.com/Lion-King-Z/workbuddy
