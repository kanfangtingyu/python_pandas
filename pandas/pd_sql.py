import pandas as pd
import pymysql
conn = pymysql.connect(
    host='127.0.0',
    user='root',
    password='12345678',
    database='test',
    charset='utf8'
)
mysql_page = pd.read_sql("select * from crazyant_pvuv", con = conn)
print(mysql_page)