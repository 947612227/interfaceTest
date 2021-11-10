import unittest
import json
import requests

class TestCase(unittest.TestCase):
    """byCgids"""

    def setUp(self):
        # self.testEnv = 'http://10.39.221.168:20051'
        self.testEnv = "http://10.39.221.168:20051"

        self.headers = {"content-type": "application/json","Authorization":"0f46f1e1-eea9-4828-b69f-0a469845c080"}

    def test_test(self):
        res = requests.get("http://www.baidu.com")
        print(res)