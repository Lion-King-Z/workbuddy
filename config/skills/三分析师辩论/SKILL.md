# 三分析师辩论 — 窄门 × 景气度 × PE消化

把三个独立的分析视角组织成一场**对抗式辩论**，从市场叙事出发，走完「窄门筛选 → 景气度验证 → PE消化测试」的三层漏斗，最后输出一个综合裁决。

核心洞察（理解性比喻，非强制执行标准）：**预期信号 ≠ 现实落地，PE是连接两者的估值桥梁。** "期货升水是预期，订单和业绩释放才是现实"只是一个帮助理解的比喻——不同标的的"预期信号"形态不同（周期品看期货升水，成长股看一致预期EPS，主题股看市场情绪，制造业看订单公告），核心逻辑是**任何预期信号都需要被现实落地验证**。三个分析师要"打架"——不是简单串联，而是交叉对抗验证，每个视角都要挑战另外两个视角的盲区。

---

## 核心承诺

给定一个标的（含代码）和它的产业链故事，**全自动**跑完三分析师辩论工作流，返回一个清晰的、信源可溯源的综合裁决：

`市场叙事 → 窄门判定(瓶颈分B) → 景气度验证(景气度分P) → PE消化测试(PE消化分E) → 交叉挑战 → 漏斗裁决 → 综合评级 → 仓位纪律`

> ⚡ **默认全自动模式**：信息缺失先自动搜索补齐，搜不到才反问用户。全程不中断不审批，三轮辩论一气呵成。输出MD格式，自动保存本地+同步IMA。

---

## 三分析师角色定义

### 角色一：瓶颈分析师（Bottleneck Analyst）

**核心问题**：这个环节有没有壁垒？能卡住别人吗？供给刚性有多强？

**使用Skill**：`产业链瓶颈投研skill`（Chokepoint Hunter 六步法 v3.0）

**关注点**：
- 供给端卡点：不可替代性、供应弹性、集中度
- 认知偏差：市场是否已充分定价
- 紧缺信号六维检测：价格/产能/客户/库存/投资/跨市场

**输出**：瓶颈分 B（0-5分）

### 角色二：景气度分析师（Prosperity Analyst）

**核心问题**：标的处于产业生命周期哪一级？预期信号（期货升水/研报预测/市场情绪/订单公告等，视标的类型而定）能否落地为现实？

**使用Skill**：`景气度skill`（产业阶段分级仓位管理法）

**关注点**：
- 产业阶段7级分级（0级技术验证→6级价值陷阱）
- 订单可见度 vs 预期信号（预期信号形态因标的而异：周期品看期货升水，成长股看一致预期EPS，主题股看市场情绪，制造业看订单公告）
- TAM天花板与10倍市值检验
- 黄金区间（0.5级→3.5级）定位

**输出**：景气度分 P（0-5分）

### 角色三：PE估值分析师（PE Valuation Analyst）

**核心问题**：如果涨价落地，量×价-成本=利润增量，这个增量能把当前PE打到多少？当前股价是否已price in？

**使用Skill**：`pe-valuation-analyst`（PE估值落地十步法）

**关注点**：
- PE消化路径：静态→N+1E→N+2E→N+3E
- PEG校验与中枢加权估值
- 催化双轨+概率加权
- 四档风险情景（乐观/中性/谨慎/悲观）

**输出**：PE消化分 E（0-5分）

---

## 辩论工作流 — 三轮对抗式验证

### Round 1：独立分析（各自按自己Skill跑）

三个分析师独立工作，互不通气，各自输出自己的5分制评分和核心结论。

#### 瓶颈分析师独立分析

按 Chokepoint Hunter v3.0 跑：
1. 供应链拓扑拆解 → 单点依赖节点识别
2. 两步漏斗筛选 → 四维度加权评分
3. 紧缺信号六维检测
4. 输出瓶颈分 B（0-5分）

**瓶颈分B映射规则**：

