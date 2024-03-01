import numpy as np 
import pandas as pd
from scipy.optimize import brentq
from scipy.stats import norm


def simulate_daily_underlying(size:int=1000, S0:int=100,end:str='2022-01-01',seed:bool=True):
    np.random.seed(123)
    returns = np.random.normal(loc=0, scale=0.02, size=size)
    prices = S0 * np.exp(np.cumsum(returns))
    prices = np.flip(prices)
    df = pd.DataFrame({'Price': prices}, index=pd.date_range(end='2022-01-01', periods=size, freq='B'))
    df['Return'] = df['Price'].pct_change()
    return df 
# 暂定size数量越多越好


df = simulate_daily_underlying(size=365*10)
df = simulate_daily_underlying(size=365*5)


#np.diff(np.log(prices))


volatility = df['Return'].std()
# 暂定年化收益率可以通过小时和每日和分交易产生
annual_volatility = volatility * np.sqrt(365)


S = df['Price'].iloc[-1]
sigma = annual_volatility
K  = 100
T = 365/365
r = 0.05

def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    call_price = S * Nd1 - K * np.exp(-r * T) * Nd2
    return call_price

def implied_volatility(S, K, T, r, sigma, option_price):
    # 牛顿-拉夫森方法
    def f(sigma):
        """
        当使用黑-斯科尔斯期权定价模型计算看涨期权理论价格时，结果应该是非负数。
        如果计算得到的看涨期权理论价格小于市场价格，则意味着市场上的看涨期权价格偏高，
        这时应该考虑购买看涨期权以获得利润，而如果计算得到的看涨期权理论价格大于市场价格，
        则意味着市场上的看涨期权价格偏低，这时应该考虑卖出看涨期权以获得利润。
        如果理论大于实际，看空
        因此，在计算隐含波动率时，如果计算得到的期权理论价格与市场价格的差值为负数，
        则意味着所选择的波动率偏低，需要增加波动率的值，以使得计算得到的期权理论价格与市场价格的差值为正数。
        如果计算得到的期权理论价格与市场价格的差值为正数，则意味着所选择的波动率偏高，需要减少波动率的值，
        以使得计算得到的期权理论价格与市场价格的差值为正数。
        """
        return black_scholes_call(S, K, T, r, sigma) - option_price
    iv = brentq(f, a=0.001, b=10.0)  # 查找方程的根
    return iv

#实际的期权价格
option_price = 60

iv = implied_volatility(S, K, T, r, sigma, option_price)

print(black_scholes_call(S, K, T, r, sigma) - option_price,iv)


l1 = []
l2  = []
S0 = 100
K  = 100
T = 365/365
r = 0.05
for i in range(10000):

    returns = np.random.normal(loc=0, scale=0.02, size=250)
    prices = S0 * np.exp(np.cumsum(returns))
    df = pd.DataFrame({'Price': prices}, index=pd.date_range(start='2022-01-01', periods=250, freq='B'))

    df['Return'] = df['Price'].pct_change()
    daily_volatility = df['Return'].std()
    annual_volatility = daily_volatility * np.sqrt(252)
    S = df['Price'].iloc[-1]
    sigma = daily_volatility
    option_price = black_scholes_call(S, K, T, r, sigma)
    iv = implied_volatility(S, K, T, r, sigma, option_price)
    l1.append(option_price)
    l2.append(iv)
    print(len(l2))

import matplotlib.pyplot as plt
plt.hist2d(l2, l1, bins=50, cmap='Blues')
plt.colorbar()
plt.xlabel('Implied Volatility')
plt.ylabel('Option Price')
plt.show()

# plt.hexbin(l2, l1, gridsize=50, cmap='Blues')
# plt.colorbar()
# plt.xlabel('Implied Volatility')
# plt.ylabel('Option Price')
# plt.show()


"""
在这个实验中有什么错误?

在这个实验中，主要是使用了随机数生成价格数据，这可能导致价格的分布与真实市场存在一定的差异。
此外，使用布伦特-高根方法计算隐含波动率时，使用了一个固定的初始猜测值，这可能会影响结果的准确性。
此外，使用了历史价格数据来估计未来的波动率，这可能与真实市场存在一定的差异。最后，该模型是基于假设的
黑-斯科尔斯模型，这些假设在实际市场中可能不完全成立。因此，这个实验的结果应该被视为一种近似，而不是真实市场的精确反映。
那改良的办法是什么？

有一些方法可以改进这个实验，例如：
增加模拟的样本量，可以通过增加returns数组的长度来实现，这将导致更精确的估计。
使用更准确的数据源，例如真实市场数据，而不是通过简单的随机漫步生成的数据。
通过对比不同的隐含波动率计算方法来减小误差。可以使用其他计算隐含波动率的方法，例如牛顿-拉弗森法或蒙特卡罗模拟法等，以减少误差。
重复实验多次并取平均值来减小随机误差。
需要根据具体情况选择合适的方法来改进实验。

"""
