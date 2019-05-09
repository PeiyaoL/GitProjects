"""runtest.py文件作用于整个测试项目，生成项目集成测试报告"""

import unittest,time
from commen import HTMLTestRunner

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os


"""生成测试报告"""
def report(test_dir,reslut_dir):
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="*.py")
    # print(discover)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    result = reslut_dir + now + "result.html"
    fp = open(result, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="SENSORO API Report",
                                           description="")
    runner.run(discover)
    fp.close()

"""发送带📎邮件"""
def send_email(sender,receiver,subject,text,attachment):

    # 发送邮箱服务器地址(设置->客户端pop/imap/smtp,状态为开启）
    smtpserver = 'smtp.sina.com'
    # 发送邮箱密码
    password = 'lipy12.8'

    # 创建一个带附件的实例
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    # 邮件主题
    msg['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    # msg.attach(MIMEText('<html><h1>Hello world！</h1></html>', 'html', 'utf-8'))
    msg.attach(MIMEText(text, 'plain', 'utf-8'))

    # 构造附件，传送当前目录下的 1.html 文件，如果发送txt附件，手动修改'html'为'base64'
    att = MIMEText(open(attachment, 'rb').read(),'html', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att["Content-Disposition"] = 'attachment; filename="API TestReport.html"'
    msg.attach(att)

    # 连接发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")



"""
输入目录路径，输出最新文件完整路径
"""
def find_new_file(dir):
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + fn) if not os.path.isdir(dir + fn) else 0)
    print('最新的文件为： ' + file_lists[-1])
    file = os.path.join(dir, file_lists[-1])
    print('完整路径：', file)
    return file




if __name__ == "__main__":

    """
    Jenkins读取test_dir下的case和生成测试报告需要绝对路径；
    """
    # test_dir = "./cases"
    test_dir = "/Users/sensoro/PycharmProjects/AI/cases"

    # 指定测试报告生成路径(./results)
    # result_dir = "./results/"
    result_dir = "/Users/sensoro/PycharmProjects/AI/results/"
    report(test_dir,result_dir)


    # 发送邮箱
    sender = 'lipy_py@sina.com'
    # 接收邮箱
    receiver = 'lipy_pz@sina.com'
    subject = "测试报告"
    text = "API测试报告，请查收!"
    attachment = find_new_file(dir = result_dir)
    send_email(sender,receiver,subject,text,attachment)










