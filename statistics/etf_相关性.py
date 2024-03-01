from datetime import datetime
import akshare as ak
from matplotlib import pyplot as plt
import pandas as pd
import os

# ak.fund_etf_hist_em(symbol=etf_symbols[0], period="daily", start_date="20000101", end_date="20230201", adjust="hfq")
# ak.fund_etf_hist_em(symbol=etf_symbols[0], period="daily", start_date="19000101", adjust="hfq")



new = True
history_len = 1500
corr_limit = 0.98
index = []
# 确认工作目录下data文件夹(如果有) 是用于保存当前数据的.
# new== True 确保每次执行都会删除data文件夹, 需要保存下载下来的文件夹就设置new 为False 并且根据旧数据的日期修改else下的trade_day
#
if new == False:
    if os.path.exists("data"):
        import shutil
        shutil.rmtree('data')
    #不要修改
    trade_day = datetime.now().date()
else:
    # 如果使用旧数据，更改new为False，并且根据旧数据的日期修改trade_day
    trade_day = pd.to_datetime("2024-01-24")
work_symbols = []
dfs  = dict()
# 从ak 上面获取etf 历史数据
def get_etf_hist(symbol,start='',end='',adjust="hfq",period="daily",special=[]):
    start = start or "19000101"
    if end:
        hist = ak.fund_etf_hist_em(symbol=symbol, period=period, start_date=start,end=end,adjust=adjust)
    else:
        hist = ak.fund_etf_hist_em(symbol=symbol, period=period, start_date=start, adjust=adjust)
    if len(hist.index) == 0:
        return hist
    hist.set_index("日期", inplace=True)
    hist.index = hist.index.astype('datetime64[ns]')
    if special == []:
        return hist
    else:
        return hist.loc[:,special]

def load_df():
    os.makedirs("data",exist_ok=True)
    data_dir = os.listdir("data")
    for symbol_file in data_dir:
        symbol = symbol_file[:-4]
        df = pd.read_csv(f"data/{symbol_file}", index_col='日期', parse_dates=['日期'])
        dfs[symbol] = df

load_df()
etf_detail  = ak.fund_etf_spot_em()
etf_symbols = etf_detail["代码"].values
for symbol in etf_symbols:
    if symbol not in dfs:
        df = get_etf_hist(symbol,special=["收盘"])
        if len(df.index) > 0:
            df.columns = [symbol]
            dfs[symbol] = df 
            print(f"save symbol {symbol} to data dir")
            df.to_csv(f'data/{symbol}.csv')


for symbol in dfs:
    symbol_index = dfs[symbol].dropna().index 
    if len(symbol_index) < history_len or (symbol_index[-1] != trade_day):
        continue
    if len(index) == 0:
        index = symbol_index
    else:
        work_symbols.append(symbol)
        index = symbol_index.intersection(index)

print(len(index))
print(len(work_symbols))
corr_df = pd.DataFrame(index=index)
for symbol in work_symbols:
    corr_df.loc[:,symbol] = dfs[symbol]

all_corr = corr_df.corr()
# 剔除没有相关性的symbol
# del_symbols = []
result = pd.DataFrame()
for symbol in work_symbols:
    x = all_corr[symbol].sort_values(ascending=False) 
    x = x.loc[x > corr_limit]#.loc[x!=1]
    if len(x.index) > 0:
        result[x.name] = x

result.dropna(axis=1,how='all',inplace=True)


# symbol1 = "159907"
# symbol2 = "159943"



# hist1 = d[symbol1].loc[index][symbol1].pct_change()
# hist2 = d[symbol2].loc[index][symbol2].pct_change()
# hist1 = dfs[symbol1].loc[index][symbol1]
# hist2 = dfs[symbol2].loc[index][symbol2]

# start1 = hist1.iloc[0]
# start2 = hist2.iloc[0]
# return1 = ((hist1 - start1) / start1) * 100
# return2 = ((hist2 - start2) / start2) * 100

# df1 = pd.DataFrame(hist1).rename(columns={hist1.name:"close"})
# df2 = pd.DataFrame(hist2).rename(columns={hist2.name:"close"})
# from trader import local
# df1.to_csv(f'{local.domain_dir}/159907.etf.csv')
# df2.to_csv(f'{local.domain_dir}/159943.etf.csv')

# plt.plot(return1.index,return1)
# plt.plot(return1.index,return2)
# plt.plot(return1.index,return1 - return2)
# plt.show()


# def get_return(history):
#     start = history.iloc[0]
#     returns = ((history - start) / start) * 100
#     return returns