import pandas as pd
df = pd.read_csv("./datas/beijing_tianqi/beijing_tianqi_2018.csv")
# 重新设定index
df.set_index('ymd', inplace=True) # inplace为true时会直接改变原df，为false时会给一个新的变量

# 预处理：选出所有的温度，用正则吧C替换掉
df.loc[:,"bWendu"] = df["bWendu"].str.replace("℃","").astype('int32')
df.loc[:,"yWendu"] = df["yWendu"].str.replace("℃","").astype('int32')

# print( df.loc['2018-01-03','bWendu']) # 查询单个值
# print(df.loc['2018-01-03',['bWendu','yWendu']]) # 得到series
# print(df.loc['2018-01-03':'2018-01-05','bWendu']) # 区间查询
# print(df.loc[df["yWendu"]<10,:])  # 范围查询
# 查询最高温度小于30，最底大于15，晴天，天气为优的数据
print(df.loc[(df["bWendu"]<=30) & (df["yWendu"]>=15) & (df["tianqi"]=="晴") & (df["aqiLevel"]==1), :])

# 函数调用
# def func():
#     pass
# df.loc[func ]