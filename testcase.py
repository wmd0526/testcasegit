# -*- coding:utf-8 -*-
import unittest
class DeamTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(self):
    #     print("setUpClass")
    def setUp(self):
        #我们案例的初始条件：如 我们登陆  等等
        #没执行一个测试用例 都会执行
        print("setup"+"1")
    def test01(self):
        #这里边使我们真实的测试用例  必须test开头
        print("test01" + "1-1")
    def test02(self):
        #这里边使我们真实的测试用例  必须test开头
        print("test02" + "1-2")
    def tearDown(self):
        #放置的是我们案例结束要处理的事情，比如删除数据啊
        #每执行完测试用例都会执行
        print("tearDown" + "3")

    # @classmethod
    # def tearDownClass(self):
    #     print("tearDownClass")

if __name__ == '__main__':

    unittest.main()