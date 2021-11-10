#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# @File    : test_case1.py
# @Time    : 2021/08/01 14:44:32
# @Author  : 张佳 
# @Version : 1.0
# @Contact : zhangjia@tianyancha.com


import sys
# sys.path.append("../common")
import unittest

import json
import requests

class TestCase(unittest.TestCase):
    """新增行政许可相关接口"""

    def setUp(self):
        self.testEnv = 'http://10.39.222.108:20064'
        self.headers = {"Authorization": "f37ed796-41c7-45d3-b7fc-b841662fd7d1"}
        
    def test_888_行政许可_工商局(self):
        """
        可以通过公司名称或ID获取企业行政许可信息，企业行政许可信息包括行政许可决定文书号、许可文件名称、许可机关等字段的详细信息\n
        行政许可-工商局\n
        请求方式：GET\n
        返回格式：JSON
        改动：新增返回字段[信用等级] --> result['baseInfo']['creditRating']
        """
        
        keyworlds = "深圳市中亚医药有限公司"
        url = self.testEnv  + "/services/open/m/getLicense/2.0?pageSize=20&keyword=" + keyworlds
        res = requests.get(url=url,headers=self.headers)
        print(res)


    def test_889_行政许可_其他来源(self):
        """
        可以通过公司名称或ID获取企业行政许可信息，企业行政许可信息包括行政许可决定文书号、许可内容、许可机关、审核类型等字段的详细信息\n
        行政许可-其他来源\n
        请求方式：GET\n
        返回格式：JSON
        改动：新增返回字段[信用等级] --> result['baseInfo']['creditRating']
        """
        
        keyworlds = "深圳市中亚医药有限公司"
        url = self.testEnv  + "/services/open/m/getLicenseCreditchina/2.0?pageSize=20&keyword=" + keyworlds
        res = requests.get(url=url,headers=self.headers)
        print(res)

    def test_867_历史行政许可_工商局(self):
        """
        可以通过公司名称或ID获取企业历史的行政许可信息\n
        历史行政许可信息包括行政许可决定文书号\n
        许可文件名称\n
        许可机关等\n
        字段信息\n
        """
        keyworlds = "锦州市中远旅行社有限责任公司"
        url = self.testEnv  + "/services/open/hi/license/2.0?&keyword=" + keyworlds 
        res = requests.get(url=url,headers=self.headers)
        print(res)


    def test_869_历史行政许可_其他来源(self):
        """
        可以通过公司名称或ID获取企业历史的行政许可信息\n
        历史行政许可信息包括行政许可决定文书号\n
        许可文件名称\n
        许可机关等\n
        字段信息\n
        """
        keyworlds = "北京百度网讯科技有限公司"
        url = self.testEnv  + "/services/open/hi/license/creditChina/2.0?keyword="+ keyworlds
        res = requests.get(url=url,headers=self.headers)
        print(res)