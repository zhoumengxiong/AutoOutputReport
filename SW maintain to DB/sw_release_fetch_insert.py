# -*- coding: utf-8 -*-
import imapclient
import pyzmail
import bs4
import re
import pymysql
import shutil
import pprint


# 该函数从软件升级目录未读邮件中获取N ｖersion, software Version, sale_country_raw等信息放入dict_version_country字典中并返回
def get_dict_version_country():
    # 创建IMAP对象，登录IMAP服务器
    imapObj = imapclient.IMAPClient(
        host='partner.outlook.cn', port=993, use_uid=True)
    imapObj.login('mengxiong.zhou@carlcare.com', 'TRA+2017')
    pprint.pprint(imapObj.list_folders())
    # 选中当前操作目录为软件升级目录
    select_info = imapObj.select_folder('INBOX/软件升级', readonly=False)
    print('%d messages in INBOX/软件升级' % select_info[b'EXISTS'])
    # 设定fetch邮件范围，返回邮件UID列表
    # 自2018/7/30之后的邮件
    uids1 = imapObj.search(['Since', '30-Jul-2018'])
    # 未读邮件
    # uids2 = imapObj.search(['UNSEEN'])
    # uids1 = []
    # for id1 in uids1:
    # for id2 in uids2:
    # if id2 == id1:
    # uids1.append(id2)
    # 将UID列表拼接成以逗号分隔的字符串
    uids_string = ','.join([str(x) for x in uids1])
    print(len(uids1))
    # 将UID字符串写入到本地磁盘
    """uids_file = open('uids1.txt', 'w')
    uids_file.write(uids_string)
    uids_file.close()
    # UID文本文件备份
    shutil.copy2('uids1.txt', 'uids_bak.txt')"""
    # 　创建包含verison, sales_country_raw等信息的字典
    dict_version_country = {}
    for msgid in uids1:
        msgdict = imapObj.fetch([msgid, ], [b'BODY[]'])
        body = msgdict[msgid][b'BODY[]']
        message = pyzmail.PyzMessage.factory(body)
        # 获取邮件标题信息
        subject = message.get_subject()
        # 如果标题中含有答复，则直接调到下一次迭代
        if re.search('答复', subject, flags=re.IGNORECASE) is not None:
            continue
        # print(subject)
        # from_ = message.get_addresses('from')
        # to = message.get_addresses('to')
        # cc = message.get_addresses('cc')
        # bcc = message.get_addresses('bcc')
        # if message.text_part is not None:
        # message_text = message.text_part.get_payload().decode(message.text_part.charset)
        # if message.html_part is not None:
        # 获取邮件正文信息
        message_html = message.html_part.get_payload().decode(message.html_part.charset)
        message_html = message_html.replace('gb2312', 'utf-8')
        # 利用Ｂeautiful soup去掉html标签，提取文本信息
        message_html_soup = bs4.BeautifulSoup(message_html, "lxml")
        # clean = message_html_soup.get_text()
        # 获取软件版本信息
        pattern_version = r'\(.+-\w+-.+|\（.+-\w+-.+'
        regex_1 = re.findall(pattern_version, subject)
        if len(regex_1) == 0:
            continue
        version = regex_1[0].replace('(', '')
        version = version.replace('（', '')
        version = version.replace(')', '')
        version = version.replace('）', '')
        version = version.strip()
        model = version.split('-')[0]
        model = model.replace(' ', '')
        model = model.upper()
        SKU = version.split('-')[1]
        print(version)
        pElems = message_html_soup.select('p')
        country = []
        # 获取Ｎ version信息
        n_version = ''
        for j in range(len(pElems)):
            if pElems[j].getText() in ['H/W:', 'Number Marking（N标识）：']:
                n_version = pElems[j + 1].getText()
                pattern_n_version = r'N[0-9]{1,2}'
                regex = re.findall(pattern_n_version, n_version)
                if len(regex) != 0:
                    n_version = regex[0]
                else:
                    n_version = ''
                n_version = n_version.strip()
                break
        print(n_version)
        # 获取新市场国家信息
        for i in range(len(pElems)):
            if pElems[i].getText() == 'Sales Country:':
                sale_country_raw = pElems[i + 1].parent.get_text()
                sale_country_raw = sale_country_raw.replace('\r\n', '')
                sale_country_raw = sale_country_raw.replace('\n', '')
                sale_country_raw = sale_country_raw.replace('.', '')
                sale_country_raw = sale_country_raw.replace('，', ',')
                sale_country_raw = sale_country_raw.replace('、', ',')
                sale_country_raw = sale_country_raw.replace('/', ',')
                sale_country_raw = sale_country_raw.replace('\\', ',')
                sale_country_raw = sale_country_raw.replace('+', ',')
                sale_country = sale_country_raw.split(',')
                sale_country = [x.strip() for x in sale_country]
                print(sale_country)
                for country_ in sale_country:
                    if re.search('归档', country_, flags=re.IGNORECASE) is not None:
                        country.append(country_)
                        if version not in dict_version_country:
                            dict_version_country[version] = [model, SKU, n_version, country]
                    for ct in demand_country:
                        if re.search(ct, country_, flags=re.IGNORECASE) is not None:
                            country.append(ct)
                            if version not in dict_version_country:
                                dict_version_country[version] = [model, SKU, n_version, country]
                break
    imapObj.logout()
    return dict_version_country


