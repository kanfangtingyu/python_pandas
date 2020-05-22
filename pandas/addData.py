import pandas as pd
df = pd.read_csv("./datas/beijing_tianqi/beijing_tianqi_2018.csv")
# ,前面是选择行，后面是选择列,:是所有
df.loc[:,"bWendu"] = df["bWendu"].str.replace("℃","").astype('int32')
df.loc[:,"yWendu"] = df["yWendu"].str.replace("℃","").astype('int32')
# 新增一列
df.loc[:,"wencha"] = df["bWendu"] - df["yWendu"]

# 使用apply添加温度类型，参数（函数，axis=0/1） 0是行，1是列
def get_type(x):
    if x["bWendu"] > 33:
        return '高温'
    if x["yWendu"] < -10:
        return '低温'
    return '常温'
df.loc[:, "wendu_type"] = df.apply(get_type,axis=1)
df["wendu_type"].value_counts()  # 统计个数

# assign可以添加，但是不改变原来的

# 条件
df['wencha_type'] = ''
df.loc[df["bWendu"]-df["yWendu"]>10, "wencha_type"] = "温差大"
df.loc[df["bWendu"]-df["yWendu"]<=10, "wencha_type"] = "温差正常"
print(df["wencha_type"].value_counts())