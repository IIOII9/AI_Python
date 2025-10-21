import pandas as pd
import chardet

csvFileName = "D:/code/AI_Python/DataProcess/data.csv"
try:
    df = pd.read_csv(csvFileName)
    print(df.head())  # 显示前5行
except Exception as e:
    print(f"发生异常{e}")
    
# 先检测编码
with open(csvFileName, "rb") as f:
    raw_data = f.read()
encoding = chardet.detect(raw_data)['encoding']

# 使用检测到的编码读取 CSV
df = pd.read_csv(csvFileName, encoding=encoding)
print(df.head())