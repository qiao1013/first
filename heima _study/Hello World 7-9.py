import sys
# 将 my_package 所在的父目录（python 目录）添加到 sys.path
sys.path.append(r'C:\Users\乔\Desktop\python')
#        第7章
#         函数的多返回值
""" def test():
    return 1,2,3

x,y,z = test()
print(x,y,z) """

#          位置参数
""" def stu_message(name,age,gender):
    print(name,age,gender)
stu_message("tom",18,"男")
stu_message(name = '小明',age = 20,gender='男') """

#   设置默认值统一都在最后
""" def stu_message(name,age,gender="男"):
    print(name,age,gender)
stu_message("xiaoming",20) """

#        不定长传参 *args是元组类型的  **kwargs是字典类型的，满足key = value
""" def test(*args):
    print(args)

test(18,'hello',True)

def test1(**kwargs):
    print(kwargs)
test1(name='小美',age = 20,gender = '女') """

#        函数作为参数进行传参
""" def add(x,y):
    sum = x + y
    return sum
def test_func(add):
    result = add(1,2)
    print(result)
test_func(add)
 """
#         lambda

""" def test_func(computer):
    result = computer(1,2)
    print(result)
test_func(lambda x,y:x+y) """

#-------------------------第8章--------------------#
#       打开文件
""" f = open("D:\测试.txt","r", encoding="UTF-8")
print(type(f)) """

#      读取文件 read()
""" print(f.read(10))
print(f.read()) """

#  连续调用两个read，第二个Read从第一个read读取末开始读取


#           readlines()读取文件的全部行，封装到列表中
""" lines =f.readlines()
print(lines)
 """
#           readline 一次读取一行内容
""" line = f.readline()
line2 = f.readline()
line3 = f.readline()
print(line)
print(line2)
print(line3)
f.close() """

#              with open() as f

""" with open("D:\测试.txt",'r',encoding='UTF-8') as f:
    for line in f:
        print(line) """


#               练习          #
#第一种方法
""" f = open("D:/练习.txt",'r',encoding="UTF-8")
words = f.read()
print(words.count('itheima'))
f.close """
#第二种方法
""" f = open("D:/练习.txt",'r',encoding="UTF-8")
count = 0
for line in f:
    line = line.strip()  #去掉首尾的空格和换行符
    words = line.split(' ')  # 按照中间的空格分割成一个一个单词
    for word in words:
        if word == 'itheima':
            count+=1
print(count)
f.close
 """



#  文件的写入 write   创建一个文件写入
""" f = open("D:/test1.txt",'w',encoding='UTF-8')
f.write("乔冠迪真帅，年薪60万，开奥迪A6L")
f.flush
 """

#   打开一个有内容的文件写入
""" 
f = open("D:/练习.txt",'w',encoding='UTF-8')
f.write("乔冠迪真帅，年薪60万，开奥迪A6L")
f.flush """

#           write  add  read readline readlines



#        练习         #
""" fr = open("D:/bili.txt",'r',encoding='UTF-8')
fw = open("D:/bili.txt.bak",'w',encoding='UTF-8')
for line in fr:
    line=line.strip()

    if line.split(',')[4] == '测试':          #字符串split以后，会得到列表，而write()无法读取列表，所以line.split(',')[4]这样写，生命周期就在if里，而不改变line
        continue
    fw.write(line)# write()写入的是字符串       #跳过了测试这一行，本身line没有变
    fw.write('\n')
    print(line)

fr.close()
fw.close()  """
"""  line = line.strip()
    if line.split(',')[4]=='测试':
        continue
    fw.write(line)
    fw.write('\n')
fr.close()
fw.close() """

#-----------------------第九章————————————————————————————————————
""" try:
    f = open("D:/test2.txt",'r',encoding='UTF-8')
except:
    f = open("D:/test2.txt",'w',encoding='UTF-8') """
#捕获指定的异常
""" 
try:
    pirnt(name)
except NameError as e:
    print("出现了异常")
    print(e) """
#   捕获多个异常
""" try:        
    1/0
except (NameError,ZeroDivisionError) as e:
    print("出现BUG")
    print(e)

 """

#         捕获全部异常  
""" try:
    1/0
except Exception as e:
    print("出现异常了")
    print(e) """
#            没有异常＋else
""" try:
    f = open("D:/123456.txt",'r',encoding='UTF-8')
except Exception as e:
    f = open("D:/123456.txt",'w',encoding='UTF-8')
    print("有异常")
    print(e)
else:
    print("没有异常。")
finally:
    print("我要开奥迪A6L")  """

#       异常具有传递性
""" 
def func1():
    print("1的开始")
    num = 1 / 0
    print("1的结束")

def func2():
    print("2的开始")
    func1()
    print("2的结束")

def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了，信息是{e}")
main()
 """

#  测试上传GitHub
#        模块导入，模块其实就是python文件，from[模块名]import[模块|类|变量|*]*是全部内容as[别名]
""" import time     #导入python内置文件，（也就是time.py)
print("你好")
time.sleep(5)
print("我好")
 """

#     from模块名import 功能名      只能导入一个功能
""" from time import sleep
print("你好")
sleep(5)
print("我好") """

# from 模块名  import*       *表示模块的全部功能
""" from time import *
print("你好")
sleep(5)                     #与第一个的区别是前面不用加模块名
print("你好") """

# from 模块名 import * as
# 使用as给特定功能加上别名

# 自定义模块，新建了一个python文件my_module
""" import my_module1 
my_module1.test1(10,20)
 """

#导入模块时，出现命名相同的函数，第二个会把第一个覆盖掉


#在测试中忘记删测试的调用函数了需要加main

# __all__ = ['里面写什么，就只能用这个模块的什么，*不在指所有了']
""" from my_module1 import*
# test1(2,5)

test2()
 """

#    包其实就是文件夹，里面全是python模块，不过要加__init__.py才能变成python包

""" import my_package.my_module2
my_package.my_module2.test()

 """

