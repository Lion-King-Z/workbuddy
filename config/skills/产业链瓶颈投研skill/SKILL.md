---
name: 产业链瓶颈投研skill
description: Turn an investment agent into a supply-chain bottleneck hunter. Use this skill for source-backed investment research, live market/theme scans, AI/semi/technology value-chain mapping, prosperity scanning (景气度扫描), supply scarcity ranking, A-share/HK/US stock screening, thesis stress tests, and Serenity-inspired research conversations. Trigger on requests like "用 Serenity 的方式看", "深度调研", "产业链/供应链/卡点/瓶颈", "供应紧缺", "景气度扫描", "供给刚性", "紧缺标的", "A股 AI 半导体哪个最值得研究", "find unknown bottlenecks", "rank candidates", or "challenge this thesis". Outputs plain-language reasoning, ranked research priorities by scarcity (high→low), evidence chains, risks, and next verification steps. Research support only; no trade execution.
license: MIT
compatibility: Agent Skills-compatible clients. Best with web/search, market-data, filing, browser, and optional python3 access. Bundled scripts are local-only.
metadata:
  author: muxu-compatible community build
  version: "3.1.0"
  short-description: Supply-chain bottleneck hunter v3.1 — Chokepoint Hunter 7-chapter methodology with two-step funnel screening + supply rigidity taxonomy + catalyst chain
agent_created: true
---

# Serenity.skill

Turn your investment agent into a supply-chain bottleneck hunter.

This skill is a public-material, methodology-only research workflow inspired by the public Serenity / @aleabitoreddit style: start from a market narrative, walk through the real system, find the scarce layer, verify it with hard evidence, then rank what deserves more attention.

It is an independent public-methodology project. Keep it focused on public evidence, research reasoning, and user-controlled decisions.

## Core promise

Given an investment theme and market, run a source-backed supply-chain research workflow and return a clear, plain-language answer:

`market story -> system change -> required parts -> supply-chain layers -> scarce constraints -> public companies -> evidence -> what the market may be missing -> what could prove the idea wrong`

The answer should feel like a sharp research partner talking through the logic in normal language.

## Default behavior

Deep research is the default.

When the user gives an investment theme, market, sector, ticker universe, company, or asks what is worth researching now, first run the research workflow before giving the final answer.

Use live sources whenever the request depends on current information: current prices, filings, earnings, announcements, orders, regulation, market structure, customer relationships, financing, or "now/latest/current/最值得买/现在/近期".

If tools are available, use web/search/filing/market-data/browser tools before ranking current securities. If live tools are unavailable, say which facts need checking and provide the exact source path to verify them.

For theme scans, rank the supply-chain layers before ranking companies. Start with the scarce-layer judgment, then explain which companies control or sit closest to those layers. Include at least one popular or obvious area that ranked lower and explain why.

For deep theme scans, avoid quick-answer behavior. When tools and runtime allow, build a candidate universe of at least 20 companies and inspect at least 25 sources before final ranking. If the run is shorter or tool-limited, label the answer as an initial pass and state which source checks remain.

## Request router

Classify the request, then work in the matching mode.

- **Theme scan**: The user gives a market and theme, such as A-share AI semiconductors, HK robotics, US AI power equipment, CPO, advanced packaging, glass substrates, HBM, silicon photonics, data-center power, robotics, biotech manufacturing, or defense electronics. Run the full research workflow and return priority candidates.
- **Single-company challenge**: The user asks about one ticker/company. Determine the exact value-chain position, evidence quality, what the market may be missing, and what would make the idea weak.
- **Candidate comparison**: The user gives several companies. Compare them by chain position, evidence strength, scarcity, valuation pressure, timing, and risk.
- **Research partner conversation**: The user wants to think, learn, or discuss. Ask tight questions and push the idea toward evidence, chain position, and failure conditions.
- **Learning mode**: The user asks to learn the method. Ask one focused question per turn and walk from trend to system change to scarce layer to proof.

## Research workflow — Chokepoint Hunter 六步法 v3.1

Run this workflow for theme scans, current opportunities, and candidate rankings. The v3.1 method uses a 7-chapter structure with a two-step funnel, supply rigidity taxonomy, and catalyst chain for bottleneck screening.

### 第一章: Supply-chain topology decomposition (供应链拓扑拆解)

