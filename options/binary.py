import numpy as np
from scipy.stats import norm

def bs_option_price(S, K, T, r, sigma, option_type):
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return price

def implied_vol(S, K, T, r, option_price, option_type):
    """
    牛顿-拉夫森方法是牛顿迭代法的一种常见形式，也被称为改进的牛顿迭代法。在求解非线性方程的问题中，
    牛顿-拉夫森方法是一种快速、高效的数值方法，通常用于求解隐含波动率等问题。与二分法相比，牛顿-拉夫森方法通常具有更快的收敛速度，
    但也需要更多的计算量和较好的初始估计值。
    
    二分法和牛顿迭代法都是求解期权隐含波动率的常用数值方法，它们各有优点和缺点：

    二分法的优点是简单易懂，收敛速度较慢但具有良好的数值稳定性，而且可以保证找到唯一的隐含波动率解。缺点是需要进行多次二分查找，计算速度较慢。

    牛顿迭代法的优点是收敛速度较快，特别是对于非线性问题，收敛速度更快。
    由于每次迭代都需要计算导数，因此需要提供期权定价模型的导数计算方法，而且可能会遇到数值不稳定的情况，
    例如可能会出现发散或收敛到错误的解。为了避免这些问题，牛顿迭代法通常需要设置一些收敛条件和保护措施。
    """
    error = 1e-6
    low_vol, high_vol = 0.01, 1.0
    while (high_vol - low_vol) > error:
        mid_vol = (low_vol + high_vol) / 2
        price = bs_option_price(S, K, T, r, mid_vol, option_type)
        if price > option_price:
            high_vol = mid_vol
        else:
            low_vol = mid_vol
    return mid_vol

S = 100  # 标的资产价格
K = 100  # 行权价格
T = 1.0  # 到期时间
r = 0.05  # 无风险利率
sigma = 0.2  # 波动率
option_price = 10.5  # 期权市场价格
option_type = 'call'  # 期权类型（看涨期权）
iv = implied_vol(S, K, T, r, option_price, option_type)
print(f'Implied volatility: {iv:.4f}')
