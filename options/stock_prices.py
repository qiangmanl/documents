import numpy as np
import matplotlib.pyplot as plt





S0 = 100 
r = 0.05 
sigma = 0.2 
T = 1 
dt = 1 / 252 # 时间步长
num_sims = 1000 # 模拟路径数
# num_steps = T/dt
num_steps = 1
stock_prices = np.zeros((num_steps + 1, num_sims))
stock_prices[0] = S0
for i in range(num_steps):
    z = np.random.standard_normal(num_sims)
    stock_prices[i + 1] = stock_prices[i] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)
plt.plot(stock_prices[1])
plt.xlabel('Time Steps')
plt.ylabel('Stock Price')
plt.title('Simulated Stock Prices')
plt.show()




#sigma
import numpy as np
import pandas as pd

l = []
for i in range(10000):
    # np.random.seed(123)
    returns = np.random.normal(loc=0, scale=0.02, size=250)
    S0 = 100
    prices = S0 * np.exp(np.cumsum(returns))
    df = pd.DataFrame({'Price': prices}, index=pd.date_range(start='2022-01-01', periods=250, freq='B'))
    # 计算每日收益率
    df['Return'] = df['Price'].pct_change()
    # 计算每日波动率
    daily_volatility = df['Return'].std()
    # 计算年化波动率
    annual_volatility = daily_volatility * np.sqrt(252)
    l.append(annual_volatility)
    # 输出结果
    #print(f"The annualized volatility of the stock is {annual_volatility:.2%}")
plt.hist(l,bins=30)
