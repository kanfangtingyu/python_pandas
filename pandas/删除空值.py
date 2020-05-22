import pandas as pd
studf = pd.read_excel("./datas/student_excel/student_excel.xlsx", skiprows=2) # 后面这个跳过excel前两个空行

print(studf)  # 判断是否为空
# 第一列全为空，先删除
studf.dropna(axis=1, how="all", inplace=True)
print(studf)
# 删除所有空行
studf.dropna(axis=0, how="all", inplace=True)
print(studf)
# 分数列为空的填充为0
studf.loc[:,'分数'] = studf['分数'].fillna(0)
print(studf)
# 填充姓名的缺失  使用自带方法 forward fill ---> ffill
studf.loc[:,'姓名'] = studf['姓名'].fillna(method="ffill")
print(studf)
# 导出excel文件，不导出index那一列
studf.to_excel("./newdatas/student_excel_clean.xlsx", index=False)