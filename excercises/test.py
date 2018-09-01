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


def send_email():
    # 邮件发送和接收人配置
    from_addr = 'mengxiong.zhou@carlcare.com'
    smtp_server = 'smtp.partner.outlook.cn'
    password = 'TRA+2017'  # 这是你邮箱的第三方授权客户端密码，并非你的登录密码
    to_reciver = ['631434724@qq.com', ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    cc_reciver = ['mengxiong.zhou@carlcare.com', ]
    receiver = to_reciver + cc_reciver
    wk = int(getNowYearWeek()[1]) - 2
    content = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>


    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

    <title>HTML Email编写指南</title>


    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

</head>

<body style="margin: 0; padding: 0;">


    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <table align="left" border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
            <tr>
                <td>
                    <p>Hi all,</p><p>更新WK31机型返修率追踪周报，请查阅并重点关注自己负责的部分，质量改善需要您的积极参与！</p>
                </td>
            </tr>


            <tr>

                <td>
                    <p style="margin:10px 0px;padding:10px;background:#F6FBFF;color:#333;border-left:3px solid #3BB0DB;font-size:14px;line-height:26px">To
                        王工(路明) ，向工（红彬），请重点关注X608,X606,X5515,X5514,X604 ramp阶段产品质量，协调安排FAE持续收集fail sample分析，及时escalate上游单位跟进处理，并请share最新进度给售后，以便售后追溯改善效果，形成快速问题闭环。
                    </p>
                </td>

            </tr>


            <tr>

                <td> Row 2 </td>

            </tr>


            <tr>

                <td> Row 3 </td>

            </tr>
        </table>

    </table>

</body>

</html>'''
    subject = 'My_anmar latest version software check list_week' + str(wk)
    msg = MIMEMultipart('related')
    msg['From'] = _format_addr('Carlcare HQ Technical Support <%s>' % from_addr)  # 显示的发件人
    # msg['To'] = _format_addr('管理员 <%s>' % to_addr)                # 单个显示的收件人
    msg['To'] = ','.join(to_reciver)
    msg['Cc'] = ','.join(cc_reciver)
    msg['Subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText(content, 'html', 'utf-8'))
    msg.attach(addimg(r"/mnt/hgfs/Python在路上/PythonI_project/SW checklist images/Myanmar.jpg", "Myanmar"))
    # 构造附件1，传送当前目录下的itel返修率周报压缩包
    path_itel = r"/mnt/hgfs/Transsion/Repair rate report/repair_rate_report/RR Archive/week" + str(
        wk) + ' Itel&Spice repair rate (warranty).7z'
    filename_itel = 'WK' + str(wk) + ' Itel&Spice repair rate (warranty).7z'
    att1 = MIMEText(open(path_itel, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1.add_header('Content-Disposition', 'attachment', filename=filename_itel)
    msg.attach(att1)

    # 构造附件2，传送当前目录下的TECNO返修率周报压缩包
    path_tecno = r"/mnt/hgfs/Transsion/Repair rate report/repair_rate_report/RR Archive/week" + str(
        wk) + ' TECNO repair rate (warranty).7z'
    filename_tecno = 'WK' + str(wk) + ' TECNO repair rate (warranty).7z'
    att2 = MIMEText(open(path_tecno, 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2.add_header('Content-Disposition', 'attachment', filename=filename_tecno)
    msg.attach(att2)
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
    send_email()
