import json

stocks = {
    '沪电股份': {
        'code': '002463', 'today': 137.13, 'board': '深市主板', 'lt_mcap': 26367.5,
        'rz_data': [
            {'date':'2026-07-13','buy':4.9797,'repay':5.1156,'balance':61.9261,'close':124.66},
            {'date':'2026-07-10','buy':9.4276,'repay':9.5543,'balance':62.0620,'close':129.44},
            {'date':'2026-07-09','buy':8.2003,'repay':8.3574,'balance':62.1888,'close':137.30},
        ],
        'history': {
            '2026-07-08':(62.3459,128.20),'2026-07-07':(63.8961,129.72),'2026-07-06':(62.8431,128.83),
            '2026-07-03':(64.9289,135.35),'2026-07-01':(68.8827,145.01),'2026-06-30':(70.7810,152.80),
            '2026-06-09':(68.6962,141.09),'2026-05-29':(53.8609,132.04),'2026-04-30':(35.3781,102.57),
        }
    },
    '生益科技': {
        'code': '600183', 'today': 147.90, 'board': '沪市主板', 'lt_mcap': 3541.5,
        'rz_data': [
            {'date':'2026-07-13','buy':6.8303,'repay':8.5908,'balance':37.5130,'close':134.45},
            {'date':'2026-07-10','buy':6.5804,'repay':7.5373,'balance':39.2735,'close':149.39},
            {'date':'2026-07-09','buy':7.4028,'repay':7.0096,'balance':40.2304,'close':157.40},
        ],
        'history': {
            '2026-07-08':(39.8371,145.46),'2026-07-07':(40.1916,150.77),'2026-07-06':(40.5674,154.27),
            '2026-07-03':(41.9650,160.78),'2026-07-01':(43.7101,164.80),'2026-06-30':(45.8897,173.40),
            '2026-06-09':(35.3770,147.47),'2026-05-29':(46.6323,140.62),'2026-04-30':(20.7863,76.51),
        }
    },
    '风华高科': {
        'code': '000636', 'today': 59.41, 'board': '深市主板', 'lt_mcap': 687.4,
        'rz_data': [
            {'date':'2026-07-13','buy':1.1413,'repay':2.8634,'balance':29.3074,'close':54.01},
            {'date':'2026-07-10','buy':5.3956,'repay':6.5479,'balance':31.0294,'close':60.01},
            {'date':'2026-07-09','buy':4.7246,'repay':5.8924,'balance':32.1818,'close':64.55},
        ],
        'history': {
            '2026-07-08':(33.3495,60.70),'2026-07-07':(33.4703,61.26),'2026-07-06':(33.4144,58.50),
            '2026-07-03':(33.8558,63.23),'2026-07-01':(35.6290,74.40),'2026-06-30':(31.9704,72.24),
            '2026-06-09':(30.6216,61.08),'2026-05-26':(13.9565,41.70),'2026-04-30':(12.0480,25.09),
        }
    },
    '江波龙': {
        'code': '301308', 'today': 538.51, 'board': '创业板', 'lt_mcap': 1517.8,
        'rz_data': [
            {'date':'2026-07-13','buy':8.5117,'repay':18.3924,'balance':86.6425,'close':522.04},
            {'date':'2026-07-10','buy':17.3289,'repay':14.6578,'balance':96.5232,'close':587.60},
            {'date':'2026-07-09','buy':14.4721,'repay':13.0276,'balance':93.8520,'close':620.00},
        ],
        'history': {
            '2026-07-08':(92.4075,592.71),'2026-07-07':(94.4572,627.90),'2026-07-06':(90.0151,681.80),
            '2026-07-03':(89.3880,618.02),'2026-07-01':(93.7356,667.84),'2026-06-30':(94.3992,703.80),
            '2026-06-09':(69.5603,514.65),'2026-05-26':(67.0849,538.95),'2026-04-14':(39.8121,381.51),
        }
    },
    '兆易创新': {
        'code': '603986', 'today': 583.99, 'board': '沪市主板', 'lt_mcap': 3903.9,
        'rz_data': [
            {'date':'2026-07-13','buy':45.9775,'repay':47.7521,'balance':218.5050,'close':550.80},
            {'date':'2026-07-10','buy':67.0765,'repay':75.8616,'balance':220.2795,'close':612.00},
            {'date':'2026-07-09','buy':56.0392,'repay':48.2171,'balance':229.0645,'close':663.49},
        ],
        'history': {
            '2026-07-08':(221.2425,603.17),'2026-07-07':(218.9566,620.00),'2026-07-06':(223.2265,654.29),
            '2026-07-03':(221.7004,677.77),'2026-07-01':(236.2751,772.01),'2026-06-30':(236.4058,815.00),
            '2026-06-09':(195.2221,500.50),'2026-05-25':(180.1144,515.60),'2026-04-14':(92.9821,280.01),
        }
    },
}

