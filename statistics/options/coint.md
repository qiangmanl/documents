```python

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
n = 10000
random_walk = np.cumsum(np.random.randn(n))

plt.plot(random_walk)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Random Walk')
plt.show()

随机游走的p 值与单位检验
from statsmodels.tsa.stattools import adfuller

result = adfuller(random_walk)
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')
print(f'Critical Values:')
for key, value in result[4].items():
    print(f'   {key}: {value}')




#时间序列是从一个正态分布中抽取的随机数
np.random.seed(0)
n = 10000
stationary_series = np.random.randn(n)

plt.plot(stationary_series)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Stationary Series')
plt.show()

result = adfuller(stationary_series)
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')
print(f'Critical Values:')
for key, value in result[4].items():
    print(f'   {key}: {value}')
    
    
    
    
直观显示是否符合正态分布
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 生成正态分布的拟合曲线
mu, sigma = np.mean(stationary_series), np.std(stationary_series)
x = np.linspace(np.min(stationary_series), np.max(stationary_series), 100)
fit_norm = norm.pdf(x, mu, sigma)

# 绘制stationary_series的直方图和正态分布拟合曲线
plt.hist(stationary_series, bins=10, density=True, alpha=0.7, label='Data')
plt.plot(x, fit_norm, 'r', label='Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram and Normal Distribution of Stationary Series')
plt.legend()
plt.show()

# 生成正态分布的拟合曲线
mu, sigma = np.mean(random_walk), np.std(random_walk)
x = np.linspace(np.min(random_walk), np.max(random_walk), 100)
fit_norm = norm.pdf(x, mu, sigma)

# 绘制random_walk的直方图和正态分布拟合曲线
plt.hist(random_walk, bins=10, density=True, alpha=0.7, label='Data')
plt.plot(x, fit_norm, 'r', label='Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram and Normal Distribution of Random Walk')
plt.legend()
plt.show()  

```



```
随机游走序列的预测方法：

随机游走序列是一个非平稳序列，其未来值的预测具有一定的困难。因为随机游走序列的未来值是通过当前值加上一个随机扰动得到的，随机扰动是难以预测的。因此，对随机游走序列的预测主要依赖于过去的观测值，例如使用移动平均方法或指数平滑方法进行预测。这些方法主要关注序列的趋势和平稳化过程。
另一种常用的方法是差分预测，即对随机游走序列进行一阶差分，得到一个平稳序列，然后对平稳序列进行预测。这种方法假设差分后的序列是平稳的，可以应用平稳时间序列的预测方法，如自回归移动平均模型（ARMA）或自回归积分滑动平均模型（ARIMA）。

正态分布序列的预测方法：
正态分布序列是一个平稳序列，其未来值的预测相对较为简单。由于正态分布具有明确的数学性质，我们可以使用统计模型来对未来值进行预测。常用的方法包括使用均值和方差来估计未来值，并且可以利用正态分布的概率密度函数来计算置信区间。
对于正态分布序列的预测，常见的方法包括均值回归模型（如线性回归模型）或基于正态分布的时间序列模型（如高斯过程或ARMA模型）。
```