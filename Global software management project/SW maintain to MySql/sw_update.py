# -*- coding: utf-8 -*-
import pymysql

version_update = {'A15-VP510AC-8.1.0-OP-V009-20180714': ['N4', ['Morocco',
                                                                'Sri Lanka']],
                  'A31-I803-7.0-OP-V036-20180713': ['N12', ['UAE', 'Morocco']],
                  'A32F-F8007-8.1-OP-V041-20180801': ['N4', ['Philippines', 'Ukraine'  # philippines, Ukraine ADD
                                                             ]],
                  'A44-F3706RU-7.0-RU-V007-20180706': ['N7', ['Russia']],
                  'A44Pro-F3706-7.0-OP-V024-20180719': ['N5', ['Cambodia']],
                  'CA7-H633BCDK-O-RU-180723V200': ['N13', ['Russia']],
                  'CA8-H633EFG-O-180717V193': ['N12', ['UAE']],
                  'CA8-H633EFG-O-V2-180718V187': ['N14',
                                                  ['Thailand', 'Iran', 'Myanmar', 'Ukraine']],
                  'CX-H501C-N-180713V89': ['N27', ['Colombia']],
                  'F2LTE-H394ABC-Go-180727V148': ['N5', ['Morocco', 'Saudi Arabia', 'Iran']],
                  'F3-H8022ACDE-N-13M-180718V76': ['N14',
                                                   ['Morocco',
                                                    'Vietnam',
                                                    'Thailand',
                                                    'Myanmar',
                                                    'Cambodia']],
                  'IN3-H3721D-N-180717V34': ['N10', ['Sri Lanka']],
                  'KA7-H8024A-GO-180731V152': ['N7',
                                               ['Myanmar',
                                                'Saudi Arabia',
                                                'Colombia',
                                                'Cambodia']],
                  'LA6-H8021AC-N-180725V123': ['N7', ['Saudi Arabia']],
                  'LA7-H393A-O-RU-180711V61': ['N7', ['Russia']],
                  'P32-F8011-8.1-OP-V033-20180719': ['N3', ['Morocco']],
                  'S13-F8012-8.1-OP-V009-20180713': ['N1', ['Morocco']],
                  'S42-QL1667-8.0-OP-V028-20180716': ['N4', ['Vietnam', 'Cambodia']  # ADD
                                                      ],
                  'W2-AW600C-M-ZA-180718V15': ['', ['South Africa']],
                  'X5514-H395AD-O-180718V175': ['N3',
                                                ['Morocco',
                                                 'Thailand',
                                                 'Saudi Arabia',
                                                 'UAE',
                                                 'Tunisia']],
                  'X5515F-H398F-O-180725V143': ['N7', ['Indonesia']],
                  'X573-QL1668DEF-O-180723V37': ['N30',
                                                 ['Vietnam',
                                                  'Philippines',
                                                  'Morocco',
                                                  'Colombia',
                                                  'Thailand',
                                                  'Iran',
                                                  'Tunisia']],
                  'X608-QL1661ABCDEF-O-180720V19': ['N6',
                                                    ['Morocco',
                                                     'Vietnam',
                                                     'Thailand',
                                                     'Philippines',
                                                     'Indonesia',
                                                     'Saudi Arabia',
                                                     'Colombia',
                                                     'Tunisia']],
                  'it2160-DL194-EnFrPo-ZA-PEP-20180724': ['N17', ['South Africa']],
                  'it2160-DL194-EnFrSwHaPoAr-AF-20180712': ['N18', ['Morocco']],
                  'it2180-G185A-RuEn-RU-20180720': ['N55', ['Russia']],
                  'it2190-G1808A-EnFrSwHaPoAr-20180719': ['N2', ['UAE']],  # ADD
                  'it5250-G2406B-EnFrPoArSwHa-20180731': ['N14', ['Morocco', 'UAE']  # Morocco ADD
                                                          ]}
version = 'it2190-G1808A-EnFrSwHaPoAr-20180719'
legal = 'True'
n_version = version_update[version][0]
like_pattern = '-'.join(version.split('-')[:3]) + '%'
args = (n_version, version, legal, like_pattern)
config = {
    'host': "192.168.1.102",  # 本地的话就是这个
    'user': "Dream",  # 输入你的数据库账号
    'password': "Dream123$",  # 以及数据库密码
    'db': "raw_data",  # 数据库名（database名）
    'charset': 'utf8mb4'  # 读取中文不想乱码的话，记得设置这个
}
# 打开数据库连接
db = pymysql.connect(**config)  # 使用关键字参数特性，这样好看一些
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 老软件MySQL更新语句
sql1 = """update sw_checklist set `N version`=%s,`Software Version`=%s,remark='Update',
Legal=%s where `Software version` like %s"""
cursor.execute(sql1, args)
"""sql2 = "select * from sw_checklist where remark='Update'"
cursor.execute(sql2)
print(cursor.fetchall())"""
# 提交更改（非查询需要提交更改才行）
db.commit()
# 断开链接
db.close()
