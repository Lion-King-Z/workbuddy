# 投资审判团【WorkBuddy】— 三分析师深度研报生成器

把「窄门 × 景气度 × PE估值」三位分析师组织成一场**投资审判庭**，由首席裁决官汇总三维对抗结论，输出一份**像素级模仿 WorkBuddy 深度研报风格**的投资分析报告：顶部决策横幅 → 核心结论卡 → 三维评级体系 → 三分析师独立章节 → 首席裁决书 → 完整推理链 → 核心风险清单 → 信源附录。

核心洞察：**预期信号 ≠ 现实落地，PE 是连接两者的估值桥梁。** 三位分析师分别代表景气度、供给侧瓶颈、PE估值，互相交叉质证；首席裁决官综合三维结论，给出最终评级、目标价区间、建议仓位、入场/退出条件与风险清单。

---

## 核心承诺

给定一个标的（含代码），**全自动**跑完投资审判团工作流，返回一份自包含 HTML 深度研报 + Markdown 摘要：

`市场叙事 → 景气度分析(L) → 瓶颈分析(B) → PE双轨估值(E) → 三维交叉验证 → 首席裁决 → 仓位纪律 → 风险清单 → 信源附录`

> ⚡ **默认全自动模式**：信息缺失先自动搜索补齐，搜不到才反问用户。全程不中断不审批，审判一气呵成。输出自包含 HTML 文件，自动保存本地 + 同步 IMA。

---

## 审判团成员

### 角色一：景气度分析师 — 陆远舟

**核心问题**：赛道景气吗？标的处于产业生命周期哪一级？预期能否落地为现实？

**使用 Skill**：`景气度skill`（产业阶段分级仓位管理法）

**关注点**：
- 行业景气度：增速、确定性、弹性上限
- 产业成熟度分级：L0 技术验证 → L6 价值陷阱
- 核心逻辑：需求驱动、国产替代、全球周期
- 业务结构拆解：收入占比、利润占比、毛利率
- 自身风险信号：季报异动、亏损业务、募投进度

**输出**：
- 景气度结论：`高景气/中景气/低景气`
- 成熟度分级：`L[X] [阶段名称]`
- 弹性上限：`[X]%`
- 确定性：`高/中/低`

---

### 角色二：瓶颈猎手 — 瓶颈分析师

**核心问题**：这个环节有没有壁垒？能卡住别人吗？供给刚性有多强？

**使用 Skill**：`产业链瓶颈投研skill`（Chokepoint Hunter 六步法）

**关注点**：
- 整体紧缺强度：强紧缺 / 中紧缺 / 弱紧缺
- Top 3 关键卡点：产能瓶颈 / 材料约束 / 客户风险 / 地缘切割
- 催化候选：近期可验证的里程碑事件
- 瓶颈推理链：供需两端如何形成利润挤压或价格传导

**输出**：
- 整体紧缺强度：`[X.X]/5.0`
- 关键卡点表格
- 供需推理链

---

### 角色三：PE估值分析师 — PE分析师

**核心问题**：基准估值（纯基本面）值多少？消息催化增量能加多少？当前价格透支了多少？

**使用 Skill**：`pe-valuation-analyst`（基准 + 消息催化分离）

**关注点**：
- 估值方法：PE法（审慎基准）、PE法（催化情景）、PB法、PS法
- 盈利预测：机构一致预期 vs 审慎调整
- 理论PE推导：可比均值 × 龙头溢价 × 增速调整 × 毛利率调整
- 安全边际：当前价 vs 基准估值 vs 催化估值

**输出**：
- 目标价区间：`[低] ~ [高]`，中枢 `[X]` 元
- 隐含涨跌：基准 `-XX%`，催化 `-XX%`
- 溢价率：`+XXX%`

---

### 角色四：首席裁决官 — 沈断言

**核心问题**：三维结论冲突时，如何给出唯一、果断、可执行的最终决策？

**职责**：
- 汇总三维交叉验证记录
- 进行冲突仲裁：好公司 vs 好价格
- 推导建议仓位
- 列出事前验尸（3-6 个月后亏损最可能原因）
- 绘制完整决策树
- 给出执行建议：持仓者 / 未持仓者 / 重新入场条件
- 输出核心风险清单

