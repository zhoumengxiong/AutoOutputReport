# -*- coding: utf-8 -*-
from sklearn.naive_bayes import GaussianNB

# 0:晴 1：阴 2：降水 3：多云
data_table = [["date", "weather"],
              [1, 0],
              [2, 1],
              [3, 2],
              [4, 1],
              [5, 2],
              [6, 0],
              [7, 0],
              [8, 3],
              [9, 1],
              [10, 1]]
# 当天的天气
x = [[0], [1], [2], [1], [2], [0], [0], [3], [1]]
# 当天的天气对应后一天的天气
y = [1, 2, 1, 2, 0, 0, 3, 1, 1]
# 现在把训练数据和对应的分类放入分类器中进行训练
clf = GaussianNB().fit(x, y)
p = [[1]]
print(clf.predict(p))
