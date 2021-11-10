#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# @File    : test_816搜索增加匹配原因字段.py
# @Time    : 2021/08/23 10:06:25
# @Author  : 张佳 
# @Version : 1.0
# @Contact : zhangjia@tianyancha.com


import sys
import unittest
import json
from unittest.main import main
import requests

class TestCase(unittest.TestCase):
    """459特殊企业基本信息"""

    def setUp(self):
        self.testEnv = 'http://open.api.tianyancha.com'
        self.headers = {"Authorization": "36ded9cc-6080-4570-9f14-badd0828bf88"}
        # "36ded9cc-6080-4570-9f14-badd0828bf88" --线上

    def test_459_特殊企业基本信息(self):
        """
        请求方式：GET\n
        返回格式：JSON
        改动：
        """
        
        keyworlds = "22822"
        url = self.testEnv  + "/services/open/ic/baseinfoV2/2.0?keyword=" + keyworlds
        res = requests.get(url=url,headers=self.headers).json()
        print(url,'\n')
        print(res)