```python

import numpy as np
import matplotlib.pyplot as plt

# 生成模拟数据
np.random.seed(123)
n = 100
x = np.arange(n)

y1 = 2 * x + 5 + np.random.normal(0, 10, n)
y2 = 2 * x + 5 + np.random.normal(0, 30, n)
# 创建DataFrame对象
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))


df1 = pd.DataFrame({'x': x, 'y': y1})
ax1.scatter(df1['x'], df1['y'])
ax1.plot(df1['x'], np.poly1d(np.polyfit(df1['x'], df1['y'], 1))(df1['x']), color='red')

df2 = pd.DataFrame({'x': x, 'y': y2})
ax2.scatter(df2['x'], df2['y'])
ax2.plot(df1['x'], np.poly1d(np.polyfit(df2['x'], df2['y'], 1))(df2['x']), color='green')
plt.show()

```
