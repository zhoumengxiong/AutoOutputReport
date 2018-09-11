from email.utils import formataddr
from email.utils import getaddresses
from email.header import decode_header

# format addrs
multi = "wenquan.huang(黄文权) <wenquan.huang@carlcare.com>, benpu.xie(谢本朴) <benpu.xie@carlcare.com>, " \
        "wendy.ning(宁建梅) <wendy.ning@carlcare.com>, szwei.du(杜威) <szwei.du@carlcare.com>, krystal.liu(刘沛) " \
        "<krystal.liu@carlcare.com>, ying.feng(冯颖) <ying.feng@carlcare.com>, " \
        "nancy.yan(严兰兰) <nancy.yan@carlcare.com>, tao.yan(严桃) <tao.yan@carlcare.com>, " \
        "qi.xie(谢琪) <qi.xie@carlcare.com>, youli.zhang(张友利) <youli.zhang@carlcare.com>," \
        " mudan.zhou(周牡丹) <mudan.zhou@carlcare.com>, junjun.wan(万军军) <junjun.wan@carlcare.com>," \
        " ping.dang(党萍) <ping.dang@carlcare.com>, fei.zeng(曾飞) <fei.zeng@carlcare.com>," \
        " gary.zhang(张起荣) <gary.zhang@carlcare.com>, xuan.liu(刘玄) <xuan.liu@carlcare.com>," \
        " yizhuan.chen(陈一专) <yizhuan.chen@carlcare.com>, wei.peng(彭薇) <wei.peng@carlcare.com>," \
        " meng.liu(刘萌) <meng.liu@carlcare.com>, xiaoying.gao(高小莹) <xiaoying.gao@carlcare.com>," \
        " yuting.zeng(曾玉婷) <yuting.zeng@carlcare.com>, xiaopei.zhu(朱晓佩) <xiaopei.zhu@carlcare.com>," \
        " qi.tang(唐琪) <qi.tang@carlcare.com>, minmin.zhao(赵敏敏) <minmin.zhao@carlcare.com>," \
        " yan.zhang3(张燕) <yan.zhang3@carlcare.com>, pei.xiong(熊佩) <pei.xiong@carlcare.com>," \
        " mingxiong.hao(郝明雄) <mingxiong.hao@carlcare.com>, bo.wang(汪波) <bo.wang@carlcare.com>," \
        " fuping.zhu(朱福平) <fuping.zhu@carlcare.com>, wei.deng(邓伟) <wei.deng@carlcare.com>," \
        " mengxiong.zhou(周梦雄) <mengxiong.zhou@carlcare.com>, jing.wu(吴靖) <jing.wu@carlcare.com>," \
        " liang.xu(许亮) <liang.xu@carlcare.com>, yinling.chen(陈银玲) <yinling.chen@carlcare.com>," \
        " kun.yuan(袁锟) <kun.yuan@carlcare.com>, jian.xiong(熊建) <jian.xiong@carlcare.com>," \
        " li.liu(刘礼) <li.liu@carlcare.com>, carol.chen(陈圆圆) <carol.chen@carlcare.com>," \
        " lei.gao(高磊) <lei.gao@carlcare.com>, anming.li(李安明) <anming.li@carlcare.com>," \
        " keira.peng(彭丽) <keira.peng@carlcare.com>, yanan.wang(王亚楠) <yanan.wang@carlcare.com>," \
        " xiaoxian.xie(谢晓娴) <xiaoxian.xie@carlcare.com>, fan.liu(刘凡) <fan.liu@carlcare.com>," \
        " barry.gao(高建旺) <barry.gao@carlcare.com>, tao.zheng(郑韬) <tao.zheng@carlcare.com>," \
        " huiyu.tang(唐慧钰) <huiyu.tang@carlcare.com>, zhifen.liu(刘志奋) <zhifen.liu@carlcare.com>," \
        " yang.jin(金阳) <yang.jin@carlcare.com>, liping.yang(杨利平) <liping.yang@carlcare.com>," \
        " chuangjin.li(李床金) <chuangjin.li@carlcare.com>, qizhi.li(李启知) <qizhi.li@carlcare.com>," \
        " shanshan.meng(蒙珊珊) <shanshan.meng@carlcare.com>, jessica.chen(陈洁) <jessica.chen@carlcare.com>," \
        " king.lei(雷富金) <king.lei@carlcare.com>, jingyan.zhang(张景岩) <jingyan.zhang@carlcare.com>," \
        " wei.liu(刘伟) <wei.liu@carlcare.com>"
pairs = getaddresses([multi])
pairs = [formataddr(pair) for pair in pairs]
recipients = ', '.join(pairs)
print(recipients)

# decoding and format addrs
rawtoheader = "=?utf-8?b?d2VucXVhbi5odWFuZyAo6buE5paH5p2DKQ==?= <wenquan.huang@carlcare.com>," \
              " =?utf-8?b?YmVucHUueGllICjosKLmnKzmnLQp?= <benpu.xie@carlcare.com>," \
              " =?utf-8?b?d2VuZHkubmluZyAo5a6B5bu65qKFKQ==?=" \
              " <wendy.ning@carlcare.com>, =?utf-8?b?c3p3ZWkuZHUgKOadnOWogSk=?=" \
              " <szwei.du@carlcare.com>, =?utf-8?b?a3J5c3RhbC5saXUgKOWImOaymyk=?=" \
              " <krystal.liu@carlcare.com>, =?utf-8?b?eWluZy5mZW5nICjlhq/popYp?=" \
              " <ying.feng@carlcare.com>, =?utf-8?b?bmFuY3kueWFuICjkuKXlhbDlhbAp?=" \
              " <nancy.yan@carlcare.com>, =?utf-8?b?dGFvLnlhbiAo5Lil5qGDKQ==?= <tao.yan@carlcare.com>"
pairs = getaddresses([rawtoheader])
addrs = []
for name, addr in pairs:
    abytes, aenc = decode_header(name)[0]  # email+MIME
    name = abytes.decode(aenc)  # Unicode
    addrs.append(formataddr((name, addr)))  # one or more addrs
recipients = ', '.join(addrs)
print(recipients)