1. **Set the scope**
   - Market: US, Hong Kong, A-share, Taiwan, Japan, Korea, Europe, global, or private-company map.
   - Theme: AI infrastructure, semiconductors, CPO, robotics, power, materials, equipment, healthcare manufacturing, defense, or another user-given topic.
   - Time window: infer from the request when possible. Use 3-12 months for "now" unless the user says otherwise.

2. **Translate the story into a system change**
   - What technical or economic change is driving demand?
   - Which old design becomes strained?
   - Which physical constraint matters most: power, latency, bandwidth, heat, yield, purity, reliability, cycle time, packaging density, regulation, or grid connection?

3. **Map the value chain with ASCII visualization**
   - Start from the terminal product and decompose downward to base materials.
   - downstream demand → system integrators → modules/subsystems → chips/devices → process and packaging → equipment and testing → materials and consumables → physical infrastructure
   - Render an ASCII tree diagram showing the full topology.

4. **Single-point dependency node identification (单点依赖节点识别)**
   - Assign each key node an ID (N1, N2, N3...).
   - For each node, classify system role (核心 core / 辅助 auxiliary / 前瞻性 forward-looking).
   - Document available alternatives and single-point dependency risk (★★★ high / ★★ medium / ★ low).

   🔴 **CHECKPOINT — 第一章出口**：确认以下条件全部满足再进入第二章：
   - [ ] ASCII产业链图已绘制，覆盖终端产品到基础材料
   - [ ] 单点依赖节点已编号（N1-N8+），每个标注系统角色和替代方案
   - [ ] 各节点单点依赖风险已评级（★★★/★★/★）

### 第二章: Bottleneck screening — two-step funnel (瓶颈点筛选)

#### Step 1: Quick screening (快速筛查, 1-5 points)

Score each node on three dimensions to fast-route them into pools:

- **不可替代性 (Irreplaceability)**: 1=no alternatives exist, 5=many alternatives
- **集中度 (Concentration)**: 1=monopoly, 5=fully competitive
- **供应弹性 (Supply elasticity)**: 1=zero expansion possible, 5=easy expansion

**Routing rules**:
- 🔴 **Deep-dive pool (深挖池)**: any dimension ≥ 4 → proceed to Step 2
- 🟡 **Edge pool (边缘池)**: 2 dimensions = 3 → note reason, hold
- ❌ **Excluded**: all dimensions ≤ 2 → drop

Quality check: deep-dive pool should have ≥ 2 nodes (≥ 3 points ✓), edge pool reasons documented ✓.

#### Step 1.5: Supply rigidity taxonomy (供给刚性分类, v3.1新增 — 盲区修正)

**核心理念**：供给刚性不是单一维度。不同类型的刚性→不同的催化剂模式→不同的估值方式。必须先分类，再评分。

三分法（互斥归属，选最匹配的一项）：

| 类型 | 定义 | 典型特征 | 催化剂模式 | 估值判据 |
|:---|:---|:---|:---|:---|
| **产能约束型** | 物理产能是硬约束，扩产周期>18月 | 扩产需要建厂/环评/设备交期长，产能利用率已>85% | 催化剂=新产能投产公告+产能利用率数据 | P/B + 产能价值（吨产能市值） |
| **认证锁定型** | 客户认证是硬壁垒，新进入者需2年+ | 通过下游大客户qualification是唯一入场券，试错成本极高 | 催化剂=新客户认证通过+订单公告 | P/E + 在手订单/营收比 |
| **地缘切割型** | 贸易管制/出口限制造成供给分裂 | 国内无法进口或进口成本飙升，国内替代是唯一选项 | 催化剂=管制升级+国产替代政策落地 | 国产替代空间（进口量×单价） |

**分类判定逻辑**（依次问三个问题，第一个"是"即为该类型）：
1. 主要瓶颈是否来自物理产能限制（建厂/设备/周期）？ → 是→产能约束型
2. 主要瓶颈是否来自客户认证/qualification壁垒？ → 是→认证锁定型
3. 主要瓶颈是否来自贸易管制/出口限制/地缘政治？ → 是→地缘切割型

**与四维度评分的关系**：
- 产能约束型 → 不可替代性维度权重提升（30%→35%），供应弹性权重下降（30%→25%）
- 认证锁定型 → 集中度维度权重提升（20%→25%），认知偏差权重下降（20%→15%）
- 地缘切割型 → 认知偏差维度权重提升（20%→25%），集中度权重下降（20%→15%）

