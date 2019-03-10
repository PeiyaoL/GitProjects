import requests
import unittest
from commen.readXrld import Read_Ex
import json

class TestLogin(unittest.TestCase):
    """测试获得当前登录的用户信息"""
    def setUp(self):
        self.url = "https://ai-api.sensoro.com/app/account/login"
        r = Read_Ex()
        # 指定sheet名字
        self.data = r.read_excel("lipy")
        # json字符串为双引号
        # print(type())


    def test_login_true_a(self):
        """所有参数正确"""
        # 将json转换成dic,json字符串使用双引号
        data = json.loads(self.data[0]["请求参数"])
        response = json.loads(self.data[0]["响应结果"])
        res = requests.post(self.url,data = data)
        self.result = res.json()

        # 断言，python中没有null，使用None
        self.assertEqual(self.result["errcode"],response["errcode"])
        self.assertEqual(self.result["errmsg"],response["errmsg"])

    # def test_login_false_b(self):
    #     """密码为空"""
    #     print(self.data[1]["请求参数"])
    #     res = requests.post(self.url,data = self.data[1]["请求参数"])
    #     self.result = res.json()

    def tearDown(self):
        print(self.result)

if __name__ == "__main__":
    unittest.main()