# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

# 创建根据机型或者品牌查询客诉数据语句

models = ['X608', 'X606', 'X604', 'X5515', 'X5514', 'S11X', 'R8S', 'P32', 'P13', 'LA7', 'KA7', 'IN6', 'F4',
          'F311', 'A62', 'A52', 'A15']
brands = ['Infinix', 'TECNO', 'Itel']
engine = create_engine(
    'mysql+mysqlconnector://Dream:Dream123$@192.168.1.105/raw_data?charset=utf8')
# 按品牌统计
for brand in brands:
    sql_by_brand = """select CallSymptom from grandtotal where EXISTS (select model 
    from np where np.model=grandtotal.model) and brand='%s'""" % brand
    pathname = r"/mnt/hgfs/Transsion/Repair rate report/repair_rate_report/wordcloud/%s.xlsx" % brand
    df = pd.read_sql(sql_by_brand, engine)
    df['CallSymptom'] = df['CallSymptom'].str.lower()
    df.to_excel(pathname, index=False, header=False)
# 按机型统计
for model in models:
    sql_by_model = """select CallSymptom from grandtotal where model='%s'""" % model
    pathname = r"/mnt/hgfs/Transsion/Repair rate report/repair_rate_report/wordcloud/%s.xlsx" % model
    df = pd.read_sql(sql_by_model, engine)
    df['CallSymptom'] = df['CallSymptom'].str.lower()
    df.to_excel(pathname, index=False, header=False)
