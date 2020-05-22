import pandas as pd
df = pd.read_csv("./datas/beijing_tianqi/beijing_tianqi_2018.csv").head()
df.set_index('ymd', inplace=True) # inplace为true时会直接改变原df，为false时会给一个新的变量

# series 的排序 series.sort_values(ascending=True,inplace=False)

print(df["aqi"].sort_values())  # 针对series，不会改变原dataframe

# dataFrame 的排序
# 单列排序
df.sort_values(by="aqi",inplace=True)
print(df)
# 多列排序
df.sort_values(by=["aqiLevel","bWendu"],ascending=[True,False])