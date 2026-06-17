# 示例 — 三分析师辩论输出模板

本文件展示三分析师辩论的完整输出结构（虚拟标的，仅作格式参考）。

---

## 输入

```
标的：[公司名]（[代码]）
市场叙事：[一句话叙事，如"AI算力需求爆发驱动XX环节紧缺"]
```

---

## 完整输出

### 辩论开场

```html
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;max-width:800px;margin:0 auto;padding:20px;background:#fff;">
  <div style="background:linear-gradient(135deg,#1a1a2e 0%,#0f3460 100%);color:#fff;padding:20px;border-radius:12px;margin-bottom:20px;">
    <div style="font-size:22px;font-weight:bold;">⚖️ [公司名]（[代码]）三分析师辩论报告</div>
    <div style="font-size:13px;color:#aaa;margin-top:6px;">分析日期：2026-06-17 | 框架：窄门×景气度×PE消化 三轮对抗式验证</div>
    <div style="font-size:13px;color:#aaa;margin-top:4px;">当前股价：[XX]元（[+X%]）| PE(TTM)：[XX]x | 总市值：[XX]亿</div>
    <div style="font-size:14px;color:#fff;margin-top:8px;background:rgba(255,255,255,0.1);padding:8px 12px;border-radius:6px;">📌 市场叙事：[AI算力需求爆发驱动XX环节紧缺，期货升水XX%]</div>
  </div>
</div>
```

### Round 1：独立分析

```html
<div style="font-weight:bold;font-size:18px;margin:24px 0 12px;color:#1a1a2e;">📊 Round 1：独立分析</div>

<!-- 瓶颈分析师 -->
<div style="background:#fff5f5;border:2px solid #e74c3c;border-radius:10px;padding:16px;margin-bottom:16px;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
    <div style="font-weight:bold;font-size:16px;color:#e74c3c;">🔒 瓶颈分析师</div>
    <div style="font-size:28px;font-weight:bold;color:#e74c3c;">B=4<span style="font-size:14px;color:#999;">/5</span></div>
  </div>
  <div style="font-size:14px;color:#333;line-height:1.6;">[节点NX]为橙色观察级瓶颈，不可替代性5分+供应弹性3分+集中度4分+认知偏差3分，加权3.8分。紧缺信号六维检测4/6检出（价格/产能/客户/投资）。</div>
  <div style="font-size:12px;color:#888;margin-top:8px;">信源：[T1]公司公告 [T2]行业协会 | Chokepoint Hunter加权总分：3.8</div>
</div>

<!-- 景气度分析师 -->
<div style="background:#f0fff0;border:2px solid #27ae60;border-radius:10px;padding:16px;margin-bottom:16px;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
    <div style="font-weight:bold;font-size:16px;color:#27ae60;">📈 景气度分析师</div>
    <div style="font-size:28px;font-weight:bold;color:#27ae60;">P=5<span style="font-size:14px;color:#999;">/5</span></div>
  </div>
  <div style="font-size:14px;color:#333;line-height:1.6;">产业阶段3级（订单远超产能），处于黄金区间峰值。在手订单可见度12个月，期货升水25%但现货成交价已跟涨20%。TAM=180亿（4.5倍市值，<10倍→仓位上限下调一档）。</div>
  <div style="font-size:12px;color:#888;margin-top:8px;">产业阶段：3级 | TAM：180亿（4.5倍市值）</div>
</div>

<!-- PE估值分析师 -->
<div style="background:#fff8e1;border:2px solid #f39c12;border-radius:10px;padding:16px;margin-bottom:16px;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
    <div style="font-weight:bold;font-size:16px;color:#f39c12;">💰 PE估值分析师</div>
    <div style="font-size:28px;font-weight:bold;color:#f39c12;">E=4<span style="font-size:14px;color:#999;">/5</span></div>
  </div>
  <div style="font-size:14px;color:#333;line-height:1.6;">PE消化路径清晰：静态80x → N+1E 45x → N+2E 28x（2年消化65%）。PEG=1.0合理区间。催化双轨：利润增量催化(订单落地)+估值溢价催化(行业龙头定位)，概率加权后综合弹性+35%。</div>
  <div style="font-size:12px;color:#888;margin-top:8px;">PE消化路径：静态80x → N+2E 28x | PEG：1.0</div>
</div>
```