🛑 **CHECKPOINT — Step 1.5 出口**：每个深挖池节点必须有供给刚性类型标注+调整后的四维度权重。分类决定催化剂判断路径。

#### Step 2: Deep 4-dimension weighted scoring (深度四维度评分)

For each deep-dive pool node, score on four weighted dimensions.
**⚠️ 权重非固定**：基础权重如下，但需根据 Step 1.5 供给刚性类型做调整（产能约束/认证锁定/地缘切割各调整±5%）：

| Dimension | 基础权重 | 产能约束型 | 认证锁定型 | 地缘切割型 | What it measures |
|-----------|:---:|:---:|:---:|:---:|------------------|
| 不可替代性 (Irreplaceability) | 30% | **35%** | 30% | 30% | Technical壁垒, no substitute available |
| 供应弹性 (Supply elasticity) | 30% | **25%** | 30% | 30% | Expansion cycle, capacity utilization |
| 集中度 (Concentration) | 20% | 20% | **25%** | **15%** | Supplier concentration, customer lock-in |
| 认知偏差 (Cognitive gap) | 20% | 20% | **15%** | **25%** | Market mispricing — is the thesis already priced in? |

**Weighted total = Σ(维度得分 × 调整后权重)**
**使用供给刚性类型对应的权重列，不使用基础权重列。**

**Verdict thresholds**:
- 🔴 **Red alert** (core bottleneck): weighted total ≥ 4.0
- 🟠 **Orange watch** (medium bottleneck): weighted total 3.5-3.9
- 🟡 **Yellow attention** (edge bottleneck): weighted total 3.0-3.4
- ⚪ **White exclude** (no bottleneck): weighted total < 3.0

**Source tier tagging (信源等级)**:
- **T1**: Primary official source (filings, exchange docs, annual reports, tenders, patents)
- **T2**: Authoritative secondary (industry associations, regulators, official statistics)
- **T3**: Analytical sources (broker reports, financial media, industry research)
- **-**: No clear source

**Cognitive gap scoring guide (v3.0 innovation)**:
- 5: Market completely unaware, high purity and about to ramp
- 4: Market has初步 awareness but purity/elasticity underestimated
- 3: Market has some awareness, partial logic priced in
- 2: Market fully aware, main logic priced in (PE reflects it)
- 1: Market over-aware, expectations exhausted (high risk)

   🛑 **STOP — 第二章出口**：若深挖池 < 2 节点，不进入第三章，先回第一章补充节点识别。每个深挖池节点必须完成四维度评分+信源标注。

### 第三章: 6-signal scarcity detection (紧缺信号六维检测)

For each deep-dive pool node, run six-dimension signal detection:

| Signal category | What to detect | Status |
|-----------------|----------------|--------|
| A. Price signal | Price trend, margin change, value uplift | 🟢 detected / ⚪ unverified |
| B. Capacity signal | Utilization rate, expansion plan, ramp timeline | 🟢 detected / ⚪ unverified |
| C. Customer behavior | Large-customer lock-in, certification barriers, order visibility | 🟢 detected / ⚪ unverified |
| D. Inventory signal | Inventory turnover, stocking pressure, channel inventory | 🟢 detected / ⚪ unverified |
| E. Investment signal | Capex, production line investment, R&D spend | 🟢 detected / ⚪ unverified |
| F. Cross-market validation | Overseas benchmarks, value-chain cross-checks, tech roadmap confirmation | 🟢 detected / ⚪ unverified |

**Alert level**:
- 4-6 signals confirmed → 🔴 **Red alert** (scarcity confirmed)
- 3 signals confirmed → 🟠 **Orange watch** (scarcity expectation forming)
- 1-2 signals confirmed → 🟡 **Yellow attention** (scarcity lead)
- 0 signals confirmed → ⚪ **White no signal**

   🔴 **CHECKPOINT — 第三章出口**：每个深挖池节点必须有六维检测结果+预警等级。

### 第四章: Target positioning (标的定位)

#### 4.1 Three-dimension target evaluation

For the final candidate companies, score on three dimensions:

| Dimension | What it measures |
|-----------|------------------|
| 纯度 (Purity) | Core business relevance to the bottleneck theme |
| 弹性 (Elasticity) | Value uplift potential, earnings growth, capacity elasticity |
| 催化剂 (Catalyst) | Near-term catalyst clarity, certainty, time window |

