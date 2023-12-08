```python
import numpy as np
import matplotlib.pyplot as plt

def get_data(l):
    l = l.split("\n")
    m = []
    for i in l:
        m.append(float(i))
    m  = np.array(m)
    return m


observations = get_data(l)


def predict_trajectory(A, B, C, Q, R, initial_state, observations):
    num_timesteps = len(observations) 
    num_states = A.shape[0]

    # 初始化预测结果
    predicted_states = np.zeros((num_timesteps, num_states))

    # 初始化状态估计
    state_estimate = initial_state
    covariance_estimate = np.eye(num_states)

    for t in range(num_timesteps - 1):
        # 预测步骤
        predicted_state = A.dot(state_estimate)
        predicted_covariance = A.dot(covariance_estimate).dot(A.T) + Q

        # 更新步骤
        innovation = observations[t] - C.dot(predicted_state)
        innovation_covariance = C.dot(predicted_covariance).dot(C.T) + R
        kalman_gain = predicted_covariance.dot(C.T).dot(np.linalg.inv(innovation_covariance))

        state_estimate = predicted_state + kalman_gain.dot(innovation)
        covariance_estimate = (np.eye(num_states) - kalman_gain.dot(C)).dot(predicted_covariance)

        # 保存预测结果
        predicted_states[t+1] = state_estimate

    return predicted_states

# 定义状态转移矩阵和输入矩阵
A = np.array([[1, 1], [0, 1]])
B = np.array([0, 1])

# 定义观测矩阵
C = np.array([[1, 0]])

# 定义状态噪声协方差矩阵和观测噪声协方差矩阵
Q = np.array([[0.1, 0], [0, 0.1]])
R = np.array([[1]])

# 定义初始状态向量
initial_state = np.array([0, 0])

# 定义观测值序列（更长且具有波动性）
# num_observations = 100
# observations = np.random.normal(15, 30, num_observations)

# 预测物体轨迹
predicted_trajectory = predict_trajectory(A, B, C, Q, R, initial_state, observations)

# 绘制预测结果
plt.figure()
plt.plot(observations, label='Observations')
plt.plot(predicted_trajectory[:, 0], label='Predicted State 1')
plt.plot(predicted_trajectory[:, 1], label='Predicted State 2')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()

predicted_trajectory[:, 0]

```



```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def predict_trajectory(num, den, Q, R, initial_state, observations):
    num_timesteps = len(observations)
    num_states = len(initial_state)

    # 初始化预测结果
    predicted_states = np.zeros((num_timesteps, num_states))

    # 初始化状态估计
    state_estimate = initial_state
    covariance_estimate = np.eye(num_states)

    # 将传递函数转换为状态空间表示
    A, B, C, D = signal.tf2ss(num, den)

    for t in range(num_timesteps):
        # 预测步骤
        predicted_state = A.dot(state_estimate) + B * observations[t]
        predicted_covariance = A.dot(covariance_estimate).dot(A.T) + Q

        # 更新步骤
        innovation = observations[t] - C.dot(predicted_state)
        innovation_covariance = C.dot(predicted_covariance).dot(C.T) + R
        kalman_gain = predicted_covariance.dot(C.T).dot(np.linalg.inv(innovation_covariance))

        state_estimate = predicted_state + kalman_gain.dot(innovation)
        covariance_estimate = (np.eye(num_states) - kalman_gain.dot(C)).dot(predicted_covariance)

        # 保存预测结果
        predicted_states[t] = state_estimate

    return predicted_states

# 定义传递函数的分子和分母多项式系数
num = [1]  # 分子多项式系数
den = [1, 1]  # 分母多项式系数

# 定义状态噪声协方差矩阵和观测噪声协方差矩阵
Q = np.array([[0.1]])  # 状态噪声协方差矩阵
R = np.array([[1]])  # 观测噪声协方差矩阵

# 定义初始状态向量
initial_state = np.array([0])

# 定义观测值序列（更长且具有波动性）
num_observations = 100
observations = np.random.normal(15, 30, num_observations)

# 预测物体轨迹
predicted_trajectory = predict_trajectory(num, den, Q, R, initial_state, observations)

# 绘制预测结果
plt.figure()
plt.plot(observations, label='Observations')
plt.plot(predicted_trajectory, label='Predicted State')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()



```