# 定义新机型软件插入函数
def sw_insert(args_):
    # 新软件MySQL插入语句
    sql_insert = "insert into sw_checklist values(%s,%s,%s,%s,'Add','True',%s);"
    # 执行SQL插入语句
    cursor.execute(sql_insert, args_)


# 定义清remark状态函数
def reset_remark():
    sql_reset = "UPDATE sw_checklist set Remark=''"
    cursor.execute(sql_reset)


# 定义查询当前机型在库中的国家列表函数
def get_country_model(model_):
    sql_country_model = "select country from sw_checklist where model=%s"
    cursor.execute(sql_country_model, (model_,))
    country_model_2d = cursor.fetchall()
    country_model = []
    for i in range(len(country_model_2d)):
        country_model.append(country_model_2d[i][0])
    return country_model


config = {
    'host': "10.240.137.31",  # 本地的话就是这个
    'user': "Dream",  # 输入你的数据库账号
    'password': "Dream123$",  # 以及数据库密码
    'db': "raw_data",  # 数据库名（database名）
    'charset': 'utf8mb4'  # 读取中文不想乱码的话，记得设置这个
}
# 打开数据库连接
db = pymysql.connect(**config)  # 使用关键字参数特性，这样好看一些
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 清空remark状态
reset_remark()
# 查询库中已有机型
sql_model = "select distinct model from sw_checklist"
cursor.execute(sql_model)
model_2d = cursor.fetchall()
model = []
for i in range(len(model_2d)):
    model.append(model_2d[i][0])

demand_country = ['Cambodia', 'Indonesia', 'Iran', 'Jordan', 'Lebanon', 'Malaysia', 'Morocco',
                  'Myanmar',
                  'Philippines', 'Saudi Arabia', 'Singapore', 'South Africa', 'Sri Lanka', 'Thailand',
                  'UAE',
                  'Ukraine', 'Vietnam', 'Colombia', 'Tunisia', 'Mexico', 'Russia']
keys_insert = []
# 新机型软件插入到数据库
dict_version_country = get_dict_version_country()
for version in dict_version_country.keys():
    value = dict_version_country[version]
    for country in value[3]:
        if country in demand_country:
            if value[0] not in model:
                args = (value[0], value[1], value[2], version, country)
                sw_insert(args)
                keys_insert.append(version)

            elif country not in get_country_model(value[0]):
                args = (value[0], value[1], value[2], version, country)
                sw_insert(args)
                keys_insert.append(version)
keys_insert_unique = []
[keys_insert_unique.append(k) for k in keys_insert if k not in keys_insert_unique]
for key in keys_insert_unique:
    dict_version_country.pop(key)
version_remain = {}
for version in dict_version_country.keys():
    value = dict_version_country[version]
    version_remain[version] = [value[2], value[3]]
pprint.pprint(version_remain)

"""sql2 = "select * from sw_checklist where remark='Add'"
cursor.execute(sql2)
print(cursor.fetchall())"""
# 提交更改（非查询需要提交更改才行）
db.commit()
# 断开连接
db.close()