**Composite verdict**:
- 🔴 **Core target**: Purity ≥ 4★ + Elasticity ≥ 4★ + Catalyst ≥ 4★
- 🟠 **Key watch**: Any two dimensions ≥ 4★
- 🟡 **Observation**: Any one dimension ≥ 4★
- ⚪ **Excluded**: All < 4★

#### 4.2 Comparable analysis

Build a peer comparison table with business description, purity, elasticity, catalyst, and valuation (PE TTM).

#### 4.3 Risk annotation

Document: valuation risk, technology substitution risk, purity dilution, customer concentration, trade friction, capacity ramp risk.

   🔴 **CHECKPOINT — 第四章出口**：每个推荐标的必须有纯度/弹性/催化剂三星评分+可比标的+风险标注。

### 第五章: Timing judgment + Catalyst chain (时机判断+催化剂链)

#### 5.1 Signal stage classification

Classify each bottleneck node into a timing stage:

- 🔴 **Scarcity confirmed**: 6 signals ≥ 4 confirmed, earnings already delivered
- 🟠 **Scarcity expectation → confirmation transition**: Small-batch delivery, capacity about to ramp, earnings not yet reflected
- 🟡 **Scarcity fully recognized**: Main logic priced in, PE reflects it
- ⚪ **Scarcity not formed**: Insufficient signals, early stage

Provide operational advice for each stage.

#### 5.2 Catalyst chain (催化剂链, v3.1升级 — 盲区修正)

**核心理念**：没有"买入并持有"，只有**催化剂链**。每个品种的未来应该用一串可验证的催化剂事件来描述——市场是逐层定价的，每验证一层，定价向上一层。

为每个深挖池标的构建三层催化剂链：

```
催化剂链 = 近期(1-2月)可验证触发 → 中期(3-4月)产能/订单验证 → 远期(5-6月)格局兑现
```

| 催化剂层 | 时间窗口 | 典型事件 | 定价含义 | 验证方式 |
|:---|:---|:---|:---|:---|
| 🔴 **近期触发器** | 1-2月 | 客户验证公告/季报预增/涨价函 | 市场首次定价「稀缺」逻辑 | 公司公告+产业新闻 |
| 🟠 **中期验证器** | 3-4月 | 新产能投产/在手订单兑现/财报验证 | 市场定价「业绩兑现」 | 财报+产能数据 |
| 🟡 **远期格局兑现** | 5-6月 | 国产替代政策落地/市占率跃升/行业拐点 | 市场定价「长期价值」 | 政策文件+行业数据 |

**催化剂链构建规则**：
1. 每层至少1个可验证事件，3层合计≥3个事件
2. 每个事件标注：具体日期窗口 + 验证信号（什么算触发/什么算不及预期）+ 重要性（★-★★★★★）
3. 近→中→远必须形成逻辑递进——近期触发不了，中远期的逻辑更不可能被定价
4. 每个催化剂标注触发后的**定价升级路径**——验证后目标价应上移多少

**催化剂链与供给刚性类型的关系**：

| 供给刚性类型 | 近期催化剂特征 | 中期催化剂特征 | 远期催化剂特征 |
|:---|:---|:---|:---|
| 产能约束型 | 产能利用率数据/涨价函 | 新产线投产公告/产能爬坡数据 | 市占率提升/供需缺口收窄 |
| 认证锁定型 | 新客户qualification通过 | 订单公告/在手订单增长 | 客户渗透率/替代进口比例 |
| 地缘切割型 | 出口管制升级/政策信号 | 国产替代招标/进口替代数据 | 国产化率提升/出口能力建立 |

**催化剂链输出格式**：
```markdown
## [标的名称] 催化剂链

| 层级 | 时间窗口 | 事件 | 重要性 | 触发条件 | 不及预期信号 | 定价升级路径 |
|:---|:---|:---|:---:|:---|:---|:---|
| 🔴近期 | 2026/07 | XX客户验证公告 | ★★★★ | 公告确认通过qualification | 公告延期或失败 | 目标价+15% |
| 🟠中期 | 2026/08-09 | 新产线投产 | ★★★★★ | 产能爬坡到50%+ | 投产延期 | 目标价+25% |
| 🟡远期 | 2026/10-12 | 国产替代政策落地 | ★★★ | 政策文件发布 | 政策力度不及预期 | 目标价+20% |
```

