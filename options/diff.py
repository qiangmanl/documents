import yfinance as yf
from scipy.stats import norm
import numpy as np

stock1 = yf.Ticker('AAPL')
stock2 = yf.Ticker('MSFT')

data1 = stock1.history(period='1y')
data2 = stock2.history(period='1y')

# 价格对数差分
delta_s = np.log(data1['Close']) - np.log(data2['Close'])

# 对数差分标准差
std_s = np.std(delta_s)

# 隐含波动率
iv1 = stock1.options['2023-01-20'].impliedVolatility
iv2 = stock2.options['2023-01-20'].impliedVolatility

# 计算Delta
delta1 = stock1.options['2023-01-20'].greeks['delta']
delta2 = stock2.options['2023-01-20'].greeks['delta']
delta_index = delta1 - delta2

#价差
price_spread = stock1.options['2023-01-20'].lastPrice - stock2.options['2023-01-20'].lastPrice

# Delta指数标准差
std_d = std_s * np.abs(delta_index)

# Delta指数Z值
z_score = delta_index / std_d

# Delta指数P值
p_value = norm.cdf(z_score)


if p_value < 0.05:
    if np.abs(iv1 - iv2) < 0.05:
        pass
