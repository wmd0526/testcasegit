import HTMLTestRunner
import unittest
from zuoye import DemoTest

# 二次修改
# 三次修改

# 12345655345234534534
suite=unittest.TestSuite()
suite.addTest(DemoTest("testuseradd"))
print(suite)

file=open('report1123.html','wb')

runner=HTMLTestRunner.HTMLTestRunner(stream=file,title="第一个报告")
runner.run(suite)