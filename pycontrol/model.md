```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 定义  的分子和分母
num = [1]  # 分子为1
den = [1, 2, 1]  # 分母为1s^2 + 2s + 1

# 创建传递函数模型
sys = signal.TransferFunction(num, den)

# 生成输入信号
t = np.linspace(0, 5, 100)  # 时间从0到5，共100个点
u = np.sin(t)  # 正弦输入信号

# 使用传递函数模型计算系统的输出
t, y, _ = signal.lsim(sys, u, t)

# 绘制输入和输出信号
plt.plot(t, u,"k", label='输入信号')
plt.plot(t, y, label='输出信号')
plt.xlabel('时间')
plt.ylabel('信号幅值')
plt.legend()
plt.show()




import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 定义传递函数的分子和分母
num = [1]  # 分子为1
den = [1, 2, 1]  # 分母为1s^2 + 2s + 1

# 转换为状态空间模型
A, B, C, D = signal.tf2ss(num, den)

# 系统初始状态
x0 = [0, 0]  # 初始状态向量

# 生成输入信号
t = np.linspace(0, 5, 100)  # 时间从0到5，共100个点
u = np.sin(t)  # 正弦输入信号

# 使用状态空间模型计算系统的输出
t, y, _ = signal.lsim((A, B, C, D), u, t, X0=x0)

# 绘制输入和输出信号
plt.plot(t, u,"k", label='输入信号')
plt.plot(t, y, label='输出信号')
plt.xlabel('时间')
plt.ylabel('信号幅值')
plt.legend()
plt.show()





```


```
            K
G(s) = -------------
       s^2 + bs + c

```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def car_speed(throttle_input):
    # 定义传递函数的分子和分母系数
    K = 1.0
    b = 0.5
    c = 2.0
    num = [K]
    den = [1, b, c]

    # 构建传递函数
    transfer_function = signal.TransferFunction(num, den)

    # 模拟输入信号
    t = np.linspace(0, 10, 1000)  # 时间范围为0到10秒
    u = throttle_input * np.sin(t)  # 油门输入信号

    # 模拟系统响应
    t, y = signal.step(transfer_function, T=t, X0=0)

    # 绘制输入和输出信号的图形
    plt.figure()
    plt.plot(t, u, label='Throttle Input')
    plt.plot(t, y, label='Speed Output')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

    # 模拟汽车速度控制系统
throttle_input = 0.5  # 油门输入信号，范围为0到1
car_speed(throttle_input)
```