import pandas as pd
df = pd.read_csv("./datas/beijing_tianqi/beijing_tianqi_2018.csv")
# ,前面是选择行，后面是选择列,:是所有
df.loc[:,"bWendu"] = df["bWendu"].str.replace("℃","").astype('int32')
df.loc[:,"yWendu"] = df["yWendu"].str.replace("℃","").astype('int32')
print(df.corr())