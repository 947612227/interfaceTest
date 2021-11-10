#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# @File    : baseClass.py
# @Time    : 2021/08/01 11:09:20
# @Author  : 张佳 
# @Version : 1.0
# @Contact : zhangjia@tianyancha.com
# @desc    : 工具类 操作excel 等

import pandas as pd
import os
import requests
import json

'''
id      ssl     method      host        path    port    parameters
1(00)  True(01)  GET(02) 10.222.(03)  /serv(04) 20064(05) ?keyword=xxx(06)
x(10)  False(1,1)
'''

class ExcelData():
    """操作EXCEL数据读写"""
    def __init__(self):
        pass

    def readExcel(self):
        file = os.getcwd()
        excelPath = file + "/testcase/testcase1.xlsx"
        self.df = pd.read_excel(excelPath,sheet_name="Sheet1")
        return self.df

    def writeJson(self,obj,filename):
        """将响应写到本地的json文件中"""
        # print(obj)
        path = os.getcwd()+"/file/json/"+filename
        obj = json.dumps(obj,sort_keys =True,indent=2,separators=(',',':'),ensure_ascii=False)
        with open(path + ".json","w+",encoding="utf-8") as files:
            files.write(obj)

    def requests(self,headers):
        """一个请求而已"""
        # print(self.df.shape[0]) #2
        for i in range(self.df.shape[0]):
            id = self.df.iloc[i,0]
            ssl = self.df.iloc[i,1]
            method = self.df.iloc[i,2]
            host = self.df.iloc[i,3]
            path = self.df.iloc[i,4]
            port = self.df.iloc[i,5]
            params = self.df.iloc[i,6]
            data = self.df.iloc[i,7]
            # /services/open/ic/baseinfo/normal?keyword = 中航重机股份有限公司
            if ssl is True:
                #        SSL  
                url ="https://" + host + ":" + str(port) + path + params
            else:
                url ="http://" +  host + ":" + str(port) + path + params

            print(url)

            if method.lower() == "get":
                try:
                    res = requests.get(url=url,headers=headers,verify=False)
                except Exception as e1:
                    print(str(e1))
                else:
                    # print(json.loads(res.text))
                    jsData = json.loads(res.text)
                    self.writeJson(jsData,params)
            else:
                try:
                    res = requests.post(url=url,headers=headers,verify=False)
                except Exception as e1:
                    print(str(e1))
                else:
                    # print(json.loads(res.text))
                    jsData = json.loads(res.text)
                    self.writeJson(jsData,params)     

            
            
            
            # try:
            #     res = requests.method(url=url,method=method,params=params,headers=headers,data=data,json=json,verify=False)
            # except Exception as e:
            #     print(str(e))
            # else:
            #     print(json.loads(res.text))
            #     return json.loads(res.text)

                



'''

# print(self.df.shape[0])    #行和列 元祖 (行,列) 数
# print(df.shape[0]) #行
# print(df.shape[1]) #列
# print(self.df.iloc[0,2])  # 数据第一行 第二列()
# print(self.df.iat[0,1])
# return self.df
# iloc[[0,1],[0,1]] #提取第0、1行，第0、1列中的数据
print(df.head())
print(df.shape)
print(df.info)
print(df['id']) #根据列名返回整列
print(df[['id','username']]) #返回多列
print(df.iloc[0,1])  #第0行第1列内容
print(df.iloc [0,:]) #第一行 key \t value

pd.read_csv (filename)# 从 CSV 文件导入数据
pd.read_table (filename)# 从限定分隔符的文本文件导入数据
pd.read_excel (filename)# 从 Excel 文件导入数据
pd.read_sql (query, connection_object)# 从 SQL 表 / 库导入数据
pd.read_json (json_string)# 从 JSON 格式的字符串导入数据
pd.read_html (url)# 解析 URL、字符串或者 HTML 文件，抽取其中的 tables 表格
pd.read_clipboard ()# 从你的粘贴板获取内容，并传给 read_table ()
pd.DataFrame (dict)# 从字典对象导入数据，Key 是列名，Value 是数据
'''