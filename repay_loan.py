import math

Rate = 0.0315
rat = Rate / 12

loan = 3000000
n = 360

# 等额本金
# 每月偿还本金固定为 portion = loan / n
# t1 时刻共需还款 a1 = portion + portion * n * r
# t2 时刻共需还款 a2 = portion + portion * (n-1) * r
# tn 时刻共需还款 an = portion + portion * 1 * r
portion = loan / n
an = portion + portion * rat
a1 = portion + portion * n * rat
a_total = portion * n + portion * rat * (n+1) * n/2

# 等额本息
# t1 时刻偿还本金 b1, 共需还款 a1 = b1 + loan * r
# t2 时刻偿还本金 b2, 共需还款 a2 = b2 + (loan - b1) * r = a1
# 因为a1 == a2 所以 b2 = b1 * (1 + r), 易证 bk+1 = bk (1+r)
# tk 时刻偿还本金 bk, 共需还款 ak = b1*(1+r)^(k-1) + (loan - b1 - b2 -...-bk-1) * r
# tn 时刻偿还本金 bn  共需还款 an = b1*(1+r)^(n-1) + (loan - b1 - b2 -...-bn-1) * r 至此还清
# 总共本金 loan = b1 + b2 +...+ bn = b1 * [(1+r)^n -1]/r 
factor = (math.pow(1+rat, n) - 1)/rat
b1 = loan / factor
month_repay = b1 + loan * rat
total_repay = month_repay * n
print("done")