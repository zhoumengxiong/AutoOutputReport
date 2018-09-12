# -*- coding: utf-8 -*-
from sklearn import svm

# 年龄
x = [[34], [33], [32], [31], [30], [30], [25], [23], [22], [18]]
# 质量
y = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1]

# 现在把训练数据和对应的分类放入分类其中进行训练
# 这里使用rbf
clf = svm.SVC(kernel='rbf').fit(x, y)

# 预测年龄30的人的质量
p = [[30]]
print(clf.predict(p))