| Chokepoint Hunter加权总分 | 瓶颈分B | 含义 |
|:---:|:---:|:---|
| ≥4.0（红色预警） | 5 | 核心瓶颈，供给刚性极强 |
| 3.5-3.9（橙色观察） | 4 | 中等瓶颈，供给有约束 |
| 3.0-3.4（黄色关注） | 3 | 边缘瓶颈，需观察 |
| 2.5-2.9 | 2 | 瓶颈较弱 |
| <2.5 | 1 | 无瓶颈，顺风层 |

#### 景气度分析师独立分析

按景气度skill 4步法跑：
1. 判定产业阶段（6个问题→0-6级）
2. 估算TAM与天花板
3. 匹配仓位配置
4. 风控校验

**景气度分P映射规则**（反映黄金区间逻辑）：

| 产业阶段 | 景气度分P | 含义 |
|:---:|:---:|:---|
| 0级（技术验证期） | 1 | 太早，无商业验证 |
| 1级（客户审厂中） | 2 | 导入期，不确定性高 |
| 2级（qualification完成） | 3 | 订单前置期 |
| 3级（订单远超产能） | 5 | **黄金区间峰值**，产能爬坡期 |
| 3.5级（过渡期） | 4.5 | 黄金区间尾部 |
| 4级（扩产完成，业绩兑现） | 4 | 业绩释放期，弹性降低 |
| 5级（成熟期龙头） | 3 | 护城河深但弹性低 |
| 6级（价值陷阱） | 1 | 增速见顶，退出 |

#### PE估值分析师独立分析

按PE估值落地十步法跑：
1. 取数与信源分级
2. 决策摘要面板
3. 估值消化路径
4. 催化追踪仪表盘
5. 多档PE评估+PEG校验
6. 中枢加权估值
7. 催化估值双轨+概率加权
8. 风险情景量化

**PE消化分E映射规则**：

| PE消化清晰度 + PEG区间 | PE消化分E | 含义 |
|:---|:---:|:---|
| 极高清晰度 + PEG<0.8 | 5 | 明显低估，增量能大幅打低PE |
| 清晰 + PEG 0.8-1.2 | 4 | 合理估值，增量能消化PE |
| 模糊 + PEG 1.2-2.0 | 2.5 | 偏贵，增量勉强消化 |
| 存疑 + PEG>2.0 | 1 | 高估风险，增量无法消化PE |

🔴 **CHECKPOINT — Round 1出口**：三个分析师必须各自输出5分制评分+一句话核心结论+关键信源标注。未完成独立分析不得进入Round 2。

---

### Round 2：交叉挑战（互相质疑）

三个分析师互相挑战对方的盲区。这是辩论的核心环节——**每个分析师必须提出至少一个对另外两个分析师的挑战**。

#### 挑战协议

**瓶颈分析师 → 景气度分析师**：
> "你的阶段判定基于订单预期和产能规划，但如果瓶颈被绕过/替代技术突破，订单能落地吗？供给端卡点决定了景气度能否持续——不是所有订单都能兑现。"

**瓶颈分析师 → PE估值分析师**：
> "你的认知偏差维度评分说市场没定价，但PE已经反映了这个预期，怎么解释？如果PE已经透支了瓶颈红利，即使瓶颈成立，估值也消化不了。"

**景气度分析师 → 瓶颈分析师**：
> "你的瓶颈评分基于供给端结构，但如果产业阶段倒退（订单取消/客户流失），瓶颈再硬也没用。需求端验证比供给端结构更前瞻。"

**景气度分析师 → PE估值分析师**：
> "你的PE消化路径基于一致预期EPS，但如果产业阶段倒退，EPS会下修。预期信号（期货升水/研报预测/订单公告等）是预期，但现实落地（实际成交价/订单兑现/业绩释放）能跟预期一致吗？你的EPS预期可能高估了。"

**PE估值分析师 → 瓶颈分析师**：
> "你的认知偏差维度说市场未充分定价，但我的PE评估显示PEG已经>2.0，市场已经price in了瓶颈红利。认知偏差维度需要和PE水平交叉验证。"

**PE估值分析师 → 景气度分析师**：
> "你的产业阶段判定基于定性信号，但我的催化追踪仪表盘显示，部分催化已兑现为市值增量。产业阶段需要和催化兑现进度交叉验证。"