**输出**：
- 最终评级：`强烈买入 / 买入 / 持有 / 减仓 / 卖出 / 强烈卖出`
- 目标价区间 + 中枢
- 建议仓位 + 弹性上限
- 置信度：高 / 中 / 低
- 完整推理链（决策树文本）
- 执行建议

---

## 审判工作流 — 四轮诉讼

### Round 1：独立取证（三人并行）

三位分析师独立工作，互不通气，各自输出完整子报告。

- 景气度分析师 → 输出「景气度分析章节」
- 瓶颈猎手 → 输出「供应链瓶颈分析章节」
- PE 分析师 → 输出「PE双轨估值章节」

🔴 **CHECKPOINT — Round 1 出口**：三人必须各自输出完整 HTML 子报告，含关键数据、信源标注、结论方向。未完成不得进入 Round 2。

---

### Round 2：交叉质证（三人对抗）

三个分析师互相挑战对方的盲区。每个分析师必须对其他两方提出至少一个具体质疑，并给出回应。

#### 质证协议

**瓶颈 → 景气度**：如果瓶颈被绕过 / 替代技术突破，订单能落地吗？供给端卡点决定了景气度能否持续。

**瓶颈 → PE**：如果 PE 已经透支了瓶颈红利，即使瓶颈成立，估值也消化不了。

**景气度 → 瓶颈**：如果产业阶段倒退（订单取消 / 客户流失），瓶颈再硬也没用。需求端验证比供给端结构更前瞻。

**景气度 → PE**：如果产业阶段倒退，一致预期 EPS 会下修。预期信号是预期，现实落地能跟预期一致吗？

**PE → 瓶颈**：认知偏差维度说市场未充分定价，但 PEG 已经 >2.0，市场可能已经 price in 瓶颈红利。

**PE → 景气度**：产业阶段判定基于定性信号，但部分催化已兑现为市值增量。产业阶段需要和催化兑现进度交叉验证。

🔴 **CHECKPOINT — Round 2 出口**：六个方向质证必须全部完成，并记录是否导致评分调整。

---

### Round 3：三维交叉验证（首席裁决官汇总）

首席裁决官汇总三维结论，形成交叉验证矩阵：

| 维度 | 结论 | 方向 | 权重 |
|:---|:---|:---:|:---:|
| 景气度（陆远舟） | [高景气(L3) · 弹性上限10% · 确定性中等] | 📈 看多 | 40% |
| 瓶颈（猎手） | [强紧缺(4.0/5.0) · MEMS产能卡死 · 催化2026年9月] | 📈 看多 | 40% |
| 估值（PE分析师） | [基准24.66元 · 催化45.75元 · 溢价523%] | 📉 看空 | 20% |

#### 矩阵落格规则

根据景气度/瓶颈二维 + 估值高低，落入 9 格矩阵：

| 景气+瓶颈 | 估值低 | 估值中 | 估值高 |
|:---|:---|:---|:---|
| **双看多** | 强共振 · 买入 | 中共振 · 持有 | 弱共振 · 减仓 |
| **一多一空** | 观察 · 逢低买 | 观望 | 卖出 |
| **双看空** | 等待 · 不抄底 | 卖出 | 强烈卖出 |

---

### Round 4：最终裁决（首席裁决官）

#### Step 1：一票否决检查

| 否决条件 | 含义 | 触发后处理 |
|:---|:---|:---|
| 景气度=L0/L6 | 产业阶段极早期或衰退期 | 直接 D 级 |
| 瓶颈 < 2.5 | 无供给壁垒 | 直接 D 级 |
| PE 溢价 > 500% 且无短期催化 | 严重透支 | 直接 D 级 |
| 财务造假/审计风险 | 信源风险 | 直接 D 级 |

#### Step 2：仓位推导

