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


def send_email(filepath_in):
    # 邮件发送和接收人配置
    from_addr = 'mengxiong.zhou@carlcare.com'
    smtp_server = 'smtp.partner.outlook.cn'
    password = 'TRA+2017'  # 这是你邮箱的第三方授权客户端密码，并非你的登录密码
    to_reciver = ['631434724@qq.com', ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    cc_reciver = ['zhoumengxiong@outlook.com', ]
    receiver = to_reciver + cc_reciver
    wk = int(getNowYearWeek()[1]) - 1
    content = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>


    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

    <title>HTML Email编写指南</title>


    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

</head>

<body style="margin: 0; padding: 0;">
    <div style="width:100%;height:100%;background-color: #f9f9f9;">
        <div style="width: 100%;height: 100%;background-color: #ffffff;padding-left: 10px;padding-right: 10px;">
            <div style="color: #13243f;font-family: Microsoft YaHei UI;font-weight: 600;font-size: 14px;letter-spacing: 1px;">
                <p>Hello all：</p>
                <p>更新WK31机型返修率追踪周报，请查阅并重点关注自己负责的部分，质量改善需要您的积极参与！</p>
                <p style="margin:10px 20px 10px 0px;padding:10px;background:#F6FBFF;color:#333;border-left:3px solid #3BB0DB;">To
                    王工(路明) ，向工（红彬），请重点关注X608,X606,X5515,X5514,X604 ramp阶段产品质量，协调安排FAE持续收集fail sample分析，及时escalate上游单位跟进处理，并请share最新进度给售后，以便售后追溯改善效果，形成快速问题闭环。
                </p>
            </div>
        </div>
    </div>
</body>

</html>'''
    subject = 'Myanmar latest version software check list_week' + str(wk)
    msg = MIMEMultipart('related')
    msg['From'] = _format_addr('Carlcare HQ Technical Support <%s>' % from_addr)  # 显示的发件人
    # msg['To'] = _format_addr('管理员 <%s>' % to_addr)                # 单个显示的收件人
    msg['To'] = ','.join(to_reciver)
    msg['Cc'] = ','.join(cc_reciver)
    msg['Subject'] = Header(subject, 'utf-8')
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
        server.sendmail(from_addr, receiver, msg.as_string())
        server.quit()
    except:
        print('Send failed!')


if __name__ == '__main__':
    send_email(r'F:\Transsion\New market\latest version software checklist by country\Myanmar')
