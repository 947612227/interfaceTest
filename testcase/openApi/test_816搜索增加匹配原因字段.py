#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# @File    : test_816搜索增加匹配原因字段.py
# @Time    : 2021/08/23 10:06:25
# @Author  : 张佳 
# @Version : 1.0
# @Contact : zhangjia@tianyancha.com


import sys
# sys.path.append("../common")
import unittest

import json
import requests

class TestCase(unittest.TestCase):
    """816新增返回字段「匹配原因」"""

    def setUp(self):
        self.testEnv = 'http://10.39.222.108:20064'
        self.headers = {"Authorization": "f37ed796-41c7-45d3-b7fc-b841662fd7d1"}

    def test_816_搜索(self):
        """
        test816
        匹配原因\n
        请求方式：GET\n
        返回格式：JSON
        改动：新增返回字段[匹配原因] --> result['items']['matchType']
        """
        
        keyworlds = "北京百度网讯科技有限公司"
        url = self.testEnv  + "/services/open/search/2.0?word=" + keyworlds
        res = requests.get(url=url,headers=self.headers).json()
        # 
        n = 0
        try:
            print(res)
        except Exception:
            print("获取字段出现异常！！！")
        else:
            for i in range(len(res['result']['items'])):
                n += 1
                print(str(n),"公司名字-->",res['result']['items'][i]['name'])
                print(str(n),"匹配原因-->",res['result']['items'][i]['matchType'])
                