| 步骤 | 计算 | 结果 |
|:---|:---|:---:|
| ① PE 基准上限 | PE 报告建议 | [X]% |
| ② 弹性上限 | 景气度硬约束 | [X]% |
| ③ MIN(①, ②) | 估值约束优先 | [X]% |
| ④ 估值折价 | 当前价 > 中枢 → 折扣系数 | ×[X.X] |
| ⑤ 催化系数 | 催化在 N 个月内 → 系数 | ×[X.X] |
| 建议仓位 | ① × ④ × ⑤ | [X]% |

#### Step 3：最终评级

| 综合判断 | 评级 | 仓位建议 |
|:---|:---:|:---|
| 强共振 + 估值合理 | 🟢 **强烈买入** | 按景气度上限 |
| 中共振 + 估值合理 | 🟢 **买入** | 仓位上限 × 80% |
| 弱共振 / 估值偏高 | 🟡 **减仓** | 仓位上限 × 50% |
| 双看空 / 估值高 | 🔴 **卖出** | 仓位上限 × 20% 或 0 |
| 严重透支 / 风险暴露 | 🔴 **强烈卖出** | 0% |

---

## HTML 报告模板（一比一像素级模仿）

报告必须保存为自包含 HTML 文件：

`deliverables/investment-tribunal/<股票代码小写>-深度研报-<YYYY-MM-DD>.html`

例如：`deliverables/investment-tribunal/sh688661-深度研报-2026-06-30.html`

### 强制视觉规范

#### 1. 顶部横幅（深蓝渐变）

```html
<div style="background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%); color: #fff; padding: 24px 28px; border-radius: 0; margin: -24px -24px 24px -24px;">
  <div style="font-size: 24px; font-weight: bold; margin-bottom: 6px;">[股票名称]（[代码]）· 深度研究报告</div>
  <div style="font-size: 13px; color: #aaa; margin-bottom: 12px;">
    [公司全称] | [行业分类] | [报告日期] | 分析师团队：[成员名]
  </div>
  <div style="display: flex; gap: 12px; align-items: center;">
    <span style="background: #e74c3c; color: #fff; padding: 6px 14px; border-radius: 20px; font-size: 14px; font-weight: bold;">卖出</span>
    <span style="background: rgba(255,255,255,0.15); color: #fff; padding: 6px 14px; border-radius: 20px; font-size: 13px;">置信度：低</span>
  </div>
</div>
```

#### 2. 核心结论卡（白色卡片，左侧红色边框）

```html
<div style="background: #fff; border-left: 4px solid #e74c3c; border-radius: 8px; padding: 20px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
  <div style="font-size: 18px; font-weight: bold; color: #1a1a2e; margin-bottom: 16px;">📊 核心结论卡</div>
  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; text-align: center;">
    <div>
      <div style="font-size: 12px; color: #666; margin-bottom: 4px;">综合评级</div>
      <div style="font-size: 24px; font-weight: bold; color: #e74c3c;">卖出</div>
      <div style="font-size: 12px; color: #999; margin-top: 4px;">好公司 ≠ 好价格</div>
    </div>
    <div>
      <div style="font-size: 12px; color: #666; margin-bottom: 4px;">目标价区间</div>
      <div style="font-size: 20px; font-weight: bold; color: #1a1a2e;">24.66 ~ 56.00</div>
      <div style="font-size: 12px; color: #999; margin-top: 4px;">中枢 45.75 元</div>
    </div>
    <div>
      <div style="font-size: 12px; color: #666; margin-bottom: 4px;">建议仓位</div>
      <div style="font-size: 24px; font-weight: bold; color: #e67e22;">4%</div>
      <div style="font-size: 12px; color: #999; margin-top: 4px;">弹性上限 10%</div>
    </div>
    <div>
      <div style="font-size: 12px; color: #666; margin-bottom: 4px;">当前价格</div>
      <div style="font-size: 24px; font-weight: bold; color: #e74c3c;">153.00 元</div>
      <div style="font-size: 12px; color: #999; margin-top: 4px;">溢价 +523%</div>
    </div>
  </div>
  <div style="margin-top: 16px; padding: 12px; background: #f8f9fa; border-radius: 6px; font-size: 14px; color: #333; line-height: 1.6;">
    <strong>核心矛盾：</strong>景气度📈 + 瓶颈📈 vs PE估值📉 → <strong>基本面方向确定，但价格已透支3-5年预期</strong>
  </div>
</div>
```

