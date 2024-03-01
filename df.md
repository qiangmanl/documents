```python
# 添加一列名为 "new_column"，数据类型为 int64
df_ohlc['new_column'] = pd.Series(dtype='int64')
# 根据行赋值
df_ohlc.iloc[-1, df_ohlc.columns.get_loc('vol')] *= 2
#根据 索引来赋值
df_ohlc.loc[df_ohlc.index[-1], 'vol'] = 2

```
