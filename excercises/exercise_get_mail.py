# -*- coding: utf-8 -*-
import imapclient
import pprint
import pyzmail

imapObj = imapclient.IMAPClient(
    host='partner.outlook.cn', port=993, use_uid=True)
imapObj.login('mengxiong.zhou@carlcare.com', 'TRA+2017')
pprint.pprint(imapObj.list_folders())
select_info = imapObj.select_folder('INBOX', readonly=False)
print('%d messages in INBOX' % select_info[b'EXISTS'])
uids1 = imapObj.search(['From', 'mengxiong.zhou@carlcare.com'])
uids2 = imapObj.search(['On', '14-Aug-2018'])
uids = list(set(uids1) & set(uids2))
print(uids)
message_html = ''
for msgid in uids:
    msgdict = imapObj.fetch([msgid, ], [b'BODY[]'])
    body = msgdict[msgid][b'BODY[]']
    message = pyzmail.PyzMessage.factory(body)
    subject = message.get_subject()
    from_ = message.get_addresses('from')
    to = message.get_addresses('to')
    cc = message.get_addresses('cc')
    bcc = message.get_addresses('bcc')
    if message.text_part != None:
        message_text = message.text_part.get_payload().decode(message.text_part.charset)
        print(message_text)
    elif message.html_part != None:
        message_html = message.html_part.get_payload().decode(message.html_part.charset)
        print(message_html)
    print(subject)
    message_html = message_html.replace('gb2312', 'utf-8')
    file = open('Repair_rate.html', 'w', encoding='utf-8')
    file.write(message_html)
    file.close()
imapObj.logout()
