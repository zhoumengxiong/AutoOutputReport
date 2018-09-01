# -*- coding: utf-8 -*-
import pandas as pd
import datetime


def getNowYearWeek():
    # 当前时间年第几周的计算
    timenow = datetime.datetime.now()
    NowYearWeek = timenow.isocalendar()
    return NowYearWeek


def sale_transform():
    wk = str(18) + str(getNowYearWeek()[1] - 2)  # 上上周，本周基础上减2
    df = pd.read_excel(r"F:\share2linux\sale.xlsx")
    df.drop(index=0, inplace=True)
    df = df.iloc[:, [0, 6, 7, 8, 9, 3, 14, 10, 11, 17, 13, 12, 15, 16, 18]]
    """if "来源" not in df.columns:
        df.insert(0, "来源", "Transsion")"""
    df.insert(7, '品牌２', df['品牌'])
    df = df.set_index('日期')
    # 当前周所处的日期段
    df = df.loc['2018-08-12':'2018-08-18']  # 需要每周修改,在原有日期基础上加7天就行了
    df = df.reset_index()
    df_date = df['日期']
    df = df.drop('日期', axis=1)
    df.insert(2, '日期', df_date)
    # 写入多少周
    df.insert(2, '周', wk)
    df.insert(12, 'model2', df['规格型号'])
    df['model2'] = df['model2'].str.upper()
    pattern1 = r'-?[A-Z0-9]*\(?[0-9]+\+[0-9]+\)?'
    pattern2 = r'-[A-Z0-9]+'
    pattern3 = r'\s+'
    df['model2'] = df['model2'].str.replace(pattern1, '')
    df['model2'] = df['model2'].str.replace(pattern2, '')
    df['model2'] = df['model2'].str.strip()
    df['model2'] = df['model2'].str.replace(pattern3, '')
    df.to_csv(r"F:\share2linux\sale.csv", index=False, encoding='utf_8_sig')


if __name__ == '__main__':
    sale_transform()
