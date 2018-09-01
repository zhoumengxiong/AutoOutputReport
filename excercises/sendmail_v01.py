# -*- coding: utf-8 -*-
import os
import smtplib
import datetime
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage


def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage


def getNowYearWeek():
    # 当前时间年第几周的计算
    timenow = datetime.datetime.now()
    NowYearWeek = timenow.isocalendar()
    return NowYearWeek


# 中文处理
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(to_addr_in, filepath_in):
    # 邮件发送和接收人配置
    from_addr = 'mengxiong.zhou@carlcare.com'
    smtp_server = 'smtp.partner.outlook.cn'
    password = 'TRA+2017'  # 这是你邮箱的第三方授权客户端密码，并非你的登录密码
    to_addr = to_addr_in
    to_addrs = to_addr.split(',')
    wk = int(getNowYearWeek()[1]) - 1
    content = '''<body style="font-family:segoe ui;color:RosyBrown;font-size:20px;"><p>Hi all,</p>
    <p>Update latest version <a href="#123">software</a> check list FYR.</p>
    <hr />
    <p><b><i>Newly added or updated items are marked with red.</i></b></font><br /><a href="https://www.taobao.com"><img src="cid:Myanmar"></a>
    <br /><strong><a id="123">If any question, pls let me know!</a><strong></p></body>
    '''
    subject = 'Myanmar latest version software check list_week' + str(wk)

    msg = MIMEMultipart('related')
    msg['From'] = _format_addr('Carlcare HQ Technical Support <%s>' % from_addr)  # 显示的发件人
    # msg['To'] = _format_addr('管理员 <%s>' % to_addr)                # 单个显示的收件人
    msg['To'] = ",".join(to_addrs)  # 多个
    msg['Subject'] = Header(subject, 'utf-8').encode()  # 显示的邮件标题

    # 需要传入的路径
    # filepath = r'F:\Transsion\New market\latest version software checklist by country'
    filepath = filepath_in
    r = os.path.exists(filepath)
    if r is False:
        msg.attach(MIMEText('no file...', 'plain', 'utf-8'))
    else:
        # 邮件正文是MIMEText:
        msg.attach(MIMEText(content, 'html', 'utf-8'))
        msg.attach(addimg(r"F:\Python在路上\PythonI_project\Myanmar.jpg", "Myanmar"))

        # 遍历指定目录，显示目录下的所有文件名
        pathdir = os.listdir(filepath)
        for alldir in pathdir:
            child = os.path.join(filepath, alldir)
            # print(child.decode('gbk'))  # .decode('gbk')是解决中文显示乱码问题

            # 添加附件就是加上一个MIMEBase，从本地读取一个文件
            with open(child, 'rb') as f:
                # 设置附件的MIME和文件名，这里是txt类型:
                mime = MIMEBase('file', 'xls', filename=alldir)
                # 加上必要的头信息:
                mime.add_header('Content-Disposition', 'attachment', filename=alldir)
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                # 把附件的内容读进来:
                mime.set_payload(f.read())
                # 用Base64编码:
                encoders.encode_base64(mime)
                # 添加到MIMEMultipart:
                msg.attach(mime)
    try:
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        server.set_debuglevel(1)  # 用于显示邮件发送的执行步骤
        server.login(from_addr, password)
        # print to_addrs
        server.sendmail(from_addr, to_addrs, msg.as_string())
        server.quit()
    except:
        print('Send failed!')


if __name__ == '__main__':
    send_email('631434724@qq.com', r'F:\Transsion\New market\latest version software checklist by country\Myanmar')
