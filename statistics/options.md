```python
import numpy
import pandas as pd
#freq='B':周末   periods:日期天数
#freq默认为D 所以一整年
start_year = 2022
#额外5年的数据
ext_years = 10

start_scale=0.02
S0 = 100
df = pd.DataFrame(index=pd.date_range(start=f'{str(start_year)}-01-01', end=f'{str(start_year)}-12-31'))
one_year_traded_days = len(df)
returns = np.random.normal(loc=0, scale=start_scale, size=one_year_traded_days)

# 标的资产价格序列 
prices = S0 * np.exp(np.cumsum(returns))
# df = pd.DataFrame({'Price': prices}, index=pd.date_range(start='2022-01-01', periods=one_year_traded_days, freq='B'))
df['Price'] = prices
df['Return'] = df['Price'].pct_change()
df["Return"].iloc[0] =  df["Price"].iloc[0] / S0 - 1
# 每日相对一年的波动率,头年算不出
# df["daily_volatility"] = np.nan
# df["annual_volatility"] = np.nan


#
for i in range(ext_years):
    new_year = start_year + (i + 1)
    new_df = pd.DataFrame(index=pd.date_range(start=f'{str(new_year)}-01-01', end=f'{str(new_year)}-12-31'))
    len(new_df)
    returns = np.random.normal(loc=0, scale=random.uniform(0.007, 0.05), size=len(new_df))
    S = df["Price"].iloc[-1]
    new_prices =  S * np.exp(np.cumsum(returns))
    new_df['Price'] = new_prices
    new_df['Return'] = new_df['Price'].pct_change()
    new_df["Return"].iloc[0] =  new_df["Price"].iloc[0] / S - 1
    df = pd.concat([df, new_df], axis=0)

df["daily_volatility"] = df['Return'].rolling(window=365).std()
# df["daily_volatility"] = df['Return'].std()
#年化波动
df["annual_volatility"] = df["daily_volatility"] * np.sqrt(one_year_traded_days)


# _df = pd.DataFrame(index=pd.date_range(start=f'{str(start_year)}-01-01', end=f'{str(start_year)}-12-31'))
# _df["daily_volatility"] = np.nan
# _df["annual_volatility"] = np.nan


plt.plot(df["daily_volatility"])
plt.show()




K  = 100
T = 365/365
r = 0.05

```
