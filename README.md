# 锅师 WorkBuddy 配置仓库

> 全局记忆 + 自建 Skill 版本控制，跨设备同步。

## 结构

```
├── .gitignore          # 排除业务内容（浑水调研/、深度研究/ 等）
├── config/
│   ├── MEMORY.md       # 全局记忆（IMA同步规则、人设偏好、项目结构等）
│   └── skills/         # 27 个自建 Skill
│       ├── 浑水电话会深度分析/  # 电话会→瓶颈→景气度→信源→IMA沉淀
│       ├── 产业链瓶颈投研skill/ # 供给刚性+不可替代性+价格传导
│       ├── 国策主题投研/       # 昊天意志三层映射法
│       ├── 信源检查/           # A/B/C/D/E 五级信源分级
│       ├── 选金/               # 信息沉淀价值筛选
│       ├── 每日投研推送/       # 降噪→10-20条信号推送
│       ├── 每周研判/           # 一周全局信号变化报告
│       ├── git-sync/           # 自动同步本仓库
│       └── ...
```

## 同步策略

- **纳入版本控制**：全局记忆 + 自建 Skill（非 marketplace skill_* 前缀）
- **排除**：业务投研内容（浑水调研/、深度研究/）、WorkBuddy 内部数据（.workbuddy/）
- **触发**：SkillManage 修改/创建 → 自动 cp + commit + push

## 设备恢复

```bash
git clone https://github.com/Lion-King-Z/workbuddy.git
cp config/MEMORY.md ~/.workbuddy/MEMORY.md
cp -r config/skills/* ~/.workbuddy/skills/
```