### Round 2：交叉挑战

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
      <td style="padding:8px;border:1px solid #eee;">🔴 供应弹性3分意味着扩产周期18个月，你的3级判定基于订单预期，但产能释放节奏可能滞后</td>
      <td style="padding:8px;border:1px solid #eee;">承认产能风险，但客户长协订单锁定12个月，短期景气度维持</td>
      <td style="padding:8px;border:1px solid #eee;text-align:center;color:#e74c3c;">P: 5→4.75</td>
    </tr>
    <tr>
      <td style="padding:8px;border:1px solid #eee;color:#e74c3c;font-weight:bold;">🔒瓶颈</td>
      <td style="padding:8px;border:1px solid #eee;color:#f39c12;">💰PE</td>
      <td style="padding:8px;border:1px solid #eee;">🟡 认知偏差3分=市场已有认知，但你的PEG=1.0说合理估值，存在矛盾</td>
      <td style="padding:8px;border:1px solid #eee;">认知偏差是定性，PEG是定量，PEG基于N+2E已纳入产能释放预期，不矛盾</td>
      <td style="padding:8px;border:1px solid #eee;text-align:center;">无调整</td>
    </tr>
    <tr>
      <td style="padding:8px;border:1px solid #eee;color:#27ae60;font-weight:bold;">📈景气度</td>
      <td style="padding:8px;border:1px solid #eee;color:#e74c3c;">🔒瓶颈</td>
      <td style="padding:8px;border:1px solid #eee;">🟡 期货升水25%是预期，现货成交价跟涨20%说明已部分落地，但交货时能否维持？</td>
      <td style="padding:8px;border:1px solid #eee;">紧缺信号价格维度已检出，且客户长协+认证壁垒支撑，维持原评分</td>
      <td style="padding:8px;border:1px solid #eee;text-align:center;">无调整</td>
    </tr>
    <tr>
      <td style="padding:8px;border:1px solid #eee;color:#27ae60;font-weight:bold;">📈景气度</td>
      <td style="padding:8px;border:1px solid #eee;color:#f39c12;">💰PE</td>
      <td style="padding:8px;border:1px solid #eee;">🔴 你的N+2E EPS基于一致预期，但TAM仅4.5倍市值(<10倍)，EPS有下修风险</td>
      <td style="padding:8px;border:1px solid #eee;">承认TAM约束，将谨慎情景概率从25%上调至35%，E分微调</td>
      <td style="padding:8px;border:1px solid #eee;text-align:center;color:#e74c3c;">E: 4→3.75</td>
    </tr>
    <tr>
      <td style="padding:8px;border:1px solid #eee;color:#f39c12;font-weight:bold;">💰PE</td>
      <td style="padding:8px;border:1px solid #eee;color:#e74c3c;">🔒瓶颈</td>
      <td style="padding:8px;border:1px solid #eee;">🟡 你的认知偏差3分说市场已有认知，但我的PE消化显示N+2E 28x仍偏贵，市场可能已透支</td>
      <td style="padding:8px;border:1px solid #eee;">认知偏差3分=部分逻辑被定价，非完全透支，与PE偏贵一致</td>
      <td style="padding:8px;border:1px solid #eee;text-align:center;">无调整</td>
    </tr>
    <tr>
      <td style="padding:8px;border:1px solid #eee;color:#f39c12;font-weight:bold;">💰PE</td>
      <td style="padding:8px;border:1px solid #eee;color:#27ae60;">📈景气度</td>
      <td style="padding:8px;border:1px solid #eee;">🟡 催化追踪显示订单落地催化已部分兑现，你的3级阶段判定可能滞后</td>
      <td style="padding:8px;border:1px solid #eee;">催化兑现≠业绩释放，产能尚未投产，维持3级</td>
      <td style="padding:8px;border:1px solid #eee;text-align:center;">无调整</td>
    </tr>
  </tbody>
</table>
```

### Round 3：综合裁决

```html
<div style="font-weight:bold;font-size:18px;margin:24px 0 12px;color:#1a1a2e;">⚖️ Round 3：综合裁决</div>

<!-- 漏斗门禁 -->
<div style="background:#f8f9fa;border-radius:10px;padding:16px;margin-bottom:16px;">
  <div style="font-weight:bold;margin-bottom:12px;">漏斗门禁检查</div>
  <div style="display:flex;gap:8px;align-items:center;">
    <div style="flex:1;background:#e74c3c;color:#fff;padding:10px;border-radius:6px;text-align:center;font-size:13px;">
      Gate 1 窄门<br><strong>B=4 ≥ 3.0 ✓</strong>
    </div>
    <div style="font-size:20px;color:#999;">→</div>
    <div style="flex:1;background:#27ae60;color:#fff;padding:10px;border-radius:6px;text-align:center;font-size:13px;">
      Gate 2 景气度<br><strong>P=4.75 ≥ 2.0 ✓</strong>
    </div>
    <div style="font-size:20px;color:#999;">→</div>
    <div style="flex:1;background:#f39c12;color:#fff;padding:10px;border-radius:6px;text-align:center;font-size:13px;">
      Gate 3 PE消化<br><strong>E=3.75 ≥ 2.0 ✓</strong>
    </div>
  </div>