#### 3. 三维评级体系

```html
<div style="background: #fff; border-radius: 8px; padding: 20px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
  <div style="font-size: 18px; font-weight: bold; color: #1a1a2e; margin-bottom: 16px;">🔍 三维评级体系</div>
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
    <div style="background: #f0fff0; border-radius: 8px; padding: 16px; text-align: center;">
      <div style="font-size: 14px; color: #333; font-weight: bold; margin-bottom: 8px;">景气度维度</div>
      <div style="font-size: 13px; color: #27ae60; margin-bottom: 4px;">高景气赛道</div>
      <div style="font-size: 12px; color: #666; margin-bottom: 8px;">L3 成长放量期</div>
      <span style="background: #27ae60; color: #fff; padding: 4px 10px; border-radius: 12px; font-size: 12px;">📈 看多</span>
    </div>
    <div style="background: #f0fff0; border-radius: 8px; padding: 16px; text-align: center;">
      <div style="font-size: 14px; color: #333; font-weight: bold; margin-bottom: 8px;">供给侧维度</div>
      <div style="font-size: 13px; color: #27ae60; margin-bottom: 4px;">强紧缺 (4.0/5.0)</div>
      <div style="font-size: 12px; color: #666; margin-bottom: 8px;">MEMS探针产能·上游材料·英伟达集中</div>
      <span style="background: #27ae60; color: #fff; padding: 4px 10px; border-radius: 12px; font-size: 12px;">📈 看多</span>
    </div>
    <div style="background: #fff5f5; border-radius: 8px; padding: 16px; text-align: center;">
      <div style="font-size: 14px; color: #333; font-weight: bold; margin-bottom: 8px;">估值维度</div>
      <div style="font-size: 13px; color: #e74c3c; margin-bottom: 4px;">严重高估</div>
      <div style="font-size: 12px; color: #666; margin-bottom: 8px;">基准溢价523%</div>
      <span style="background: #e74c3c; color: #fff; padding: 4px 10px; border-radius: 12px; font-size: 12px;">📉 看空</span>
    </div>
  </div>
  <div style="margin-top: 16px; padding: 12px; background: #f8f9fa; border-radius: 6px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <div style="font-size: 13px; color: #666; margin-bottom: 4px;">矩阵落格</div>
      <div style="font-size: 14px; color: #1a1a2e; font-weight: bold;">弱共振 · 减仓</div>
      <div style="font-size: 12px; color: #999;">"高景气+紧缺卡点" × "估值偏高"</div>
    </div>
    <div style="font-size: 24px; font-weight: bold; color: #e74c3c;">卖出</div>
  </div>
</div>
```

#### 4. 分章节标题样式

```html
<h2 style="font-size: 18px; font-weight: bold; color: #1a1a2e; margin: 24px 0 16px; padding-bottom: 8px; border-bottom: 2px solid #1a1a2e;">
  🏭 景气度分析 — 陆远舟
</h2>
```

#### 5. 表格样式

```html
<table style="width: 100%; border-collapse: collapse; font-size: 13px; margin-bottom: 16px;">
  <thead>
    <tr style="background: #1a1a2e; color: #fff;">
      <th style="padding: 10px; text-align: left; border: 1px solid #333;">项目</th>
      <th style="padding: 10px; text-align: left; border: 1px solid #333;">结果</th>
      <th style="padding: 10px; text-align: left; border: 1px solid #333;">信源</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #fff;">
      <td style="padding: 10px; border: 1px solid #eee;">行业景气度</td>
      <td style="padding: 10px; border: 1px solid #eee;">高景气赛道</td>
      <td style="padding: 10px; border: 1px solid #eee; color: #666;">中国FT探针市场增速>30% (集微网2026-04-24)</td>
    </tr>
  </tbody>
</table>
```

#### 6. 风险框样式

