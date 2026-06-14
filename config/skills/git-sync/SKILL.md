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
G:\锅师\
├── .gitignore          # Excludes: 业务内容(浑水调研/ 深度研究/), .workbuddy/, 年报, 聚宝盆索引
├── config/
│   ├── MEMORY.md       # Copy of ~/.workbuddy/MEMORY.md
│   └── skills/         # Self-built skills only (no marketplace skill_* dirs)
│       └── <skill-name>/SKILL.md
├── 浑水调研/           # Ignored by git
├── 深度研究/           # Ignored by git
└── ...
```

Remote: `https://github.com/Lion-King-Z/workbuddy.git` (branch: main)

## Self-Built Skill Identification

Self-built skills are those in `~/.workbuddy/skills/` whose directory names do NOT start with `skill_` (which are marketplace-installed). Project-level skills in `G:\锅师\.workbuddy\skills/` are also self-built.

Exclude the following:
- Directories named `skill_<digits>`
- Files (non-directory items like `.zip`, `.json`, etc.)

## Sync Workflow

### Step 1 — Mirror Self-Built Skills

Clear `G:\锅师\config\skills\`, then copy every self-built skill directory from both sources:

**Source 1** — User-level: `~/.workbuddy/skills/*` (directories only, skip skill_* prefix)
**Source 2** — Project-level: `G:\锅师\.workbuddy\skills/*` (directories only)

For each skill directory, copy the entire subtree to `G:\锅师\config\skills/<name>/`.

### Step 2 — Mirror Global Memory

Copy `~/.workbuddy/MEMORY.md` → `G:\锅师\config\MEMORY.md`.

### Step 3 — Git Commit & Push

```bash
cd "G:/锅师" && git add config/ && git commit -m "<描述>" && GIT_TERMINAL_PROMPT=0 git push origin HEAD:main
```

Commit message format: describe what changed, e.g.:
- `chore: sync all self-built skills` (periodic full sync)
- `chore: update 浑水电话会深度分析 Skill` (specific skill change)
- `chore: update global memory (IMA sync rules)` (memory update)

### Step 4 — Push Fallback

If `git push` hangs (HTTPS auth), use GitHub MCP `push_files` tool with `owner: "Lion-King-Z"`, `repo: "workbuddy"`, `branch: "main"`.

## One-Shot Full Sync

When user says "全部同步git", execute all steps. Report count: number of skills synced, files changed.

## Rules

- Never sync business content (浑水调研/, 深度研究/) — excluded by .gitignore
- Never sync marketplace skills (skill_* prefix)
- Never sync .workbuddy/ internal data
- After successful push, confirm URL: https://github.com/Lion-King-Z/workbuddy
