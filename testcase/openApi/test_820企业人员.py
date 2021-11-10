import sys
# sys.path.append("../common")
import unittest

import json
import requests

class TestCase(unittest.TestCase):
    """820重构"""

    def setUp(self):
        self.testEnv = 'http://10.39.222.35:20064'
        self.headers = {"Authorization": "f37ed796-41c7-45d3-b7fc-b841662fd7d1"}

    def test_820_主要人员(self):
        """
        test820
        重构\n
        请求方式：GET\n
        返回格式：JSON重构\n
        原因：重构
        """
        
        keyworlds = "北京百度网讯科技有限公司"
        url = self.testEnv  + "/services/open/ic/staff/2.0?keyworld=" + keyworlds
        res = requests.get(url=url,headers=self.headers)
        print(res)