# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import userTest02
if __name__ == '__main__':
    # 创建一个测试套件
    suite = unittest.TestSuite()
    # 将测试用例加载到测试套件中
    suite.addTest(userTest02.userAddTest('testUserAdd1'))
    #suite.addTest(userTest02.userAddTest('testUserAdd2'))
    #定义一个TextTestRunner
    # runner = unittest.TextTestRunner()
    # #运行测试用例
    # runner.run(suite)

    # 定义一个文件
    path = "report.html"
    fp = open(path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="testCase")
    runner.run(suite)