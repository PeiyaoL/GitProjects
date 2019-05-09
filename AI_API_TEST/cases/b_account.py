import requests
import unittest
from commen import commen,host
import pprint


class TestAccountMe(unittest.TestCase):
    """测试获得当前登录的用户信息"""
    def setUp(self):
        base_url = host.host["base_url"]
        self.url = base_url + "/app/account/me"
        self.headers = commen.get_headers("peiyao.li@sensoro.com","Lipy1208")

    def test_account_me(self):
        """获取用户信息"""
        r = requests.get(self.url,headers = self.headers)
        self.result = r.json()
        self.assertEqual(self.result["errcode"], 0)
        self.assertEqual(self.result["errmsg"],"success")




    # def test_login_true(self):
    #     """所有参数正确"""
    #     r = self.s.post(self.url,self.data)
    #     self.result = r.json()
    #     # 断言，python中没有null，使用None
    #     self.assertEqual(self.result["errcode"],0)
    #     self.assertEqual(self.result["errmsg"],"success")
    #
    #
    def tearDown(self):
        pprint.pprint(self.result)

if __name__ == "__main__":
    unittest.main()
