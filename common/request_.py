#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   request_.py
@Time    :   2020/01/17 16:11:08
@Author  :   Zhang.Jia 
@Version :   1.0
@Contact :   zhang.jia@xcar.com.cn
@License :   (C)Copyright 2020-2099, Liugroup-NLPR-CASIA
@Desc    :   Python工程
'''

import requests
import sys
import os
import json

from requests.api import head
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class goRequest:
    """定义请求类"""
    print(123)
    def get(self, url, data=None, headers=None, cookies=None):
        try:
            req = requests.post(url=url, data=data ,headers=headers, cookies=cookies)
        except Exception as e:
            print("请求失败:", str(e))
            assert False,{"errcode":"error","errmsg":"请求异常"}
            sys.exit(0)
        else:
            return req
            
    def post(self, url, data=None, headers=None, cookies=None):
        print("载入POST方法")
        try:
            req = requests.post(url=url, data=data ,headers=headers, cookies=cookies)
        except Exception as e:
            print("请求失败:", str(e))
            assert False,{"errcode":"error","errmsg":"请求异常"}
            sys.exit(0)
        else:
            return req


    def login(self):
        """登录获取到token\n
        return str-->token

        """
        import requests

        cookies = {
            'TYCID': '93103620179211ec9fb3a54966388f2a',
            'undefined': '93103620179211ec9fb3a54966388f2a',
            'csrfToken': 'PO61aMJ_aKu1mYRUNK2-_g8D',
            'ssuid': '3005784576',
            'bannerFlag': 'true',
            '_bl_uid': 'Fgk23twjoL046O8qt8IOjyzi3Lv7',
            'Hm_lvt_e92c8d65d92d534b0fc290df538b4758': '1631669594,1631868261',
            '_ga': 'GA1.2.598550640.1631868262',
            '_gid': 'GA1.2.1418399558.1631868262',
            'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2213488883948%22%2C%22first_id%22%3A%2217bf2e7d39d180-0c957fe9c8f1e6-7d680a5d-2073600-17bf2e7d39e79d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217bf2e7d39d180-0c957fe9c8f1e6-7d680a5d-2073600-17bf2e7d39e79d%22%7D',
            'tyc-user-info-save-time': '1631868301604',
            'tyc-user-phone': '%255B%252213488883948%2522%255D',
            'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758': '1631929114',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
            'Content-Type': 'application/json; charset=UTF-8',
            'cookie':'TYCID=93103620179211ec9fb3a54966388f2a; undefined=93103620179211ec9fb3a54966388f2a; csrfToken=PO61aMJ_aKu1mYRUNK2-_g8D; ssuid=3005784576; bannerFlag=true; _bl_uid=Fgk23twjoL046O8qt8IOjyzi3Lv7; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1631669594,1631868261; _ga=GA1.2.598550640.1631868262; _gid=GA1.2.1418399558.1631868262; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2213488883948%22%2C%22first_id%22%3A%2217bf2e7d39d180-0c957fe9c8f1e6-7d680a5d-2073600-17bf2e7d39e79d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217bf2e7d39d180-0c957fe9c8f1e6-7d680a5d-2073600-17bf2e7d39e79d%22%7D; tyc-user-info-save-time=1631868301604; tyc-user-phone=%255B%252213488883948%2522%255D; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1631929114',
        }
        data = {"mobile":"13488883948","cdpassword":"329d34c990a979b2f0fc2b5bc337ac8d","loginway":"PL","autoLogin":"ture","type":"","challenge":"964399b31c7e227ac3b01a0ef642c77eeh","validate":"bdde7a5c7f40a9903da9549695907d90","seccode":"bdde7a5c7f40a9903da9549695907d90|jordan"}

        res = requests.post('https://www.test63.tianyancha.com/cd/login.json', headers=headers,  json=data ,cookies=cookies)

        print(res.text)


# if __name__ == '__main__':
#     rest = goRequest()
#     url = "https://sj.test.tianyancha.com/api/getAdvancedFilterResult"
#     data = {"pageNum":1,"pageSize":100,"filterJson":{"groupName":"all","conditions":[{"name":"establishTime","conditionName":"timein","optionValues":["1630425600","1633017599"]}]}}
#     headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
#     'Content-Type': 'application/json;charset=UTF-8',
#         }
#     cookies = {
#         'auth_token':"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzQ4ODg4Mzk0OCIsImlhdCI6MTYzMTkyOTE4NiwiZXhwIjoxNjYzNDY1MTg2fQ.9BmFt3a04qsqtZkIijjx2LEG2iIriOPGc8f3lTlIXClmVboJTuotqHHwg-jc9PaG7uv-WWkqnTZ8GXwPXyl_JA",
#     }
#     res = rest.post(url=url, data=json.dumps(data), headers=headers, cookies=cookies)
#     print(res.text)

    # rest.login()




