import os
import pymysql
import time
import subprocess
config = {
    'host': "localhost",  # 本地的话就是这个
    'user': "Dream",  # 输入你的数据库账号
    'password': "Dream123$",  # 以及数据库密码
    'db': "raw_data",  # 数据库名（database名）
    'charset': 'utf8mb4'  # 读取中文不想乱码的话，记得设置这个
}
# 打开数据库连接
db = pymysql.connect(**config)  # 使用关键字参数特性，这样好看一些
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 创建SQL查询语句
country_updated = """SELECT DISTINCT country from sw_checklist where Remark in ('Update','Add')"""
cursor.execute(country_updated)
country_tup = cursor.fetchall()
countries = []
for x in range(len(country_tup)):
    countries.append(country_tup[x][0])
file_path = r'F:\Python在路上\PythonI_project\SW checklist mails sending'
for country in countries:
    print(country)
    file = os.path.join(file_path, country)
    print(file)
    try:
        subprocess.Popen(["python",file+".py"])
        # time.sleep(10)
    except:
        continue
