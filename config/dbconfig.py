#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   run.py
@Time    :   2020/01/16 23:13:14
@Author  :   Zhang.Jia 
@Version :   1.0
@Contact :   zhang.jia@xcar.com.cn
@License :   (C)Copyright 2020-2099, Liugroup-NLPR-CASIA
@Desc    :   Python工程

接口测试配置文件
'''

import configparser
import json
import os
import sys
import pymysql
import requests
import xlrd
from pymysql import connect,cursors
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree

json.dump
class DB:

    """
    接口测试配置文件读取
    """
    def __init__(self,dbname):
        # pass

    # def readDBconfig(self, ):
        """读取数据库配置"""
        self.dbpath = os.getcwd()
        self.cf = configparser.ConfigParser()
        self.cf.read(self.dbpath + "/config/config.txt")
        self.secs = self.cf.sections() #获取所有的[A]里面的内容
        self.options = self.cf.options(dbname) #获取[A]里面所有的KEY,等号左边的值
        self.items = self.cf.items(dbname)  # 获取section名为dbname所对应的全部键值对
        config_pr = []
        for i in self.items:
            config_pr.append(i[1])
        self.desc = config_pr[0] #描述
        self.host = config_pr[1] # host
        self.prot = int(config_pr[2]) # 端口
        self.user = config_pr[3] # 用户名 
        self.pass_ = config_pr[4] # 密码
        self.name = config_pr[5] # 库名
        self.table = config_pr[6] # 表名
        self.char_ = config_pr[7] # 编码
        print("数据库描述：" + self.desc + "\n数据库地址：" + self.host + "\n数据库端口：" + \
            str(self.prot) + "\n数据库用户：" + self.user + "\n数据库密码：" + self.pass_ + \
                "\n数据库名称：" + self.name + "\n数据表名称：" + self.table + "\n数据库编码：" + self.char_ )

        
        # self.desc = self.cf.get(dbname, "dbdesc")  #获取数据库描述
        # self.host = self.cf.get(dbname, "dbhost")  # 获取[dbname]中host对应的值

    
    def db_con(self):
        """创建数据库连接"""
        try:
            self.conn = connect(host=self.host, user=self.user, password=self.pass_, \
                port=self.prot, db=self.name, charset=self.char_)
        except Exception as e:
            print("数据库连接异常\n" + str(e))
        else:
            print("连接的数据库为" + self.desc)
            return self.conn

    def db_clear_table(self, table_name):
        """清除表数据"""
        # self.db_con()
        sql = "DELETE FROM " + table_name
        with self.conn.cursor() as cursor:
            cursor.Execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.Execute(sql)
        self.conn.commit()
        self.db_close()

    def db_insert(self, table_name, table_data):
        for key in table_data:
             table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
 
        with self.conn.cursor() as cursor:
           cursor.execute(real_sql)

        # self.conn.commit() # 谨慎一点，不要提交事务
        self.db_close()

    def db_close(self):
        self.conn.close()

if __name__ == '__main__':
    print("欢迎使用爱卡汽车接口测试平台,初始化中...")
    config = DB("db_test")
    coon = config.db_con()
    print(coon)

