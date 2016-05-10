# -*- coding: utf-8 -*-
import commands
import smtplib

from email.mime.text import MIMEText

mailto_list = ["fenghuibin@ismartv.cn"]
mail_host = "smtp.qiye.163.com"  # 设置服务器
mail_user = "fenghuibin@ismartv.cn"  # 用户名
mail_pass = "Hope0Dies"  # 口令


def send_mail(to_list, sub, content):  # to_list：收件人；sub：主题；content：邮件内容
    me = "hello" + "<" + mail_user + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content, _charset='utf8')  # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


def get_current_branch():
    branch_list = commands.getoutput("git branch")
    branch_list = branch_list.split("\n")
    for branch in branch_list:
        if branch.__contains__("*"):
            return branch


if __name__ == '__main__':
    gitLog = commands.getoutput("git log --pretty=format:'%h  ====>  %s'  python ^origin/python")
    gitLog += "\r\n\r\n"
    gitLog += "git branch: " + get_current_branch()
    print gitLog

    if send_mail(mailto_list, "hello", gitLog):
        print "发送成功"
    else:
        print "发送失败"
