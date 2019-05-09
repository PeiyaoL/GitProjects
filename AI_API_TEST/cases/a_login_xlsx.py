import requests
import unittest
from commen.readXrld import Read_Ex
from commen.host import host
import json
from ddt import ddt,data
import pprint

# 数据驱动

filename = "/Users/sensoro/PycharmProjects/AI/data/data.xlsx"
r = Read_Ex()
testdata = r.read_excel(filename,"login")

@ddt
class TestLogin(unittest.TestCase):
    """测试登录"""
    def setUp(self):
        base_url = host["base_url"]
        self.url = base_url+"/app/account/login"
        # print(self.url)


    # 解析数据
    @data(*testdata)
    def test_login(self,data):
        self.description = (data["case"])
        self.param = json.loads(data["请求参数"])
        response = json.loads(data["响应结果"])
        r = requests.post(self.url, json=self.param)
        self.result = r.json()
        self.assertEqual(self.result["errcode"], response["errcode"])



    def tearDown(self):
        pprint.pprint(self.description)
        pprint.pprint(self.result)
        print()
        pass

if __name__ == "__main__":
    unittest.main()

