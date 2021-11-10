#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   xlsconfig.py
@Time    :   2020/01/17 16:08:43
@Author  :   Zhang.Jia 
@Version :   1.0
@Contact :   zhang.jia@xcar.com.cn
@License :   (C)Copyright 2020-2099, Liugroup-NLPR-CASIA
@Desc    :   Python工程--EXCEL操作集
'''
import requests
import sys
import os
import json
import xlrd
from xlutils.copy import copy
class xls:
    """定义一个EXCEL类"""
    def __init__(self,file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name =  os.getcwd() + "/testcase/DuanShiPinFF/testcase1.xlsx"
            self.sheet_id = 0
        self.data = self.get_xls_data()
        
    def get_xls_data(self):
        """获取sheet内容"""
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
        # print(self.tables)

    def get_lines(self):
        """获取行数"""
        tables = self.data
        return tables.nrows

    def get_cell_value(self, row, col):
        """获取某一个单元格的内容"""
        return self.data.cell_value(row, col)
        

    def write_value(self,row,col,value):
        '''
        写入excel数据
        row,col,value
        '''
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    def get_rows_data(self, case_id):
        """根据caseid找到对应行的内容"""
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    def get_row_num(self, case_id):
        """根据对应的caseid找到对应的行号"""
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num+1

    def get_row_values(self, row):
        """根据对应的caseid 找到对应行的内容"""
        tables = self.data
        row_data = tables.row_values(row)
        return row_data


    def get_cols_data(self, col_id=None):
        """获取某一列的内容"""
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    print("欢迎使用接口测试平台,配置读取中...")
    config = xls()
    # case_path = os.getcwd() + "/testcase/DuanShiPinFF/testcase1.xlsx"
    testcast = config.get_cell_value(1,3)
    print(testcast)
