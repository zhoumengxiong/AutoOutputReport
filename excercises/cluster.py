# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 从磁盘读取城市经纬度数据
f = open(r"F:\Python_project\PythonI_project\China_city_lon_lat.txt",
         encoding='utf-8')
text = f.read()
x = [[float(x.split(',')[1]), float(x.split(',')[2][:-1])]
     for x in text.split(';')]

# 转换成numpy array
x = np.array(x)

# 类簇的数量
n_clusters = 5

# 现在把数据和对应的分类数放入聚类函数中进行聚类
cls=KMeans(n_clusters).fit(x)

# x中每项所属分类的一个列表
cls.labels_

# 画图
markers=['^','x','o','*','+']
for i in range(n_clusters):
    members=cls.labels_==i
    plt.scatter(x[members,0],x[members,1],s=60,marker=markers[i],alpha=0.5)

plt.title('')
plt.show()