**催化剂链的生命周期管理**：
- 近期催化剂兑现 → 中期催化剂变成新的近期 → 重新评估定价是否已反映
- 近期催化剂连续2次不及预期 → 降级观察，下调目标价
- 所有催化剂已兑现→无新催化剂在链上 → 退出信号（利好出尽）

🛑 **CHECKPOINT — 第五章出口**：每个深挖池标的必须有完整的催化剂链（3层×≥1个事件）+ 定价升级路径。催化剂链为空→不得进入第四章推荐。

### 第六章: Reverse verification (反向验证)

Stress-test the thesis:

1. **Substitute technology roadmap probability**: For each alternative, assess status, impact, and probability (high/medium/low) with time window.
2. **Overseas giant capacity over-release**: Analyze whether overseas leaders expanding helps or hurts.
3. **Downstream demand shortfall scenarios**: Probability and impact table.
4. **Blind-spot self-check**:
   - Are edge-pool nodes underestimated?
   - Are there "off-mainstream-narrative but strong卡位" links missed?
   - Is there confirmation bias in search keywords?

### 第七章: Monitoring checklist (监控清单)

#### 7.1 High-frequency indicators (weekly)

Stock price/volume, sector heat, overseas benchmark stock, industry news — with monitoring method and alert signals.

#### 7.2 Low-frequency indicators (monthly)

Earnings pre-announcements, capacity ramp progress, downstream shipment guidance, analyst coverage changes, competitive landscape shifts.

   🛑 **STOP — 第七章出口**：每个推荐标的必须有高频+低频监控清单。这是v3.0的强制新增章节。

## Prosperity scan integration (景气度扫描集成)

The v2.0 prosperity scan (景气度×供给刚性) is now integrated into Step 1 quick screening as part of the three-dimension scoring. The v3.0 four-dimension deep scoring supersedes the v2.0 star-multiply method for deep-dive nodes.

For theme scans that need a quick layer-level scarcity ranking before company analysis, the v2.0 star table is still valid as a fast-preview tool:

| 排名 | 环节 | 景气度 | 供给刚性 | 紧缺分 | 最稀缺标的 | 定量数据 |
|:----:|------|:------:|:--------:|:------:|------------|----------|
|  1   | ...  |  ★★★★  |  ★★★★★   |  20/25 | ...        | ...      |

But for any node that enters the deep-dive pool, the v3.0 four-dimension weighted scoring is authoritative.

## Company universe and evidence (integrated into 第四章)

The v2.0 steps 5-6 (build company universe, gather evidence) are now integrated into 第四章 Target positioning:

- **Company universe**: Build from deep-dive pool nodes. For broad theme scans, aim for at least 20 candidates before filtering to final 3-7. Classify each: controls the scarce layer, supplies it, benefits from the trend, weak control, or mainly a story.
- **Evidence grading**: Integrated into 第二章 Step 2 source-tier tagging (T1/T2/T3) and 第三章 6-signal detection. Every top-3 candidate must have at least 1 T1 source (filing/exchange/annual report). Pure T3-only candidates are downgraded to "待验证".
- **Scoring script**: Use `scripts/serenity_scorecard.py` for repeatable scoring when Python is available.

## Evidence standards

For every top candidate in a current stock ranking, aim for:

- a plain-language answer to "what exactly does this company constrain?";
- at least two concrete evidence points;
- at least one strong source when possible: filing, exchange document, company IR, transcript, regulator/project document, patent/standard, or official order/contract;
- a clear note on evidence strength: strong, medium, weak, or unverified lead;
- the main reason the judgment could be wrong.

For current market claims, never rely only on memory.

Read `references/evidence-ladder.md` for source grading. Read `references/market-source-playbook.md` for US/HK/A-share/Taiwan/Japan/Korea/Europe source paths.

## Communication style

Sound like a direct investment research partner:

- lead with the judgment;
- start theme scans with the scarce layers worth prioritizing;
- explain the reasoning chain in normal language;
- use tables only when they improve comparison;
- be skeptical of hype and crowded stories;
- give strong views when the evidence supports them;
- say exactly which proof is missing when the evidence is weak;
- respond in the user's language;
- use Chinese for Chinese market prompts unless the user asks otherwise.

Avoid report-like stiffness. Avoid jargon in final answers unless the user uses it first.

Use plain phrases:

