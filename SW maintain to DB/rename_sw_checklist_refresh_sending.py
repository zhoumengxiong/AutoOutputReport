# -*- coding: utf-8 -*-
import os
import shutil
import pymysql
import datetime
import pyautogui
import time
import subprocess


def getNowYearWeek():
    # 当前时间年第几周的计算
    time_now = datetime.datetime.now()
    NowYearWeek = time_now.isocalendar()
    return NowYearWeek


last_week = str(getNowYearWeek()[1] - 1)
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
file_path = r'F:\Transsion\New market\latest version software checklist by country'
r = os.path.exists(file_path)
if r is False:
    print("Path doesn't exist!")
# 重命名checklist，刷新checklist，截图
else:
    path_dir = os.listdir(file_path)
    for all_dir in path_dir:
        child = os.path.join(file_path, all_dir)
        files = os.path.join(child, os.listdir(child)[0])
        for country in countries:
            if country in child:
                files_modify = files[:-7] + last_week + files[-5:]
                shutil.move(files, files_modify)
                # 打开对应国家的check list文件
                subprocess.Popen(
                    [r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE", files_modify])
                # 暂设定12S延时，excel打开超级慢，大家都懂的！
                time.sleep(12)
                # 设定每个动作的执行时间为1S
                pyautogui.PAUSE = 1
                # 将excel窗口置顶
                # pyautogui.click(1397, 31, duration=1)
                # 打开数据标签
                pyautogui.click(359, 58, duration=1)
                # 刷新数据库连接
                pyautogui.click(556, 108, duration=1)
                # 弹出安全警示，点击确认
                pyautogui.click(1011, 629, duration=1)
                # 刷新数据库需要时间，暂设定3S
                time.sleep(3)
                # 点击保存
                pyautogui.click(35, 18, duration=1)
                # 创建屏幕快照
                im = pyautogui.screenshot()
                # 截图并保存到指定目录
                croppedIm = im.crop((34, 272, 872, 976))
                croppedIm.save(os.path.join(
                    r'F:\Python在路上\PythonI_project\SW checklist images', all_dir) + '.jpg')
                # print(im.getpixel((50, 200)))
                # pyautogui.pixelMatchesColor(50, 200, (230, 230, 230))
                # 关掉当前文件
                pyautogui.click(1891, 19, duration=1)
                print(files_modify)
# 发邮件
py_path = r'F:\Python在路上\PythonI_project\SW checklist mails sending'
for country in countries:
    file = os.path.join(py_path, country)
    print(file)
    try:
        subprocess.Popen(["python", file + ".py"])
        # time.sleep(10)
    except:
        continue
