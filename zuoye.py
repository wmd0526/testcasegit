import unittest
import time
import requests
class DemoTest(unittest.TestCase):
    def setUp(self):
        # 登录
        loginurl = "http://47.92.88.246:8087/x_springboot/sys/login"
        data = {"username": "test", "password": "test"}
        self.headers = {'content-type': 'application/json'}
        r = requests.post(url=loginurl, json=data, headers=self.headers)
        print(r.json()["token"])
        self.token = r.json()["token"]
        self.headers = {"token": self.token}
    def testuseradd(self):
    #     增加user
        useraddurl="http://47.92.88.246:8087/x_springboot/sys/user/save"
        data={"status":1,"roleIdList":[],"username":"增加"+str(time.time()),"password":"test","email":"test@test.com"}

        r=requests.post(url=useraddurl,json=data,headers=self.headers)
        print(r.json())
        # 查询
        userurl = "http://47.92.88.246:8087/x_springboot/sys/user/list"
        data = { "limit":"10","page":"1","order":"asc"}
        headers = {"token": self.token}
        r = requests.get(url=userurl,params=data,headers=headers)
        print(r.json())
        self.userId=r.json()["page"]["list"][0]["userId"]
        # print(userId)
    #     删除
    #     usedeleterurl = "http://47.92.88.246:8087/x_springboot/sys/user/delete"
    #     data = [userId]
    #     headers = {"token": token}
    #     r = requests.post(url=usedeleterurl, json=data, headers=headers)
    #     print(r.json())
    #     查询
    #     userurl = "http://47.92.88.246:8087/x_springboot/sys/user/list"
    #     data = {"limit": "10", "page": "1", "order": "asc"}
    #     headers = {"token": token}
    #     r = requests.get(url=userurl, params=data, headers=headers)
    #     print(r.json())
    #     userId = r.json()["page"]["list"][0]["userId"]
    #     print(userId)

    def tearDown(self):
        #     删除
        print(str(self.headers)+"--------")
        usedeleterurl = "http://47.92.88.246:8087/x_springboot/sys/user/delete"
        data = [self.userId]
        # headers = {"token": token}
        r = requests.post(url=usedeleterurl, json=data, headers=self.headers)
        print("打印删除的数据")
        print(r.json())
        #     查询
        # userurl = "http://47.92.88.246:8087/x_springboot/sys/user/list"
        # data = {"limit": "10", "page": "1", "order": "asc"}
        # headers = {"token": self.token}
        # r = requests.get(url=userurl, params=data, headers=headers)
        # print(r.json())
        # userId = r.json()["page"]["list"][0]["userId"]
        # print(userId)


if __name__ == '__main__':
    unittest.main
