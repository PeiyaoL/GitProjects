import requests
# 屏蔽warning信息
# requests.packages.urllib3.disable_warnings()

# 获得get_ssid
def get_headers(user,passwd):
    url = "https://ai-api-mocha.sensoro.com/app/account/login"
    data = {"account":user,"password":passwd}
    r = requests.post(url=url,json=data)
    result = r.json()
    ssid = result["data"]["ssid"]
    headers = {'x-session-id': ssid}
    return headers



import zmail
import pprint
from requests_html import HTML
from bs4 import BeautifulSoup
import time


def get_pin(username,passwd):
    # 接收邮件
    server = zmail.server(username, passwd)
    mail = server.get_latest()
    # mail["content_html"]返回由字符串组成的列表
    mail_str = mail["Content_html"][0]
    # 将str转换成html
    mail_html = HTML(html=mail_str)
    pin_ele = mail_html.find("span[style='font-size: 20px; color: #006ef2;']")
    # pin_ele = mail_html.xpath("//span[@style='font-size: 20px; color: #006ef2;']")
    # print(type(pin_ele[0]))
    return pin_ele[0].text

    # 解析html邮件，获取邮件中的验证码
    # soup = BeautifulSoup(mail['Content_html'][0])
    # tag=soup.find_all(style="font-size: 20px; color: #006ef2;")
    # print(tag[0].text)


#
# if __name__ == "__main__":
#
#     print(get_pin("lipy_py@sina.com", "lipy12.8"))
#
#
#     ssid = get_ssid("peiyao.li@sensoro.com","Lipy1208")
#     print(ssid)