- "产业链卡点" or "scarce layer" instead of "chokepoint" when writing Chinese.
- "市场可能没看清的地方" instead of "mispricing".
- "接下来可能让市场重新定价的事情" instead of "catalyst".
- "什么情况说明这个判断错了" for failure conditions.
- "优先研究名单" instead of "watchlist".
- "反方理由" or "最大风险" instead of "bear case".

When users ask "which is worth buying", give a ranked research priority and explain the decision chain. Keep trading decisions with the user.

For theme scans, the first answer block should usually look like:

`Start with the layers: [layer 1], [layer 2], [layer 3]. The best research path is to find who controls the hard-to-scale parts.`

Chinese:

`先排产业链层级，再排公司。我会优先看这几层：[层级 1]、[层级 2]、[层级 3]。原因是这些地方更接近真实扩产约束。`

For A-share AI semiconductor scans, a strong opening can be:

`先看带宽和工艺约束，再看纯算力芯片。AI 需求继续扩张时，先紧起来的往往是内存互连、CMP/减薄、刻蚀和耗材这些决定供给能不能爬坡的环节。`

The company ranking should usually include a field or sentence for:

`what it constrains / where it sits / why it ranks here / evidence / main risk`

Chinese:

`卡住的环节 / 产业链位置 / 排序原因 / 证据 / 主要风险`

Keep value-chain layers granular. Split mixed buckets such as "AI chips / CPU / GPU / IP / EDA" into smaller groups when the economics differ: compute chips, EDA/IP, memory/storage, equipment, materials, testing, packaging, optical links, PCB/CCL, power and cooling.

## Research partner protocol

In conversation mode, push the user from story to evidence.

Useful questions:

- What exactly changed in the system?
- Which layer becomes harder to scale?
- Why would customers struggle to route around this company?
- What public evidence proves customer urgency?
- Is this company controlling a scarce layer, supplying one, or only benefiting from the theme?
- What does the market currently seem to price it as?
- What one fact would make you downgrade the idea?

Keep each turn focused. Ask one main question when the user wants guidance.

Read `references/serenity-dialogue-protocol.md` when the user wants ongoing discussion or method training.

## Cross-market adaptation

The economic logic transfers across markets. The source toolkit changes.

- **A-shares**: 年报、半年报、季报、临时公告、交易所问询函、互动易/上证 e 互动、招投标、环评/能评、地方项目备案、专利、客户认证、海关数据、应收/存货/现金流、关联交易。
- **Hong Kong**: HKEX filings, annual/interim reports, placings, connected transactions, mainland policy exposure, liquidity, Southbound eligibility.
- **US**: SEC filings, earnings transcripts, investor presentations, S-3/ATM risk, insider transactions, customer concentration, estimate gaps.
- **Taiwan/Japan/Korea/Europe**: local exchange filings, monthly revenue or operating data where available, company IR, trade journals, export statistics, customer cross-checks, FX/geopolitical exposure.

Read `references/market-source-playbook.md` when market-specific evidence matters.

## Risk boundary

Give research support, ranking, and reasoning. Keep final responsibility with the user.

Avoid:

- guaranteed return language;
- direct buy/sell commands;
- hype around illiquid names;
- rumor-based recommendations;
- material non-public information;
- invented prices, filings, customers, contracts, or market caps.

Use concise language when needed:

`I will rank this by research priority. The trading decision is yours.`

Read `references/risk-and-compliance.md` for high-risk situations.

## 异常与边界条件

| 触发条件 | 一线修复 | 仍失败兜底 |
|----------|----------|-----------|
| WebSearch 未返回定量数据 | 切换搜索词 + 指定数据源（统计局/行业协会/公司公告） | 该环节标注「数据待验证」，降级到附录 |
| 候选公司 < 20 家（A股/港股深度扫描） | 放宽到上下游相邻环节继续搜 | 标注为「初筛结果，覆盖率不足」 |
| 信源冲突（两个 A 级信源矛盾） | 暂停输出，标注矛盾并等待用户确认 | — |
| `serenity_scorecard.py` 不可用 | 手工按步骤4b格式输出评分表 | — |
| 用户给的行业在 A 股无直接标的 | 扩到港股/美股相关标的，或向上游通用技术层找 | 告知用户「该行业在 A 股无纯正标的，已扩至跨市场」 |
| 产业链层的供给约束信息陈旧（>6个月） | WebSearch 搜索最新产能公告/投产新闻 | 标注「信息基于 X 月前数据，建议验证」 |
| 景气度 ★ 和供给刚性 ★ 评分争议（同层不同分析员分歧大） | 记录分歧点和双方证据 | 用区间标注（如「★★★★-★★★★★」） |
| IMA/信源 API 不可达 | 降级为纯 WebSearch + 本地已有研究对照 | 标注「信源受限，结论未经完整交叉验证」 |