```html
<div style="background: #fff5f5; border-left: 4px solid #e74c3c; padding: 14px 16px; border-radius: 0 8px 8px 0; margin: 16px 0;">
  <div style="font-weight: bold; color: #e74c3c; margin-bottom: 8px;">⚠️ 景气度自身风险信号</div>
  <div style="font-size: 13px; color: #555; line-height: 1.8;">...</div>
</div>
```

#### 7. 首席裁决书样式

```html
<div style="background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%); color: #fff; padding: 24px; border-radius: 8px; margin-bottom: 24px; text-align: center;">
  <div style="font-size: 14px; margin-bottom: 8px;">最终裁决</div>
  <div style="font-size: 36px; font-weight: bold; color: #e74c3c;">卖出</div>
  <div style="font-size: 14px; margin-top: 8px; color: #aaa;">三维严重冲突</div>
</div>
```

#### 8. 完整推理链（决策树）样式

```html
<div style="background: #f8f9fa; border-radius: 8px; padding: 16px; font-family: monospace; font-size: 12px; line-height: 1.6; color: #444; white-space: pre-wrap; margin-bottom: 16px;">
┌─ 输入层
├── 景气度: ...
├── 瓶颈: ...
└── PE: ...
   ↓
┌─ 推理层
├── ① 9格矩阵 ...
├── ② 冲突仲裁 ...
├── ③ 可信度加权 ...
└── ④ 事前验尸 ...
   ↓
└─ 裁决层: ...
</div>
```

#### 9. 风险清单样式

```html
<div style="margin-bottom: 16px;">
  <div style="font-weight: bold; font-size: 14px; color: #1a1a2e; margin-bottom: 6px;">① 风险标题</div>
  <div style="font-size: 13px; color: #e74c3c; margin-bottom: 6px;">概率：中高 | 影响：极大</div>
  <div style="font-size: 13px; color: #555; line-height: 1.6; padding: 10px; background: #f8f9fa; border-radius: 6px;">
    风险描述... 应对：...
  </div>
</div>
```

#### 10. 信源附录样式

```html
<div style="font-size: 18px; font-weight: bold; color: #1a1a2e; margin: 24px 0 16px;">📚 信源附录</div>
<table style="width: 100%; border-collapse: collapse; font-size: 13px;">
  <thead>
    <tr style="background: #1a1a2e; color: #fff;">
      <th style="padding: 10px; text-align: left; border: 1px solid #333;">信源等级</th>
      <th style="padding: 10px; text-align: left; border: 1px solid #333;">内容</th>
      <th style="padding: 10px; text-align: left; border: 1px solid #333;">时间戳</th>
    </tr>
  </thead>
  <tbody>...</tbody>
</table>
<div style="font-size: 12px; color: #666; margin-top: 12px;">
  信源分级体系：T0 法定权威 > T1 权威财经媒体 > T2 主流数据平台 > T3 券商研报 > T4 社交自媒体
</div>
```

---

## 标准报告结构（HTML 必含模块）

1. **顶部横幅**：标题、副标题、评级徽章、置信度
2. **📊 核心结论卡**：四宫格（评级/目标价/仓位/现价）、核心矛盾
3. **🔍 三维评级体系**：三个维度卡片 + 矩阵落格
4. **🏭 景气度分析**：
   - 赛道评级与分级表格
   - 核心逻辑（4-6 条）
   - 业务结构表格
   - 自身风险信号
5. **⛓️ 供应链瓶颈分析**：
   - 整体紧缺强度
   - Top 3 关键卡点表格
   - 催化候选
   - 瓶颈推理链
6. **💰 PE双轨估值**：
   - 估值摘要表格
   - 盈利预测表格
   - 理论PE推导
   - 安全边际评估
7. **⚖️ 首席裁决书**：
   - 最终裁决横幅
   - 三维交叉验证记录
   - 冲突仲裁
   - 仓位推导表格
   - 事前验尸
   - 完整推理链（决策树）
   - 执行建议：持仓者 / 未持仓者 / 重新入场条件
8. **⚠️ 核心风险清单**：5-8 条风险，含概率、影响、应对
9. **📚 信源附录**：表格 + 分级说明 + 免责声明

---

## 数据与计算规则

### 景气度评分规则