def compute(name, s):
    d = s['rz_data']
    buys = [x['buy'] for x in d]
    prices = [x['close'] for x in d]
    cw = sum(b*p for b,p in zip(buys,prices)) / sum(buys)
    vals = [(b*p, p, dt) for b,p,dt in [(x['buy'],x['close'],x['date']) for x in d]]
    ch = max(vals)
    
    today = s['today']
    lt_mcap = s['lt_mcap']
    bal = d[0]['balance']
    f_ratio = bal / (lt_mcap * 100) * 100
    
    p130_cw = 0.65 * cw
    p115_cw = 0.575 * cw
    p130_ch = 0.65 * ch[1]
    p115_ch = 0.575 * ch[1]
    
    res130_cw = (today - p130_cw)/today * 100
    res115_cw = (today - p115_cw)/today * 100
    res130_ch = (today - p130_ch)/today * 100
    res115_ch = (today - p115_ch)/today * 100
    
    v_curr = 2 * today / ch[1] * 100
    status = '安全' if v_curr >= 150 else ('警戒' if v_curr >= 130 else ('追保区' if v_curr >= 115 else '强平区'))
    
    h = s['history']
    bal_5d = h.get('2026-07-07', h.get('2026-07-08'))
    bal_10d = h.get('2026-07-01', h.get('2026-07-02'))
    bal_20d = h.get('2026-06-24', h.get('2026-06-23'))
    
    d5 = ((bal - bal_5d[0])/bal_5d[0]*100) if bal_5d else 0
    d10 = ((bal - bal_10d[0])/bal_10d[0]*100) if bal_10d else 0
    d20 = ((bal - bal_20d[0])/bal_20d[0]*100) if bal_20d else 0
    
    repay_ratio = d[0]['repay'] / d[0]['buy'] if d[0]['buy'] > 0 else 0
    
    all_balances = [v[0] for v in h.values()] + [bal]
    max_bal = max(all_balances)
    min_bal = min(all_balances)
    percentile = (bal - min_bal) / (max_bal - min_bal) * 100 if max_bal > min_bal else 50
    
    if bal_10d:
        s10 = (today - bal_10d[1]) / bal_10d[1] * 100
        m10 = d10
        if s10 > 2 and m10 < -5:
            diverge = '背离(涨+融资降)动能衰竭预警'
        elif s10 > 2 and m10 > 2:
            diverge = '一致上行趋势健康'
        elif s10 < -5 and m10 < -10:
            r_ratio = abs(m10)/abs(s10) if abs(s10) > 0 else 99
            if r_ratio > 1.5:
                diverge = '被动去杠杆(R=%.1f)勿接刀' % r_ratio
            else:
                diverge = '主动去杠杆(R=%.1f)偏健康' % r_ratio
        else:
            diverge = '正常'
    else:
        diverge = 'N/A'
    
    if percentile > 90: temp = '偏热'
    elif percentile > 70: temp = '偏热'
    elif percentile > 30: temp = '正常'
    else: temp = '偏冷'
    
    repay_warn = '偿还压力大' if repay_ratio > 1 else '融资净买入'
    
    print('%s|%.2f|%.2f|%s|%.2f|%.2f|%.1f|%s|%.2f|%.2f|%.2f|%.2f|%.1f|%.1f|%.1f|%.1f|%.1f|%.1f|%.1f|%.2f|%.0f|%s|%s|%s' % (
        name, cw, ch[1], ch[2], bal, f_ratio, v_curr, status,
        p130_cw, p130_ch, p115_cw, p115_ch,
        res130_cw, res130_ch, res115_cw, res115_ch,
        d5, d10, d20, repay_ratio, percentile, temp, diverge, repay_warn))

for name, s in stocks.items():
    compute(name, s)