#### 挑战记录格式

| 挑战方 | 被挑战方 | 挑战要点 | 被挑战方回应 | 是否影响评分 |
|:---:|:---:|------|------|:---:|
| 瓶颈 | 景气度 | [挑战内容] | [回应] | 是/否 |
| 瓶颈 | PE | [挑战内容] | [回应] | 是/否 |
| 景气度 | 瓶颈 | [挑战内容] | [回应] | 是/否 |
| 景气度 | PE | [挑战内容] | [回应] | 是/否 |
| PE | 瓶颈 | [挑战内容] | [回应] | 是/否 |
| PE | 景气度 | [挑战内容] | [回应] | 是/否 |

🔴 **CHECKPOINT — Round 2出口**：六个方向的挑战必须全部完成。如果挑战导致评分调整，需标注调整前后分数。

---

### Round 3：综合裁决（漏斗+加权）

#### Step 1：一票否决检查

逐条检查否决条件，任一触发直接D级，不进入加权计算：

| 否决条件 | 含义 | 触发后处理 |
|:---|:---|:---|
| B < 2.5 | 窄门不通过，无供给壁垒 | 直接D级，标注"瓶颈不足" |
| P = 0级或6级 | 产业阶段极早期或衰退期 | 直接D级，标注"阶段不合适" |
| E < 1.5 | PE消化存疑且PEG>2.5 | 直接D级，标注"估值透支" |

#### Step 2：漏斗门禁检查

通过一票否决后，进入三层漏斗门禁：

```
Gate 1: 窄门 — B ≥ 3.0 ?
  ├─ 否 → 最终评级降一档，标注"瓶颈不足，仅作观察"
  └─ 是 → 进入Gate 2

Gate 2: 景气度 — P ≥ 2.0 ?
  ├─ 否 → 最终评级降一档，标注"景气度未确认"
  └─ 是 → 进入Gate 3

Gate 3: PE消化 — E ≥ 2.0 ?
  ├─ 否 → 最终评级降一档，标注"估值已透支"
  └─ 是 → 进入加权计算
```

#### Step 3：加权综合评分

**综合分 = B × 35% + P × 35% + E × 30%**

权重设计逻辑：
- 窄门35%：前提条件，没有壁垒免谈（一票否决权）
- 景气度35%：核心验证环节，预期vs现实的桥（老大的核心洞察）
- PE消化30%：最终出口，估值能否落地

#### Step 4：最终评级

| 综合分 | 评级 | 含义 | 仓位建议 |
|:---:|:---:|:---|:---|
| ≥4.0 | 🟢 **A级** | 强买入信号，三维度共振 | 按景气度skill仓位上限 |
| 3.5-3.9 | 🟡 **B级** | 可关注信号，两维度以上支撑 | 仓位上限×70% |
| 3.0-3.4 | 🟠 **C级** | 观察信号，单一维度突出 | 仓位上限×50% |
| <3.0 | 🔴 **D级** | 否决，不推荐 | 0% |

**A级额外要求**：三维度必须全部≥3.5，否则降为B级。

---

## 综合报告输出结构

### 1. 辩论开场（市场叙事+标的）

```html
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;max-width:800px;margin:0 auto;padding:20px;background:#fff;">
  <div style="background:linear-gradient(135deg,#1a1a2e 0%,#0f3460 100%);color:#fff;padding:20px;border-radius:12px;margin-bottom:20px;">
    <div style="font-size:22px;font-weight:bold;">⚖️ [标的名称]（[代码]）三分析师辩论报告</div>
    <div style="font-size:13px;color:#aaa;margin-top:6px;">分析日期：YYYY-MM-DD | 框架：窄门×景气度×PE消化 三轮对抗式验证</div>
    <div style="font-size:13px;color:#aaa;margin-top:4px;">当前股价：[XX]元（[涨跌%]）| PE(TTM)：[XX]x | 总市值：[XX]亿</div>
    <div style="font-size:14px;color:#fff;margin-top:8px;background:rgba(255,255,255,0.1);padding:8px 12px;border-radius:6px;">📌 市场叙事：[一句话叙事]</div>
  </div>
</div>
```

