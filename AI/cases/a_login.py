import requests
import unittest


class TestLogin(unittest.TestCase):
    """测试用户登录"""
    def setUp(self):
        self.url = "https://ai-api.sensoro.com/app/account/login"
        self.data = {"account":"peiyao.li@sensoro.com","password":"Lipy1208"}
    def test_login_true(self):
        """所有参数正确"""
        r = requests.post(self.url,data = self.data)
        self.result = r.json()
        # 断言，python中没有null，使用None
        self.assertEqual(self.result["errcode"],0)
        self.assertEqual(self.result["errmsg"],"success")
        #将ssid写入文件
        with open('/Users/sensoro/PycharmProjects/AI/cases/ssid.txt', 'w') as f:
            f.write(self.result["data"]["ssid"])

    def test_login_false(self):
        """请求方式错误"""
        r = requests.get(self.url, data=self.data)
        self.result = r.json()
        # 断言，python中没有null，使用None
        self.assertEqual(self.result["errcode"], 100003)
        self.assertEqual(self.result["errmsg"], "Request method error")

    def tearDown(self):
        print(self.result)

if __name__ == "__main__":
    unittest.main()
