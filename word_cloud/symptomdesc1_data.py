# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

# 创建根据机型或者品牌查询客诉数据语句

models = ('X573',)
brands = ['Infinix', 'TECNO', 'Itel']
engine = create_engine(
    'mysql+mysqlconnector://root:Dream123$@localhost/raw_data?charset=utf8')
for model in models:
    sql_by_model = """select defectdesc1 from call_month where model='%s' and countryname!='India' and 
    symptomdesc1!=''""" % model
    pathname = r"F:\wordcloud\%s.xlsx" % model
    df = pd.read_sql(sql_by_model, engine)
    df['defectdesc1'] = df['defectdesc1'].str.lower()
    df.to_excel(pathname, index=False, header=False)