### 2. Round 1 — 三分析师独立评分卡

```html
<div style="font-weight:bold;font-size:18px;margin:24px 0 12px;color:#1a1a2e;">📊 Round 1：独立分析</div>

<!-- 瓶颈分析师卡片 -->
<div style="background:#fff5f5;border:2px solid #e74c3c;border-radius:10px;padding:16px;margin-bottom:16px;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
    <div style="font-weight:bold;font-size:16px;color:#e74c3c;">🔒 瓶颈分析师</div>
    <div style="font-size:28px;font-weight:bold;color:#e74c3c;">B=[X]<span style="font-size:14px;color:#999;">/5</span></div>
  </div>
  <div style="font-size:14px;color:#333;line-height:1.6;">[一句话核心结论]</div>
  <div style="font-size:12px;color:#888;margin-top:8px;">信源：[T1/T2/T3] | Chokepoint Hunter加权总分：[X.X]</div>
</div>

<!-- 景气度分析师卡片 -->
<div style="background:#f0fff0;border:2px solid #27ae60;border-radius:10px;padding:16px;margin-bottom:16px;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
    <div style="font-weight:bold;font-size:16px;color:#27ae60;">📈 景气度分析师</div>
    <div style="font-size:28px;font-weight:bold;color:#27ae60;">P=[X]<span style="font-size:14px;color:#999;">/5</span></div>
  </div>
  <div style="font-size:14px;color:#333;line-height:1.6;">[一句话核心结论]</div>
  <div style="font-size:12px;color:#888;margin-top:8px;">产业阶段：[X级] | TAM：[XX亿]（[X]倍市值）</div>
</div>

<!-- PE估值分析师卡片 -->
<div style="background:#fff8e1;border:2px solid #f39c12;border-radius:10px;padding:16px;margin-bottom:16px;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
    <div style="font-weight:bold;font-size:16px;color:#f39c12;">💰 PE估值分析师</div>
    <div style="font-size:28px;font-weight:bold;color:#f39c12;">E=[X]<span style="font-size:14px;color:#999;">/5</span></div>
  </div>
  <div style="font-size:14px;color:#333;line-height:1.6;">[一句话核心结论]</div>
  <div style="font-size:12px;color:#888;margin-top:8px;">PE消化路径：静态[X]x → N+2E [X]x | PEG：[X.X]</div>
</div>
```

### 3. Round 2 — 交叉挑战记录

```html
<div style="font-weight:bold;font-size:18px;margin:24px 0 12px;color:#1a1a2e;">⚔️ Round 2：交叉挑战</div>

<table style="border-collapse:collapse;width:100%;font-size:13px;">
  <thead>
    <tr style="background:#1a1a2e;color:#fff;">
      <th style="padding:8px;border:1px solid #333;">挑战方</th>
      <th style="padding:8px;border:1px solid #333;">被挑战方</th>
      <th style="padding:8px;border:1px solid #333;">挑战要点</th>
      <th style="padding:8px;border:1px solid #333;">被挑战方回应</th>
      <th style="padding:8px;border:1px solid #333;">评分调整</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:8px;border:1px solid #eee;color:#e74c3c;font-weight:bold;">🔒瓶颈</td>
      <td style="padding:8px;border:1px solid #eee;color:#27ae60;">📈景气度</td>
      <td style="padding:8px;border:1px solid #eee;">[挑战内容]</td>
      <td style="padding:8px;border:1px solid #eee;">[回应]</td>
      <td style="padding:8px;border:1px solid #eee;text-align:center;">[无/调整]</td>
    </tr>
    <!-- 其余5个方向... -->
  </tbody>
</table>
```

### 4. Round 3 — 综合裁决