| 产业阶段 | 成熟度分级 | 弹性上限 | 确定性 |
|:---|:---|:---:|:---:|
| L0 技术验证期 | 太早 | 5% | 低 |
| L1 客户审厂中 | 导入期 | 10% | 低 |
| L2 qualification完成 | 订单前置期 | 15% | 中 |
| L3 订单远超产能 | 成长放量期 | 20% | 中 |
| L4 扩产完成业绩兑现 | 业绩释放期 | 10% | 高 |
| L5 成熟期龙头 | 稳健增长期 | 5% | 高 |
| L6 价值陷阱 | 退出 | 0% | 高 |

### 瓶颈评分规则

| 强度 | 评分 | 含义 |
|:---|:---:|:---|
| 强紧缺 | 4.0-5.0 | 核心瓶颈，供给刚性极强 |
| 中紧缺 | 2.5-3.9 | 中等瓶颈，供给有约束 |
| 弱紧缺 | 1.0-2.4 | 瓶颈较弱 |
| 无瓶颈 | <1.0 | 顺风层 |

### 估值溢价计算

```
溢价率 = (当前价 - 基准估值) / 基准估值 × 100%
```

### 仓位推导公式

```
建议仓位 = MIN(PE基准上限, 弹性上限) × 估值折价系数 × 催化系数
```

| 当前价相对中枢 | 估值折价系数 |
|:---|:---:|
| 溢价 < 50% | 1.0 |
| 溢价 50%-100% | 0.8 |
| 溢价 100%-300% | 0.7 |
| 溢价 300%-500% | 0.6 |
| 溢价 > 500% | 0.5 |

| 催化时间 | 催化系数 |
|:---|:---:|
| < 3个月 | 1.3 |
| 3-6个月 | 1.2 |
| 6-12个月 | 1.0 |
| > 12个月 | 0.8 |
| 无催化 | 0.6 |

---

## 失败模式与异常处理

| 触发条件 | 一线修复 | 仍失败兜底 |
|---|---|---|
| 三维结论完全一致 | 标注"无有效对抗"，提高反向验证强度 | 降级一档 |
| 某维度数据严重不足 | 标注"数据不足"，该维度降权 | 该维度给最低分 |
| 当前价缺失 | 用实时行情补全 | 报告无法生成 |
| 信源不足 | 降级信源等级，标注来源 | 不输出 T0 以下未验证结论 |
| 用户要求快速模式 | 跳过交叉质证，直接输出简化版 | 标注"快速模式，未交叉质证" |

---

## 禁止行为

| # | 禁止项 | 正确做法 |
|---|--------|----------|
| 1 | 跳过三维交叉质证直接裁决 | 六个方向质证必须完成 |
| 2 | 首席裁决官代写分析师子报告 | 每个分析师独立输出 |
| 3 | 输出纯文本或简陋表格 | 必须生成自包含 HTML |
| 4 | 使用非 WorkBuddy 风格 | 严格一比一模仿模板 |
| 5 | 评分无信源标注 | 每个数据必须带 T0-T4 等级 |
| 6 | 省略核心风险清单 | 至少 5 条风险 |
| 7 | 省略信源附录 | 必须列出所有引用信源 |
| 8 | 省略完整推理链 | 必须输出决策树文本 |
| 9 | 报告不自动保存本地 | 保存后立即同步 IMA |
| 10 | 使用中文路径或特殊字符 | 文件名使用英文+数字，小写股票代码 |

---

## 版本信息

- **版本**：v1.0
- **创建日期**：2026-06-30
- **设计灵感**：原「三分析师辩论」skill + 和林微纳_688661_深度研报_20260630 WorkBuddy 共享报告
- **升级点**：
  - 新增首席裁决官角色，统一输出最终决策
  - 输出格式从 Markdown 升级为自包含 HTML 深度研报
  - 一比一模仿 WorkBuddy 研报风格：顶部横幅、核心结论卡、三维评级、决策树、风险清单、信源附录
  - 新增矩阵落格、仓位推导公式、事前验尸、重新入场条件
- **基础 Skill 依赖**：`产业链瓶颈投研skill` / `景气度skill` / `pe-valuation-analyst`
