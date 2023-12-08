```python
import numpy as np
import matplotlib.pyplot as plt

def compare_normal_distributions(n):
    #第一个参数表示均值，均值表示中间位置，注意看10和0的区别
    #第二个参数表示一个标准差，注意看1个标准差为10和为20的区别
    # 生成符合正态分布的随机数
    data1 = np.random.normal(0, 10, n)
    data2 = np.random.normal(10, 20, n)

    # 绘制直方图
    plt.hist(data1, bins=30, alpha=0.5, label='Normal(0, 10)')
    plt.hist(data2, bins=30, alpha=0.5, label='Normal(10, 20)')
    plt.legend()

    # 设置图形标题和轴标签
    plt.title('Comparison of Normal Distributions')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # 显示图形
    plt.show()

# 设置样本数量
n = 1000

# 调用函数进行比较
compare_normal_distributions(n)


```
