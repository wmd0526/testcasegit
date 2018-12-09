# -*- coding:utf-8 -*-
import unittest
import requests
import time
class userAddTest(unittest.TestCase):
    def setUp(self):
        pass
    def testUserAdd1(self):

        #测试我们的登陆
        url = "http://47.92.88.246:8087/x_springboot/sys/login"
        data = {"username": "niuyuting", "password": "111111"}
        headers = {"Content-Type": "application/json"}
        res = requests.post(url=url, json=data)
        token=res.json()["token"]

        #测试用户添加
        userAddurl="http://47.92.88.246:8087/x_springboot/sys/user/save"
        data={"status":1,"roleIdList":[],"username":"用户"+str(time.time()),"password":"test","email":"test@test.com"}
        headers.update({"token": token})

        print(str(headers)+"-------------------------------")
        res=requests.post(url=userAddurl,json=data,headers=headers)
        print(res.json())
    def testUserAdd2(self):
        #测试我们的登陆
        url = "http://47.92.88.246:8087/x_springboot/sys/login"
        data = {"username": "niuyuting", "password": "111111"}
        headers = {"Content-Type": "application/json"}
        res = requests.post(url=url, json=data)
        token=res.json()["token"]

        #测试异常添加用户
        userAddurl="http://47.92.88.246:8087/x_springboot/sys/user/save"
        data={"status":1,"roleIdList":[],"username":"","password":"test","email":"test@test.com"}
        headers.update({"token": token})

        print(str(headers)+"-------------------------------")
        res=requests.post(url=userAddurl,json=data,headers=headers)
        print(res.json())
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main