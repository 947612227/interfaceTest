#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# @File    : test_进出口信用增加信用等级字段.py
# @Time    : 2021/08/23 10:02:53
# @Author  : 张佳 
# @Version : 1.0
# @Contact : zhangjia@tianyancha.com


import sys
# sys.path.append("../common")
import unittest

import json
import requests

class TestCase(unittest.TestCase):
    """接口881，进出口信用接口增加「信用等级」字段"""

    def setUp(self):
        self.testEnv = 'http://10.39.222.108:20064'
        self.headers = {"Authorization": "f37ed796-41c7-45d3-b7fc-b841662fd7d1"}

        
    def test_881_进出口信用(self):
        """
        test881
        进出口信用\n
        请求方式：GET\n
        返回格式：JSON
        改动：新增返回字段[信用等级] --> result['baseInfo']['creditRating']
        """
        
        keyworlds = "珠海市优隆贸易有限公司"
        url = self.testEnv  + "/services/open/m/importAndExport/2.0?keyword=" + keyworlds
        res = requests.get(url=url,headers=self.headers).json()
        try:
            print(res)
        except Exception:
            print("获取数据异常!!!")
        else:
            print("新增字段:",res['result']['baseInfo']['creditRating'])