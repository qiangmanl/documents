```python
#插入某行
com = """sed -i '3s/^/start,open,high,low,close,volume,closed,quote asset volume,number of trades,\
taker buy base asset volume,taker buy quote asset volume,ignore\\n/' data.csv """
x = os.popen(com,"r",1)
```
