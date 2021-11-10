#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# @File    : test_816搜索增加匹配原因字段.py
# @Time    : 2021年09月26日16:58:07
# @Author  : 张佳
# @Version : 1.0
# @Contact : zhangjia@tianyancha.com


import unittest
import json
from unittest.main import main

from requests.api import head
from common.request_ import goRequest


class TestCase(unittest.TestCase):
    """天眼商机-接口测试"""

    # def __init__(self):
    #     """初始化请求类"""
        

    def setUp(self):
        self.req = goRequest()
        self.testEnv = 'https://sj.test.tianyancha.com'
        self.interfaceEnvHost = "http://10.2.18.5:10003/sherlock-crm"
        # self.headers = {"Authorization": "36ded9cc-6080-4570-9f14-badd0828bf88"}
        # "36ded9cc-6080-4570-9f14-badd0828bf88" --线上
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
            'Content-Type': 'application/json;charset=UTF-8',
        }
        self.cookies = {
            'TYCID': "ab4cc2401cdc11ec845a13219411842a; undefined=ab4cc2401cdc11ec845a13219411842a; ssuid=3008242700; _ga=GA1.2.2019170770.1632449503; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2213488883948%22%2C%22first_id%22%3A%2217c159205d548f-0d582fde99c03f-7d680a5d-2073600-17c159205d691e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217c159205d548f-0d582fde99c03f-7d680a5d-2073600-17c159205d691e%22%7D; tyc-user-phone=%255B%252213488883948%2522%255D; bannerFlag=true; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1632449503,1632624629; _gid=GA1.2.1221842676.1632624629; bad_idb0e6cf40-a70a-11eb-9a75-4d3e44bda0ca=6c79d391-1e90-11ec-873c-9142451d9c5d; nice_idb0e6cf40-a70a-11eb-9a75-4d3e44bda0ca=6c79d392-1e90-11ec-873c-9142451d9c5d; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1632645581; tyc-user-info={%22isExpired%22:%220%22%2C%22mobile%22:%2213488883948%22%2C%22state%22:%223%22%2C%22vipManager%22:%220%22}; tyc-user-info-save-time=1632645588070; SECKEY_CID1=1a27552cfde2d295d1fb6169cec7e1ac265d94eb; BMAP_SECKEY=6b58eea4a726aa90838886f5a05bef8198a12f84742bd25e36d5f3c0baf1bfe1ada14360fd40b88dcd24c43cfff98deb7f40b57ae0cfa737054e79f3807a2bb8edc000bb6b6c94ea162c401efc9b1baab28020803b5eaa40d859391a8e1c5937d438a028fccd4628cb34e3a8d47ada69d5cc1df523352f703d6e8af4ef1c6f1f73a7b32111b7a296a89dd6437f43dc44551123f96eae54cfe326d1148c970ca2ef38ee2cc24f733244751477ce308eb737a926acce5d873bd37821784efa5c7bf8c9af7dbca12959f908c08bc2bc5eb50851071081f40b15422125649f9c2d818204430bb68fc9f6601819c02f2a120d",
        }

    def test_商机免费试用(self):
        """
        商机免费试用 \n
        Method:POST \n
        url:https://sj.tianyancha.com/api/applyProbation
        """
        url = "https://sj.test.tianyancha.com/api/clueManagement/editClueItem"
        data = json.dumps({"companyName":"北京金堤科技有限公司","companyId":2318455639,"userName":"免费试用-0001","mobile":"13671333005","channel":""})
        res = self.req.post(url=url, data=data,headers=self.headers,cookies=self.cookies)
        print(res.text)

    
