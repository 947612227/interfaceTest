import sys
# sys.path.append("../common")
import unittest

import json
import requests

class TestCase(unittest.TestCase):
    """1116企业基本信息"""

    def setUp(self):
        self.testEnv = 'http://open.api.tianyancha.com'
        self.headers = {'Authorization': '0f46f1e1-eea9-4828-b69f-0a469845c080'} 
        
    def test_1116_product_企业基本信息(self):
        """
        keyword:北京百度网讯科技有限公司\n

        """
        keyword = "北京百度网讯科技有限公司"
        url = self.testEnv  + "/services/open/ic/baseinfo/normal?keyword=" + keyword
        res = requests.get(url=url,headers=self.headers)
        print((res.text))



