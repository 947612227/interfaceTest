import sys
# sys.path.append("../common")
import unittest

import json
import requests

class TestCase(unittest.TestCase):
    """byCgids"""

    def setUp(self):
        # self.testEnv = 'http://10.39.221.168:20051'
        self.testEnv = "http://10.39.221.168:20051"

        self.headers = {"content-type": "application/json","Authorization":"0f46f1e1-eea9-4828-b69f-0a469845c080"}

    def test_byCgids_主要接口(self):
        """
        优化\n
        请求方式：POST\n

        """
        data = [7254,7254,7254]
        url = self.testEnv  + "/company/legalInfos/byCgids"
        res = requests.post(url=url,headers=self.headers,json=data)
        print(res.text)