```html
<div style="font-weight:bold;font-size:18px;margin:24px 0 12px;color:#1a1a2e;">⚖️ Round 3：综合裁决</div>

<!-- 漏斗门禁可视化 -->
<div style="background:#f8f9fa;border-radius:10px;padding:16px;margin-bottom:16px;">
  <div style="font-weight:bold;margin-bottom:12px;">漏斗门禁检查</div>
  <div style="display:flex;gap:8px;align-items:center;">
    <div style="flex:1;background:#e74c3c;color:#fff;padding:10px;border-radius:6px;text-align:center;font-size:13px;">
      Gate 1 窄门<br><strong>B=[X] ≥ 3.0 ✓</strong>
    </div>
    <div style="font-size:20px;color:#999;">→</div>
    <div style="flex:1;background:#27ae60;color:#fff;padding:10px;border-radius:6px;text-align:center;font-size:13px;">
      Gate 2 景气度<br><strong>P=[X] ≥ 2.0 ✓</strong>
    </div>
    <div style="font-size:20px;color:#999;">→</div>
    <div style="flex:1;background:#f39c12;color:#fff;padding:10px;border-radius:6px;text-align:center;font-size:13px;">
      Gate 3 PE消化<br><strong>E=[X] ≥ 2.0 ✓</strong>
    </div>
  </div>
</div>

<!-- 加权评分计算 -->
<div style="background:#1a1a2e;color:#fff;padding:16px;border-radius:10px;margin-bottom:16px;">
  <div style="font-size:14px;margin-bottom:8px;">综合分 = B×35% + P×35% + E×30%</div>
  <div style="font-size:14px;margin-bottom:8px;">= [X]×35% + [X]×35% + [X]×30%</div>
  <div style="font-size:24px;font-weight:bold;color:#f39c12;">= [X.X]</div>
</div>

<!-- 最终评级 -->
<div style="background:linear-gradient(135deg,#27ae60,#2ecc71);color:#fff;padding:20px;border-radius:10px;text-align:center;margin-bottom:16px;">
  <div style="font-size:14px;margin-bottom:6px;">最终评级</div>
  <div style="font-size:36px;font-weight:bold;">🟢 A级</div>
  <div style="font-size:14px;margin-top:6px;">强买入信号，三维度共振</div>
  <div style="font-size:16px;margin-top:12px;font-weight:bold;">建议仓位：[XX]%</div>
</div>
```

### 5. 行动计划

```html
<div style="font-weight:bold;font-size:18px;margin:24px 0 12px;color:#1a1a2e;">📋 行动计划</div>

<!-- 仓位纪律 -->
<table style="border-collapse:collapse;width:100%;font-size:13px;margin-bottom:16px;">
  <thead>
    <tr style="background:#1a1a2e;color:#fff;">
      <th style="padding:8px;border:1px solid #333;">维度</th>
      <th style="padding:8px;border:1px solid #333;">建议</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:8px;border:1px solid #eee;font-weight:bold;">仓位</td><td style="padding:8px;border:1px solid #eee;">[XX]%</td></tr>
    <tr><td style="padding:8px;border:1px solid #eee;font-weight:bold;">建仓节奏</td><td style="padding:8px;border:1px solid #eee;">① 首仓 ② 加仓 ③ 满仓</td></tr>
    <tr><td style="padding:8px;border:1px solid #eee;font-weight:bold;">止损线</td><td style="padding:8px;border:1px solid #eee;">跌破 [XX] 元（-XX%）</td></tr>
  </tbody>
</table>

<!-- 验证时间线 -->
<div style="background:#fffdf0;border-left:4px solid #f39c12;padding:12px 14px;border-radius:0 8px 8px 0;">
  <div style="font-weight:bold;color:#f39c12;margin-bottom:8px;">⏰ 验证时间线</div>
  <pre style="font-size:12px;color:#555;line-height:1.6;white-space:pre-wrap;">YYYY.MM │ 📌 验证项1（瓶颈维度）
        │ 📌 验证项2（景气度维度）
        │  → 若达标：动作
        │  → 若不达标：动作
────────┼─────────────────
YYYY.MM │ 📌 验证项（PE维度）</pre>
</div>

<!-- 监控清单 -->
<div style="margin-top:16px;">
  <div style="font-weight:bold;font-size:14px;color:#3498db;margin-bottom:6px;">高频监控（每周）</div>
  <div style="font-size:13px;color:#555;line-height:1.8;">[指标1] | [指标2] | [指标3]</div>
  <div style="font-weight:bold;font-size:14px;color:#9b59b6;margin:12px 0 6px;">低频监控（每月）</div>
  <div style="font-size:13px;color:#555;line-height:1.8;">[指标1] | [指标2] | [指标3]</div>
</div>
```

