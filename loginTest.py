# -*- coding:utf-8 -*-
#1.导入unittest
#2.定义一个类继承unittest.TestCase
#3.setUp ，tearDown 重写
#4.写我们的测试用例
#5. 每一个测试用例都要加一个断言
import unittest
import requests
import json
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://47.92.88.246:8087/x_springboot/sys/login"
    #正常登陆
    def testLogin01(self):
        url = "http://47.92.88.246:8087/x_springboot/sys/login"
        data={"username":"niuyuting","password":"111111"}
        headers = {"Content-Type": "application/json"}
        res = requests.post(url=self.url, json=data)
        print(res.json()["msg"])
        # first  实际结果  second 预期结果
        self.assertEqual(res.json()["msg"],"success1",msg="登陆不通过")

    def testLogin02(self):
        data = {"username": "niuyuting", "password": ""}
        headers = {"Content-Type": "application/json"}
        res = requests.post(url=self.url, json=data)
        print(res.json())
        self.assertEqual(res.json()["msg"],"账号或密码不正确",msg="登陆异常")
    def tearDown(self):
        pass

if __name__ == '__main__':
    a=LoginTest()
    a.testLogin01()
    # unittest.main()