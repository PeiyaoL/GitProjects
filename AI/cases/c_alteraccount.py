import requests
import unittest

class TestAccountMe(unittest.TestCase):
    """测试获得当前登录的用户信息"""
    def setUp(self):
        self.url = "https://ai-api.sensoro.com/app/account/alteraccount"
        # 读取ssid.txt中的ssid
        with open('/Users/sensoro/PycharmProjects/AI/cases/ssid.txt', 'r') as f:
            self.ssid = f.read()
            print(self.ssid)
        self.s = requests.Session()
        headers = {"x-session-id":self.ssid}
        self.s.headers = headers
        self.data = {"newEmail":"peiyao.li@sensoro.com","password":"Lipy1208"}

    def test_login_true(self):
        """所有参数正确"""
        r = self.s.post(self.url,self.data)
        self.result = r.json()
        # 断言，python中没有null，使用None
        self.assertEqual(self.result["errcode"],0)
        self.assertEqual(self.result["errmsg"],"success")

    def tearDown(self):
        print(self.result)
        # 关闭Session会话
        self.s.close()

if __name__ == "__main__":
    unittest.main()
