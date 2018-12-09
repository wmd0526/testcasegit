# -*- coding:utf-8 -*-
import unittest
import requests
import time
import HtmlTestRunner
class userAddTest(unittest.TestCase):
    def setUp(self):
        # 测试我们的登陆
        url = "http://47.92.88.246:8087/x_springboot/sys/login"
        data = {"username": "niuyuting", "password": "111111"}
        self.headers = {"Content-Type": "application/json"}
        res = requests.post(url=url, json=data)
        self.token = res.json()["token"]
        # 用户的数据
        self.addUserUrl = "http://47.92.88.246:8087/x_springboot/sys/user/save"
        self.userID=""
    def testUserAdd1(self):
        #测试用户添加
        data={"status":1,"roleIdList":[],"username":"用户"+str(time.time()),"password":"test","email":"test@test.com"}
        self.headers.update({"token": self.token})
        res=requests.post(url=self.addUserUrl,json=data,headers=self.headers)
        print(res.json())
        #查询
        selecturl="http://47.92.88.246:8087/x_springboot/sys/user/list"
        data={"limit":"10","page":"1","order":"asc"}
        res=requests.get(url=selecturl,params=data,headers=self.headers)
        print(res.text)
        self.userID=res.json()["page"]["list"][0]["userId"]
        # print(str(self.userID)+"新增的数据")

    def testUserAdd2(self):
        data={"status":1,"roleIdList":[],"username":"","password":"test","email":"test@test.com"}
        self.headers.update({"token": self.token})
        print(str(self.headers)+"-------------------------------")
        res=requests.post(url=self.addUserUrl,json=data,headers=self.headers)
        print(res.json())


    def tearDown(self):
        # 删除
        deleteUrl = "http://47.92.88.246:8087/x_springboot/sys/user/delete"
        data = [self.userID]
        res = requests.post(url=deleteUrl, json=data, headers=self.headers)


        # 查询
        selecturl = "http://47.92.88.246:8087/x_springboot/sys/user/list"
        data = {"limit": "10", "page": "1", "order": "asc"}
        res = requests.get(url=selecturl, params=data, headers=self.headers)
        #print(res.text)
        userID = res.json()["page"]["list"][0]["userId"]

if __name__ == '__main__':

    pass


