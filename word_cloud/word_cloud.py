# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import imageio

# import codecs

# fin = codecs.open('HotelComments.txt',mode = 'r', encoding = 'utf-8')
# print fin.read()

# 第一次运行程序时将分好的词存入文件
# text = ''
# with open('HotelComments.txt') as fin:
#     for line in fin.readlines():
#         line = line.strip('\n')
#         text += ' '.join(jieba.cut(line))
#         text += ' '
# fout = open('text.txt','wb')
# pickle.dump(text,fout)
# fout.close()

# 直接从文件读取数据
file = open(r"/mnt/hgfs/Transsion/Repair rate report/repair_rate_report/wordcloud/Infinix.txt", 'r')
text = file.read()
# backgroud_Image = plt.imread(r"/mnt/hgfs/Transsion/Repair rate report/repair_rate_report/wordcloud/bg.jpg")
backgroud_Image = imageio.imread(r"/mnt/hgfs/Transsion/Repair rate report/repair_rate_report/wordcloud/bg.jpg")
# block_words = ('problem', 'work', 'and', 'the')
wc = WordCloud(background_color='white',  # 设置背景颜色
               mask=backgroud_Image,  # 设置背景图片
               max_words=50,  # 设置最大现实的字数
               # stopwords=block_words,  # 设置停用词
               # font_path='C:/Users/Windows/fonts/msyh.ttf',  # 设置字体格式，如不设置显示不了中文
               max_font_size=60,  # 设置字体最大值
               random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
               )
wc.generate(text)
# image_colors = ImageColorGenerator(backgroud_Image)
# wc.recolor(color_func=image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()
file.close()
