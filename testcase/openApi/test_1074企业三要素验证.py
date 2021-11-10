#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# @File    : test_1074企业三要素验证.py
# @Time    : 2021/08/25 09:38:29
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
        
    def test_1074_企业三要素验证(self):
        """
        code:纳税识别号\n
        name:公司名\n
        legalPersonName:法人\n
        """
        code = "91110000802100433B"
        name = "珠海市优隆贸易有限公司"
        legalPersonName = "梁志祥"
        url = self.testEnv  + "/services/open/ic/verify/2.0?code="+ code + "&name=" +name + "&legalPersonName=" + legalPersonName
        res = requests.get(url=url,headers=self.headers)
        print(res)