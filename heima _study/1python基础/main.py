""" 
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1设计一个类，可以完成数据的封装
2设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3读取文件，生产数据对象
4进行数据需求的逻辑计算（计算每一天的销售额）
5通过pyecharts进行绘图

 """

#3
"""import json
import pymysql
from pymysql import Connection
from file_define import FileReader, TextFileReader,JsonFileReader
from data_define import Record
from pymysql import Connection
text_file_reader = TextFileReader('D:/2011年1月销售数据.txt')
json_file_reader = JsonFileReader("D:/2011年2月销售数据JSON.txt")

text_record:list[Record] = text_file_reader.read_data()
json_record:list[Record] = json_file_reader.read_data()

all_record = text_record + json_record
 """
""" record_dict = {}
for record in all_record:
    if record.date in record_dict.keys():
        record_dict[record.date] += record.money
    else:
        record_dict[record.date] = record.money

print(record_dict)
 """

""" #构建MySQL连接对象
conn = Connection(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password='8055241013',
    autocommit=True
)
#获得游标
cursor = conn.cursor()
#选择数据库
conn.select_db("py_sql")
#组织SQL语句
for record in all_record:
    sql = f"insert into orders(order_date,order_id,money,province) values('{record.date}','{record.order_id}','{record.money}','{record.province}')"
#执行SQL语句
    cursor.execute(sql)


#关闭

conn.close()
import pymysql
import json


conn = pymysql.Connection(
    host='localhost',
    port=3306,
    user='root',
    password='8055241013',
    autocommit=True,
)
#获取游标对象
cursor = conn.cursor()
#选择数据库
conn.select_db("py_sql")
#使用游标对象，执行sql语句
cursor.execute('select * from orders')
#获取所有记录
results = cursor.fetchall()
#定义字段名（要与查询的一致）
name = ['date','order_id','money','province']
#建立字典
dict_results = []
for r in results:
    #将元组转为字典 zip配对字段名和值
    r_dict = dict(zip(name,r))
    r_dict['date'] = r_dict['date'].isoformat()
    dict_results.append(r_dict)

with open('D:/2011年2月json.txt','w',encoding='UTF-8')as f:
    json.dump(dict_results,f,ensure_ascii=False,indent =4)
conn.close() 
"""


""" from pymysql import Connection
import json

conn = Connection(
    port = 3306,
    host = 'localhost',
    user = 'root',
    password='8055241013',
    autocommit=True
)
#建立游标对象
cursor = conn.cursor()
#获取连接
conn.select_db('py_sql')
#执行sql
cursor.execute('select * from orders')
#创建JSON文件
f = open('D:/2011年2月份json数据.txt','w',encoding='UTF-8')
#创建字典
dict_sql = {}
#fetchall,获取所有结果行
results = cursor.fetchall()
#for循环
for r in results:
    date = str(r[0])
    order_id = r[1]
    money = r[2]
    province = r[3]
    dict_sql['date'] = date
    dict_sql['order_id']=order_id
    dict_sql['money']=money
    dict_sql['province'] = province
    print(dict_sql)
    data_str = json.dumps(dict_sql,ensure_ascii=False)
    f.write(f"{data_str}\n")

f.close() """

