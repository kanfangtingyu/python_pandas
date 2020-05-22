import pandas as pd
import numpy as np

# series 左侧为索引，右侧是数据
# 可以用 s1.index获取索引，values获取数据
# 使用序列或者字典创建series
s1 = pd.Series([1,'a',5.2,7])
# print(s1)

# dataframe 每列可以是不同值类型
# 既有行索引index，也有列索引columns
# 可以看成有series组成的字典

fpath = "./datas/crazyant/access_pvuv.xlsx"
df = pd.read_excel(fpath)
print(df['日期'])  # 查询列
print(df.loc[1])  # 查询行
print(df.loc[1:3])  # 查询多行，  ！！！注：python里面左开右闭，pandas里面都开
# 只查询一行，一列，返回的是pd.Series
# 查询多行、多列，返回pd.DataFrame