</div>

<!-- 加权评分 -->
<div style="background:#1a1a2e;color:#fff;padding:16px;border-radius:10px;margin-bottom:16px;">
  <div style="font-size:14px;margin-bottom:8px;">综合分 = B×35% + P×35% + E×30%</div>
  <div style="font-size:14px;margin-bottom:8px;">= 4×35% + 4.75×35% + 3.75×30%</div>
  <div style="font-size:14px;margin-bottom:8px;">= 1.40 + 1.66 + 1.13</div>
  <div style="font-size:24px;font-weight:bold;color:#f39c12;">= 4.19</div>
</div>

<!-- 最终评级 -->
<div style="background:linear-gradient(135deg,#27ae60,#2ecc71);color:#fff;padding:20px;border-radius:10px;text-align:center;margin-bottom:16px;">
  <div style="font-size:14px;margin-bottom:6px;">最终评级</div>
  <div style="font-size:36px;font-weight:bold;">🟢 A级</div>
  <div style="font-size:14px;margin-top:6px;">强买入信号，三维度共振（B=4, P=4.75, E=3.75，全部≥3.5）</div>
  <div style="font-size:16px;margin-top:12px;font-weight:bold;">建议仓位：7%（3级上限10% × TAM下调一档5% × A级100%）</div>
</div>
```

### 行动计划

```html
<div style="font-weight:bold;font-size:18px;margin:24px 0 12px;color:#1a1a2e;">📋 行动计划</div>

<table style="border-collapse:collapse;width:100%;font-size:13px;margin-bottom:16px;">
  <thead>
    <tr style="background:#1a1a2e;color:#fff;">
      <th style="padding:8px;border:1px solid #333;">维度</th>
      <th style="padding:8px;border:1px solid #333;">建议</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:8px;border:1px solid #eee;font-weight:bold;">仓位</td><td style="padding:8px;border:1px solid #eee;">7%（首仓3% + 加仓2% + 满仓2%）</td></tr>
    <tr><td style="padding:8px;border:1px solid #eee;font-weight:bold;">建仓节奏</td><td style="padding:8px;border:1px solid #eee;">① 首仓3%（当前价） ② 加仓2%（N+1财报订单确认） ③ 满仓2%（产能投产公告）</td></tr>
    <tr><td style="padding:8px;border:1px solid #eee;font-weight:bold;">止损线</td><td style="padding:8px;border:1px solid #eee;">跌破 [XX] 元（-15%）减至3%</td></tr>
  </tbody>
</table>

<div style="background:#fffdf0;border-left:4px solid #f39c12;padding:12px 14px;border-radius:0 8px 8px 0;">
  <div style="font-weight:bold;color:#f39c12;margin-bottom:8px;">⏰ 验证时间线</div>
  <pre style="font-size:12px;color:#555;line-height:1.6;white-space:pre-wrap;">2026.08 │ 📌 N+1财报订单确认（景气度维度）
        │  → 若订单增速>50%：加仓2%
        │  → 若订单增速<30%：减至3%
────────┼─────────────────
2026.12 │ 📌 产能投产进度（瓶颈维度）
        │  → 若按期投产：满仓2%
        │  → 若延期：维持5%观察
────────┼─────────────────
2027.03 │ 📌 N+2E EPS上修情况（PE维度）
        │  → 若EPS上修>10%：维持仓位
        │  → 若EPS下修：启动退出流程</pre>
</div>
```

### 辩论纪律提醒

```html
<div style="background:#fff5f5;border:1px solid #fcc;border-radius:8px;padding:14px 16px;margin:20px 0;">
  <div style="font-weight:bold;font-size:15px;color:#e74c3c;margin-bottom:8px;">⚠️ 辩论纪律</div>
  <div style="font-size:13px;color:#666;line-height:1.8;">
    期货升水25%是预期，订单和业绩释放才是现实。三个分析师的辩论不是为了达成一致，而是为了暴露盲区——本轮挑战暴露的关键盲区：TAM不足（4.5倍<10倍）导致EPS有下修风险，已通过谨慎情景概率上调纳入。
  </div>
</div>
```