### 6. 辩论纪律提醒

```html
<div style="background:#fff5f5;border:1px solid #fcc;border-radius:8px;padding:14px 16px;margin:20px 0;">
  <div style="font-weight:bold;font-size:15px;color:#e74c3c;margin-bottom:8px;">⚠️ 辩论纪律</div>
  <div style="font-size:13px;color:#666;line-height:1.8;">
    预期信号 ≠ 现实落地。三个分析师的辩论不是为了达成一致，而是为了暴露盲区——每个被挑战的点，都是后续需要验证的节点。
  </div>
</div>
```

---

## 与三个基础Skill的衔接

本Skill是**编排层**，不替代三个基础Skill的执行：

| 基础Skill | 角色 | 本Skill调用方式 |
|:---|:---|:---|
| 产业链瓶颈投研skill | 瓶颈分析师 | Round 1调用Chokepoint Hunter v3.0完整跑 |
| 景气度skill | 景气度分析师 | Round 1调用4步法完整跑 |
| pe-valuation-analyst | PE估值分析师 | Round 1调用十步法完整跑 |

**执行顺序**：先并行跑三个基础Skill（Round 1），再进入交叉挑战（Round 2），最后综合裁决（Round 3）。

---

## 失败模式与异常处理

| 触发条件 | 一线修复 | 仍失败兜底 |
|----------|----------|-----------|
| 三个分析师评分差距>3分（如B=5, P=1, E=2） | 标注"维度严重分歧"，强制进入Round 2深度挑战 | 降级为C级，标注"分歧过大" |
| 某个基础Skill无法执行（信源不足） | 该维度标注"数据不足"，评分降一档 | 该维度给最低分，标注"待验证" |
| 一票否决触发但用户坚持要分析 | 输出否决理由+单一维度分析，不做综合评级 | 标注"已触发否决，以下为单一维度参考" |
| 交叉挑战无法形成有效对抗（三方一致） | 标注"无有效对抗"，提高反向验证强度 | 降级一档，标注"缺乏对抗" |
| TAM数据缺失导致景气度无法判定 | 用下游客户资本开支反推，标注"自估算" | P降一档，标注"TAM待验证" |

---

## 禁止行为

| # | 禁止项 | 原因 | 正确做法 |
|---|--------|------|----------|
| 1 | 跳过Round 2交叉挑战直接综合 | 失去对抗验证的价值 | 六个方向挑战必须全部完成 |
| 2 | 三分析师简单串联无对抗 | 不是辩论，是流水线 | 每个分析师必须挑战另外两个 |
| 3 | 综合分计算省略漏斗门禁 | 漏斗是一票否决的保障 | 必须先过Gate1-3再加权 |
| 4 | 评分无信源标注 | 无法追溯 | 每个维度评分必须带T1/T2/T3 |
| 5 | A级评级但维度有<3.5 | A级要求三维度全部≥3.5 | 降为B级 |
| 6 | 仓位建议超过景气度skill上限 | 景气度skill是仓位锚 | 综合仓位≤景气度skill对应阶段上限 |
| 7 | 输出纯文本无HTML格式 | 关键信息不醒目 | 优先MD+表格格式 |
| 8 | 交叉挑战敷衍（"同意对方观点"） | 失去对抗意义 | 每个挑战必须有具体质疑点 |
| 9 | 分阶段暂停等用户确认 | 用户要求全自动 | 三轮一口气跑完，不中断 |
| 10 | 报告不自动同步IMA | 产出必须沉淀 | 保存本地后立即同步IMA聚宝盆 |

---

## 版本信息

- **版本**：v1.0
- **创建日期**：2026-06-17
- **基础Skill依赖**：产业链瓶颈投研skill v3.0 / 景气度skill / pe-valuation-analyst v1.0
- **设计灵感**：Vibe-Trading的Swarm多Agent辩论机制 + 锅师体系三层漏斗逻辑