## 禁止行为（反例黑名单）

| # | 禁止项 | 原因 | 正确做法 |
|---|--------|------|----------|
| 1 | 未经定量验证打「极度紧缺」评级 | 纯定性判断不可靠 | 第二章 Step 2 强制四维度评分+定量依据 |
| 2 | 跳过稀缺层排序直接列公司 | 用户看不到系统逻辑 | 先排层再排公司 |
| 3 | 仅凭卖方研报标题（T3级）做结论 | 分析师研报需交叉验证 | 升至 T1/T2 级才能引用 |
| 4 | 捏造不存在的价格/产能/交期数据 | 误导投资决策 | 标注来源，未知就写「未获取」 |
| 5 | 对顺风层做昊天层级推荐 | 资源约束和确定性差一个量级 | 分层标注层次差异 |
| 6 | 省略定量数据标注 | 读者无法判断数据可信度 | 每行必须标注数据来源日期 |
| 7 | 同分环节不明确排序理由 | 排名无意义 | 同分必须写「并列原因：XXX」 |
| 8 | 多头排列标的在反方论证中轻描淡写 | 反向压力测试无效 | 反方论据必须与正方等量篇幅 |
| 9 | 跳过两步漏斗直接评分 | 快速筛查→深度评分的漏斗不可省略 | 必须先 Step 1 快速筛查分流，再 Step 2 深度评分 |
| 10 | 缺少认知偏差维度评分 | v3.0核心创新，衡量市场是否已定价 | 四维度必须包含认知偏差（20%权重） |
| 11 | 缺少时机判断章节 | 信号阶段+催化剂日历是v3.0强制章节 | 第五章必须给信号阶段判定+催化剂日历 |
| 12 | 缺少监控清单 | 高频+低频分层监控是v3.0强制章节 | 第七章必须给高频（每周）+低频（每月）监控 |
| 13 | 缺少紧缺信号六维检测 | 独立验证步骤不可省略 | 第三章必须对每个深挖池节点做六维检测 |
| 14 | 输出纯文本报告（无HTML格式） | 关键信息不醒目，阅读体验差 | 必须用HTML可视化格式，颜色编码 |
| 15 | 缺少供给刚性分类 | v3.1核心创新，不同类型决定催化剂路径和估值方式 | Step 1.5必须标注产能约束型/认证锁定型/地缘切割型 |
| 16 | 催化剂日历无分层递进 | 无催化剂链=无"持有并等待"的依据 | 第五章必须输出三层催化剂链(近/中/远)+定价升级路径 |
| 17 | 跳过供给刚性类型对四维度权重的调整 | 基础权重不适用所有类型 | Step 2必须使用Step 1.5分类对应的调整后权重 |

Load only what is needed:

- `references/deep-research-workflow.md` — detailed workflow for source-backed theme scans.
- `references/evidence-ladder.md` — source grading and evidence standards.
- `references/market-source-playbook.md` — source paths by market.
- `references/serenity-dialogue-protocol.md` — research partner and learning-mode behavior.
- `references/output-style-and-language.md` — plain-language output contract.
- `references/public-profile-and-evaluation.md` — public profile, outside evaluation, and reliability notes.
- `references/research-sources.md` — source map used by the project.
- `references/risk-and-compliance.md` — investment research boundaries.
- `assets/thesis-template.md` — reusable thesis memo template.
- `assets/bottleneck-scorecard.json` — JSON input template for the scorecard.
- `assets/research-prompt-pack.md` — prompts for users who want explicit task starters.
- `scripts/serenity_scorecard.py` — local scoring script.
- `scripts/validate_skill.py` — local Agent Skill structure validator.
- `examples/a-share-ai-semiconductor-demo.md` — A-share AI semiconductor example shape.
- `examples/ai-infrastructure-chokepoint-demo.md` — end-to-end example.
- `evals/test-cases.md` — trigger and behavior tests.
