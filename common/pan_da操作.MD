pd.read_csv (filename)# 从 CSV 文件导入数据
pd.read_table (filename)# 从限定分隔符的文本文件导入数据
pd.read_excel (filename)# 从 Excel 文件导入数据
pd.read_sql (query, connection_object)# 从 SQL 表 / 库导入数据
pd.read_json (json_string)# 从 JSON 格式的字符串导入数据
pd.read_html (url)# 解析 URL、字符串或者 HTML 文件，抽取其中的 tables 表格
pd.read_clipboard ()# 从你的粘贴板获取内容，并传给 read_table ()
pd.DataFrame (dict)# 从字典对象导入数据，Key 是列名，Value 是数据

#导出
df.to_csv (filename)# 导出数据到 CSV 文件
df.to_excel (filename)# 导出数据到 Excel 文件
df.to_sql (table_name, connection_object)# 导出数据到 SQL 表
df.to_json (filename)# 以 Json 格式导出数据到文本文件

#取值
df.head() # 取所有行
df.head(2) # 去前两行
df.tail(n) #倒数第n行
df.shape #查看行数列数

