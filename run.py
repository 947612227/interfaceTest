#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# @File    : run.py
# @Time    : 2021/08/01 10:53:43
# @Author  : 张佳 
# @Version : 1.0
# @Contact : zhangjia@tianyancha.com


import unittest
import HTMLTestRunner_CN
import os

basePase = os.getcwd()
# print(basePase)
def createTests():
    suite = unittest.TestSuite()
    testpath = basePase + "/testcase/ShangJi"
    # print(testpath)
    testdir = unittest.defaultTestLoader.discover(
        testpath, pattern='test_*.py')
    for TestSuite in testdir:
        for testcase in TestSuite:
            suite.addTest(testcase)
    return suite



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # 定义报告存放的路径，支持相对路径
    file_path = basePase+"/report/report.html"
    file_result = open(file_path, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner_CN.HTMLTestRunner(
        stream=file_result, title="测试报告", tester="张佳",description="接口测试报告",verbosity=2)#,retry=1)
    #runner = unittest.TextTestRunner(verbosity=2)  #输出到控制台
    runner.run(createTests())
    file_result.close()
