import sys
# sys.path.append("../common")
import unittest

import json
import requests

class TestCase(unittest.TestCase):
    """1116企业基本信息"""

    def setUp(self):
        self.testEnv = 'http://10.39.222.108:20064'
        self.headers = {"Authorization": "f37ed796-41c7-45d3-b7fc-b841662fd7d1"}
        
    def test_1116_test_企业基本信息(self):
        """
        code:纳税识别号\n
        """
        keyword = "北京百度网讯科技有限公司"
        url = self.testEnv  + "/services/open/ic/baseinfo/normal?keyword=" + keyword
        res = requests.get(url=url,headers=self.headers)
        print((res.text))


