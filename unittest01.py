import unittest
import requests
import time
class demotest(unittest.TestCase):
    def setUp(self):
       # self.url = "http://47.92.88.246:8087/x_springboot/sys/login"
       # self.headers = {'content-type': 'application/json'}
        pass
    def testlogin01(self):
        url = "http://47.92.88.246:8087/x_springboot/sys/login"
        data = {"username": "test", "password": "test"}
        headers = {'content-type': 'application/json'}
        r = requests.post(url=url,json=data)
        # print(r.json()["msg"])
        token=r.json()["token"]
        # self.assertEqual(r.json()["msg"],"success1",msg="登录不通过")
    # def testlogin02(self):
    #     url = "http://47.92.88.246:8087/x_springboot/sys/login"
    #     data = {"username": "test", "password": ""}
    #     headers = {'content-type': 'application/json'}
    #     r = requests.post(url=url, json=data, headers=headers)
    #     print(r.json())
    # def testlogin03(self):
    #     url = "http://47.92.88.246:8087/x_springboot/sys/login"
    #     data = {"username": "test", "password": "qqqqqqq"}
    #     headers = {'content-type': 'application/json'}
    #     r = requests.post(url=url, json=data, headers=headers)
    #     print(r.json())
    def testuseradd01(self):
        url = "http://47.92.88.246:8087/x_springboot/sys/user/save"
        data = {"status":1,"roleIdList":[],"username":"增加"+str(time.time()),"password":"test","email":"test@test.com"}
        headers = {"token":token}
        r = requests.post(url=url, json=data, headers=headers)
        print(r.json())
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()