```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# 生成示例数据
np.random.seed(42)
series_length = 100
series1 = np.random.rand(series_length) + np.sin(np.linspace(0, 4 * np.pi, series_length))
series2 = 0.8 * series1 + 0.2 * np.random.rand(series_length)

# 创建时间索引
index = pd.date_range(start='2023-01-01', periods=series_length, freq='D')

# 将数据放入DataFrame中
data = {'series1': series1, 'series2': series2}
df = pd.DataFrame(data, index=index)

# 绘制时间序列图
df.plot(figsize=(10, 6), title='Example Time Series Data')
plt.show()

# 拟合SARIMA模型
order = (1, 1, 1)  # ARIMA阶数
seasonal_order = (1, 1, 1, 12)  # 季节性阶数
model = SARIMAX(df['series1'], order=order, seasonal_order=seasonal_order)
result_series1 = model.fit(disp=False)

model = SARIMAX(df['series2'], order=order, seasonal_order=seasonal_order)
result_series2 = model.fit(disp=False)

# 进行预测
forecast_steps = 10
forecast_series1 = result_series1.get_forecast(steps=forecast_steps)
forecast_series2 = result_series2.get_forecast(steps=forecast_steps)

# 绘制预测结果
plt.figure(figsize=(10, 6))
plt.plot(df['series1'], label='Series 1')
plt.plot(df['series2'], label='Series 2')
plt.plot(forecast_series1.predicted_mean, label='Series 1 Forecast', linestyle='--')
plt.plot(forecast_series2.predicted_mean, label='Series 2 Forecast', linestyle='--')
plt.legend()
plt.title('SARIMA Forecast')
plt.show()
```