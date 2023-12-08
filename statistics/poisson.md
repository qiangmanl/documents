```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

#平均每天卖出的商品数量
lambda_ = 30
size=3650
# 生成泊松分布的随机样本（模拟十年的销售数量）
sales = poisson.rvs(mu=lambda_, size=size)
days = np.arange(1, size+1)
plt.bar(days, sales)
plt.title('Daily Sales of Buns')
plt.xlabel('Day')
plt.ylabel('Number of Buns Sold')
plt.show()


#2
plt.hist(sales, bins=range(0, max(sales) + 1), align='left', rwidth=0.8, density=True)
# 绘制泊松分布的概率质量函数（PMF）
x = np.arange(0, max(sales) + 1)
pmf = poisson.pmf(x, mu=lambda_)
print(f'sum(pmf)=={sum(pmf)}')
plt.plot(x, pmf, 'ro-', lw=2)

# 添加标题和标签
plt.title('Poisson Distribution - Daily Sales of Buns')
plt.xlabel('Number of Buns Sold')
plt.ylabel('Probability')

# 显示图形
plt.show()

#思考：
如何确定概率
```
