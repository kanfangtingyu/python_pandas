import pandas as pd
fpath = "./datas/ml-latest-small/ratings.csv"
ratings = pd.read_csv(fpath)
print(ratings.head()) # 查看前几行
print(ratings.shape) # 参考数据的形状，返回行数，列数
ratings.columns # 查看列名列表
ratings.index # 查看索引列
ratings.dtypes # 查看每列数据类型