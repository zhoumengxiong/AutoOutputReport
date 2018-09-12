# -*- coding: utf-8 -*-
from sklearn import svm
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from pprint import pprint

newsgoups_train = fetch_20newsgroups(subset='train')
pprint(list(newsgoups_train.target_names))
# 20个主题
"""['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball',
    'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']"""

# 这里选取4个主题
categories = ['alt.atheism', 'comp.graphics',
              'sci.med', 'soc.religion.christian']

# 下载这4个主题里的文件
twenty_train = fetch_20newsgroups(subset='train', categories=categories)

# 文件内容保存在twenty_train.data这个变量里，现在对内容进行分词和向量化操作
count_vect = CountVectorizer()
x_train_counts = count_vect.fit_transform(twenty_train.data)

# 接着对向量化之后的结果做TF-IDF转换
tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)

# 现在把TF-IDF转换后的结果和每条结果对应的主题编号twenty_train.target放入分类器中进行训练
clf = svm.SVC(kernel='linear').fit(x_train_tfidf,twenty_train.target)

# 创建测试集合，这里有2条数据，每条数据一行内容，进行向量化和TF-IDF转换
docs_new = ['God is love', 'OpenGL on the GPU is fast']
x_new_counts = count_vect.transform(docs_new)
x_new_tfidf = tfidf_transformer.transform(x_new_counts)

# 预测
predicted = clf.predict(x_new_tfidf)

# 打印结果
for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, twenty_train.target_names[category]))
