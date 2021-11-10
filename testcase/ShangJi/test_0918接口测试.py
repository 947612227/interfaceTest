#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# @File    : test_816搜索增加匹配原因字段.py
# @Time    : 2021/08/23 10:06:25
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
            'x-auth-token': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMDIyMjIyMjIzMiIsImlhdCI6MTYzMTg2NTM4MSwiZXhwIjoxNjYzNDAxMzgxfQ.aIdJ2W7RgQSPc3MwU4KQ17ixc21bF6t1ADJHDkKfxui9z4n5XpvLXjSwFC7-mAkNQOj4Hai0oxO4DDNk7rMN9w',
            'authorization': '10222222232###1111###111111',
            'version': 'TYC-Web',
        }
        self.cookies = {
            'auth_token': "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMDIyMjIyMjIzMiIsImlhdCI6MTYzMTg2NTM4MSwiZXhwIjoxNjYzNDAxMzgxfQ.aIdJ2W7RgQSPc3MwU4KQ17ixc21bF6t1ADJHDkKfxui9z4n5XpvLXjSwFC7-mAkNQOj4Hai0oxO4DDNk7rMN9w",
        }

    def test_新建线索(self):
        """
        修改线索详情\n
        Method:GET\n
        url:http://172.28.83.239/mock/114/clue/edit
        """
        url = "https://sj.test.tianyancha.com/api/clueManagement/editClueItem"
        data = json.dumps({"clueName":"保时捷（中国）汽车销售有限公司","companyNameAlias":"保时捷（中国）汽车销售有限公司","companyName":"","nextFollowTime":1631932059546,"telephone":"010-61872706","mobile":"13488883948","email":"zhangjia@tianyancha.com","wechatNum":"ajzhangjia","qqNum":"947612227","website":"www.porsche.cn/china/zh","address":"中国（上海）自由贸易试验区世纪大道826号17层（实际楼层：15层）","postCode":"zhangjia@tianyancha.com","scale":"51-100 人","registerCapatial":"8888","establishTime":1128873600000,"remark":"备注备注备注","clueId":31680,"graphId":"null","highTechCompany":0,"listedCompany":0})
        res = self.req.post(url=url, data=data,headers=self.headers, cookies=self.cookies)
        print(res.text)

    def test_新建客户(self):
        """
        新建客户\n
        Method:POST\n
        return:None\n
        url:http://172.28.83.239/project/114/interface/api/21211
        
        """

        url = self.interfaceEnvHost + "/customer/edit"
        data = {
            "address":"北京市地址",
            "companyName":"北京市的一家小公司而已",
            "customerId":"",
            "customerLevel":"",
            "customerSource":"",
            "email":"tianyancha@tianyancha.com",
            "establishTime":"",
            "graphId":3204428892,
            "highTechCompany":"",
            "listedCompany":"",
            "mobile":"13488883948",
            "name":"张佳-新建客户",
            "nextFollowTime":"",
            "postCode":"102304",
            "qqNum":"947612227",
            "registerCapatial":"",
            "remark":"备注备注备注",
            "scale":"",
            "telephone":"010-61872706",
            "website":"http://wwww.tianyancha.com",
            "wechatNum":"ajzhangjia"
        }

        res = self.req.post(url=url,data=json.dumps(data),headers=self.headers,cookies=self.cookies)
        print(res.text)

    def test_新建客户去重(self):
        """
        URL:http://172.28.83.239/project/114/interface/api/21211\n
        Method:POST\n

        """
        url = self.interfaceEnvHost + "/customer/edit"
        data = {
            "address":"",
            "companyName":"百度科技",
            "customerId":"139",
            "customerLevel":"",
            "customerSource":"",
            "email":"",
            "establishTime":"",
            "graphId":"3204428892",
            "highTechCompany":"",
            "listedCompany":"",
            "mobile":"13488883948",
            "name":"百度",
            "nextFollowTime":"",
            "postCode":"",
            "qqNum":"",
            "registerCapatial":"",
            "remark":"",
            "scale":"",
            "telephone":"",
            "website":"",
            "wechatNum":"",
        }
        res = self.req.post(url=url,data=json.dumps(data),headers=self.headers,cookies=self.cookies)
        print(res.text)

    def test_编辑客户详情(self):
        """
        
        URL:	http://172.28.83.239/project/114/interface/api/21211
        """
        url = self.interfaceEnvHost + "/customer/edit"
        data = {
            "address":"",
            "companyName":"百度科技",
            "customerId":"139",
            "customerLevel":"",
            "customerSource":"",
            "email":"",
            "establishTime":"",
            "graphId":"3204428892",
            "highTechCompany":"",
            "listedCompany":"",
            "mobile":"13488883948",
            "name":"百度",
            "nextFollowTime":"",
            "postCode":"",
            "qqNum":"",
            "registerCapatial":"",
            "remark":"",
            "scale":"",
            "telephone":"",
            "website":"",
            "wechatNum":"",
        }
        res = self.req.post(url=url,data=json.dumps(data),headers=self.headers,cookies=self.cookies)
        print(res.text)

    def test_编辑联系人详情去重(self):
        """
        联系人去重\n
        Method:POST\n
        URL:http://172.28.83.239/project/114/interface/api/21193
        """
        url = self.interfaceEnvHost + "/contacts/update/contact"
        data = {
            "address":"ffffff",
            "birthday":"",
            "clueId":"",
            "clueName":"",
            "contactName":"张佳-测试姓名",
            "copy":"",
            "customerId":139,
            "department":"",
            "duty":"",
            "email":"",
            "id":139,
            "mobile":"13488883948",
            "postcode":"",
            "qqNum":"",
            "remark":"备注备注备注信息",
            "sex":"",
            "source":"",
            "star":"",
            "telephone":"010-61872706",
            "wechatNum":"",
        }
        res = self.req.post(url=url,data=json.dumps(data),headers=self.headers,cookies=self.cookies)
        print(res.text)

    def test_添加联系人(self):
        """
        添加联系人\n
        Method:POST\n
        URL:http://172.28.83.239/project/114/interface/api/21166\n
        """
        url = self.interfaceEnvHost + "/contacts/add/contact"
        data = {
            "address":"",
            "birthday":"",
            "clueId":"",
            "clueName":"",
            "contactName":"张佳-测试姓名1",
            "copy":"",
            "customerId":139,
            "department":"",
            "duty":"",
            "email":"",
            "id":139,
            "mobile":"13488883948",
            "postcode":"",
            "qqNum":"",
            "remark":"备注备注备注信息",
            "sex":"",
            "source":"",
            "star":"",
            "telephone":"010-61872706",
            "wechatNum":"",
        }
        res = self.req.post(url=url,data=json.dumps(data),headers=self.headers,cookies=self.cookies)
        print(res.text)



