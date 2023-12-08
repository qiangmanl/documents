T = 1  # 时间跨度（单位为年）
N = 252  # 时间步长（每年的交易日数量）
dt = T / N  
S0 = 100





def fact(mu, sigma, dt, z):
    return np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
    
Z = np.random.standard_normal(N) 
mu = 0.05
sigma = 0.2
l = []
for z in Z:
    l.append(fact(mu,sigma,dt,z))
plt.hist(l)
plt.show()




l = []
sigma = 0.2
mu = 0.05
interval = 0.05
num_elements = 100
arr = np.arange(num_elements) * interval + mu
for mu in arr:
    l.append(fact(mu,sigma,dt,z))
plt.plot(l)
plt.show()



l = []
sigma = 0.2
mu = 0.05
interval = 0.2
num_elements = 100
arr = np.arange(num_elements) * interval + sigma
for sigma in arr:
    l.append(fact(mu,sigma,dt,z))
plt.plot(l)
plt.show()



mu = 0.05
sigma = 0.2
l = []
for i in range(252):
    dt = i/N
    l.append(fact(mu,sigma,dt,z))
plt.plot(l)
plt.show()


#完整的几何布朗运动
import numpy as np
import matplotlib.pyplot as plt

# Parameters
mu = 0.02  # Drift (平均收益率)
sigma = 1  # Volatility (波动率)
S0 = 100  # 初始价格
T = 1  # 时间跨度（单位为年）
N = 252  # 时间步长（每年的交易日数量）
dt = T / N  # 时间步长

# Generate random numbers from standard normal distribution
z = np.random.standard_normal(N)

# Generate stock price path
t = np.linspace(0, T, N+1)
S = np.zeros(N+1)
S[0] = S0

for i in range(1, N+1):
    S[i] = S[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z[i-1])

# Plot the simulated stock price path
plt.plot(t, S)
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.title('Geometric Brownian Motion')
plt.grid(True)
plt.show()


#平均收益率
price_diff = np.diff(S)
returns = price_diff / S[:-1] * 100
returns.mean()


std_returns = np.std(returns)

# 波动率

historical_volatility = std_returns * np.sqrt(252)
print(historical_volatility)





