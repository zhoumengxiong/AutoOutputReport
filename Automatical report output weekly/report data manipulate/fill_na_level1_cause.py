# -*- coding: utf-8 -*-
import pymysql


def fill_na():
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
    # 定义各类问题原因空白总数目的SQL语句
    sql_count_pwr = """select count(*) from model_select where Level1Cause='' and  CallSymptom like 'pwr%%'"""
    sql_count_acb123 = """select count(*) from model_select where Level1Cause='' and  CallSymptom REGEXP '^ACB0(1|2|3)'"""
    sql_count_acb46 = """select count(*) from model_select where Level1Cause='' and  CallSymptom REGEXP '^ACB0(4|6)'"""
    sql_count_chg = """select count(*) from model_select where Level1Cause='' and CallSymptom like  'CHG%%'"""
    # 填充各类问题原因的SQL语句
    fill_na_pwr = """update model_select set Level1Cause=%s where Level1Cause='' and  CallSymptom like 'pwr%%' limit %s"""
    fill_na_acb123 = """update model_select set Level1Cause=%s where Level1Cause='' and  CallSymptom REGEXP 
    '^ACB0(1|2|3)' limit %s"""
    fill_na_acb46 = """update model_select set Level1Cause=%s where Level1Cause='' and  
    CallSymptom REGEXP '^ACB0(4|6)' limit %s"""
    fill_na_chg = """update model_select set Level1Cause=%s where Level1Cause='' and CallSymptom like  'CHG%%' limit %s"""
    fill_na_acb99 = """update model_select set Level1Cause='battery' where Level1Cause='' and CallSymptom REGEXP '^ACB'"""
    # 查询pwr问题原因空白的总数目
    cursor.execute(sql_count_pwr)
    count = cursor.fetchall()[0][0]
    # 填充pwr问题的原因
    # cursor.execute(fill_na_pwr, ('PCBA', int(count * 0.539)))
    cursor.executemany(fill_na_pwr, [['PCBA', int(count * 0.539)], [
        'software', int(count * 0.3987)
    ], ['sub board', int(count * 0.0313)], [
        'battery',
        count - int(count * 0.539) - int(count * 0.3987) - int(count * 0.0313)
    ]])
    # 查询acb123问题原因空白的总数目
    cursor.execute(sql_count_acb123)
    count = cursor.fetchall()[0][0]
    # 填充acb123问题的原因
    # cursor.execute(fill_na_acb123, ('PCBA', int(count * 0.539)))
    cursor.executemany(fill_na_acb123, [[
        'sub board', int(count * 0.4562)
    ], ['PCBA', int(count * 0.2217)], [
        'software', int(count * 0.1657)
    ], [
        'battery',
        count - int(count * 0.4562) - int(count * 0.2217) - int(count * 0.1657)
    ]])
    # 查询acb46问题原因空白的总数目
    cursor.execute(sql_count_acb46)
    count = cursor.fetchall()[0][0]
    # 填充acb46问题的原因
    # cursor.execute(fill_na_acb46, ('PCBA', int(count * 0.539)))
    cursor.executemany(fill_na_acb46, [[
        'software', int(count * 0.3864)
    ], ['PCBA', int(count * 0.3164)], [
        'battery', int(count * 0.2422)
    ], [
        'sub board',
        count - int(count * 0.3864) - int(count * 0.3164) - int(count * 0.2422)
    ]])
    # 查询chg问题原因空白的总数目
    cursor.execute(sql_count_chg)
    count = cursor.fetchall()[0][0]
    # 填充chg问题的原因
    # cursor.execute(fill_na_chg, ('PCBA', int(count * 0.539)))
    cursor.executemany(fill_na_chg, [['PCBA', int(count * 0.4056)], [
        'sub board', int(count * 0.3933)
    ], ['software', count - int(count * 0.4056) - int(count * 0.3933)]])
    # 填充电池问题
    cursor.execute(fill_na_acb99)
    db.commit()
    db.close()


if __name__ == '__main__':
    fill_na()