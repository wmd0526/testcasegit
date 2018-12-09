import unittest
import time
import requests
class logintest(unittest.TestCase):
    def setUp(self):
        pass
    def testUserlogin(self):
        # 正确登录，拿到token
        url = "http://47.92.88.246:8087/x_springboot/sys/login"
        data = {"username": "test", "password": "test"}
        headers = {'content-type': 'application/json'}
        r = requests.post(url=url,json=data,headers=headers)
        print(r.json())
        token=r.json()["token"]
        print(token)
        # 正确添加管理员
        useraddurl = "http://47.92.88.246:8087/x_springboot/sys/user/save"
        data = {"status": 1, "roleIdList": [], "username": "增加" + str(time.time()), "password": "test",
                "email": "test@test.com"}
        headers = {"token":token }
        r = requests.post(url=useraddurl, json=data, headers=headers)
        print(r.json())
        # print(r.json()["msg"])
        # self.assertEqual(r.json()["msg"],"success",msg="增加不成功")
        # 查询
        userurl = "http://47.92.88.246:8087/x_springboot/sys/user/list"
        data = {"limit":"10","page":"1", "order":"asc"}
        headers = {"token": token}
        r = requests.get(url=userurl,params=data,headers=headers)
        print(r.json())
        userId=r.json()["page"]["list"][0]["userId"]
        print(userId)

        # 删除管理员
        deleteurl = "http://47.92.88.246:8087/x_springboot/sys/role/delete"
        data = [userId]
        r = requests.post(url=deleteurl,json=data,headers=headers)
        print(r.json())

        # def testuseradd(self):
        #      # 正确登录，拿到token
        #     url = "http://47.92.88.246:8087/x_springboot/sys/login"
        #     data = {"username": "test", "password": "test"}
        #     headers = {'content-type': 'application/json'}
        #     r = requests.post(url=url, json=data, headers=headers)
        #     print(r.json())
        #     token = r.json()["token"]
        #     print(token)
        #     # 异常--用户名为空
        #     useraddurl = "http://47.92.88.246:8087/x_springboot/sys/user/save"
        #     data = {"status":1,"roleIdList":[],"username":"", "password": "test",
        #             "email":"test@test.com"}
        #     headers = {"token":token }
        #     r = requests.post(url=useraddurl, json=data, headers=headers)
        #     print(r.json())
            # self.assertEqual(r.json()["msg"],"success",msg="增加不成功")
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main
