
```python 
import csv
import pandas as pd
def csv_data_generator(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # 获取 CSV 文件的标题行
        for row in reader:
            yield dict(zip(headers, row))

def readdf():
    file_path = 'data.csv'
    data_generator = csv_data_generator(file_path)
    for data_point in data_generator:
        yield from [data_point]

x = readdf()
next(x)
next(x)
next(x)


```
