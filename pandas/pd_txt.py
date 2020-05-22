import pandas as pd
fpath = "./datas/crazyant/access_pvuv.txt"
pvuv = pd.read_csv(
    fpath,
    sep="\t",   # 设置分隔符
    header=None,    #  文件无标题行
    names=['pdate','pv','uv']   # 自己指定列名
)
print(pvuv)