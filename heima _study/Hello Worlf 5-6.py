""" for i in range(1,10):
    print(i) """

""" name = "itheima"
length = len(name)
print(f"name函数中的字符串长度是{length}") """

""" str1 = "itheima"
str2 = "itcast"
str3 = "python"

count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}的长度是{count}")

count = 0
for i in str3:
    count += 1
print(f"字符串{str3}的长度是{count}")

#    构造函数  #

def my_len(data):
    count = 0
    for i in data:
        count += 1
    pri`t(f"字符串{data}的长度是{count}")

my_len(str1)
my_len(str2)
my_len(str3)
 """
""" 
def say_hi():
    print("hi,我是2030年的奥迪A6L车主，我现在在努力学习")

say_hi() """

#               练习1               #
""" 
def hesuan():
    print("欢迎来到黑马程序员！")
    print("请出示您的健康码和72小时核算证明")

hesuan() """

#        定义2数相加的函数    #
""" 
def add(x,y):
    sum = x + y
    print(f"{x}+{y}={x+y}")


add(int(input()),int(input())) """


#             升级版自动查核酸           #
""" 
def tempeture(x):
    print("欢迎来到黑马程序员，请出示您的健康码，及72小时核算证明，并配合测量体温！")
    print(f"体温测量中，您的体温是{x}度",end='')
    if(x<=37.5):
        print("体温正常请进！")
    else:
        print("需要隔离")

tempeture(float(input("输入您的温度"))) """

""" 
def add(x,y):
    sum = x + y
    return sum


result = add(int(input()),int(input())) 
print(result) """

""" 
def add(x,y):
    
    sum = x + y
    print(f"两个数相加的结果是{sum}")
    return sum """


#                     函数的嵌套        #
""" 
def fun_b():
    print("----------2----------")

    fun_c()

def fun_a():
    print("-------1--------")

    fun_b()

    print("--------4---------")

def fun_c():
    print("---------3---------")

fun_a() """


#           局部变量       #             global关键字         #
""" 
num = 100

def testA():
    print(num)

testA()


def testB():
    global num           #设置内部变量为全局变量 
    num = 200
    print(num)

testB()
print(num)
"""
#         print(num)            会报错，num的生命周期在函数内部就已经结束 



""" #           综合案例   黑马ATM         #

#全局变量
name = input("请输入你的姓名：")
money = 500000
#        设置一个主菜单
def menu():
    print("-----------------主菜单------------------")
    print(f"{name},您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款    \t[输入2]")
    print("取款    \t[输入3]")
    print("退出    \t[输入4]")
    return int(input(("请输入您的选择：")))
#  查询余额效果
def balance():
    print(f"{name},您好，您的余额剩余：{money}元")
#  存款效果
def deposit():
    global money
    num1 = int(input("请输入您存款的金额："))
    money = add(money,num1)
    print(f"{name},您好，您存款{num1}元成功")
    print(f"{name},您好，您的余额剩余：{money}元")

#  取款效果
def withdrawal():
    global money
    num2 = int(input("请输入您取款的金额："))
    if num2>money:
        print("余额不足，取款失败！")
    else:
        money = sub(money,num2)
        print(f"{name},您好，您取款{num2}元成功")
        print(f"{name},您好，您的余额剩余：{money}元")
# 存款，取款加减元
def add(x,y):
    return x+y
def sub(x,y):
    return x-y

#         主函数      #
while True:
    choice = menu()
    if choice == 1:
        balance()
    elif choice == 2:
        deposit()
    elif choice ==3:
        withdrawal()
    elif choice == 4:
        break
    else:
        print("输入错误，请重新输入")
         """


""" #           综合案例   黑马ATM         #

name = input("请输入您的姓名")
money = 5000000

#          查询余额        #

def balance(show_header=True):
    if show_header:
        print("-----------查询余额------------")
    print(f"{name},您好，您的余额剩余{money}")

#         存款           #

def depoist():
    print("-----------存款------------")
    num = int(input("请输入您要存款的金额"))
    print(f"{name},您好，您存款{num}元成功。")
    global money
    money += num
    balance(False)
    

#        取款           #

def withdrawal():
    print("-----------取款------------")
    num = int(input("请输入您要取款的金额"))
    global money
    if num >money:
        print("您的余额不足")
        
    else:
        print(f"{name},您好，您取款{num}元成功。")
        money -= num
        balance(False)

#        设置一个主菜单      #
def menu():
    print("-----------------主菜单------------------")
    print(f"{name},您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款    \t[输入2]")
    print("取款    \t[输入3]")
    print("退出    \t[输入4]")
    return int(input("请输入您的选择："))

while True:
    choice = menu()
    if choice == 1:
        balance()
        continue
    elif choice == 2:
        depoist()
        continue
    elif choice == 3:
        withdrawal()
        continue
    else:
        break
print("结束啦")
    

     """


#                        第 6 章             #

""" name_list= [ '张三', '李四','王五','李六']
print(name_list)

name=list(['张三', '李四','王五','李六'])
print(name)

name_list1=[['张三', '李四','王五','李六'],[666,True,'dhahid']]
print(name_list1[0][2]) 
print(name_list1[0][0])
print(name_list1[1][2])
print(name_list1[1][1]) 


 """
#list 列表中 my_list[元素下标位置]，，my_list.index('itheima')查找itheima的下表位置，my_list[0]='黑马程序员'，修改下标元素0的值为黑马程序员，
# my_list.insert(2,'黑马程序员'),插入黑马程序员作为下标元素2的位置
# my_list.append('itheima')在最后插入itheima
# name = ['qiaoguandi','真帅','nb666']
# my_list.extend(name)，                      在元素最后插入'qiaoguandi','nb666','克拉斯'
# del my_list[1]
# my_list.pop(0)                   这两个都是列表中的删除
# my_list.remove(666)               指定元素移除，从左到右，移除第一个666，如果要移除两个666，调用两次remove

# my_list.clear()                整个列表清空 

# my_list2.count(1)            统计元素的数量
# len(my_list2)                 统计有多少个元素
""" name_list = ['tome','lili','suoer']
print(name_list[-1])
print(name_list[1])
print(name_list[2])
 

my_list = ['itcast','itheima','python']
 index = my_list.index('itheima')
print(f"itheima在列表中的下表索引值是{index}")

my_list[0]='传智教育'
print(my_list) 
my_list = ['itcast','itheima','python']
my_list.insert(2, "NB克拉斯")         #       2 是将要插入下表的位置    
my_list.append(666)
name = ['qiaoguandi','真帅','nb666']
my_list.extend(name)
print(my_list)
del my_list[1]
my_list.pop(0)
my_list.remove(666)
print(my_list)
my_list.clear()
print(my_list)

my_list2 = [1,1,1,2,3]
count = len(my_list2)
print(my_list2.count(1))
print(count)"""

#                     列表练习案例             #
""" age = [21,25,21,23,22,20]
age2 = [29,33,30]
age.append(31)
print(f"追加一个数字31，到列表的尾部{age}")
age.extend(age2)
print(f"追加一个新列表[29,33,30],到列表的尾部{age}")
num1 = age[age.index(21)]
age.remove(21)
print(f"取出第一个元素是{num1}")
num2 = age[age.index(30)]
age.remove(30)
print(f"取出最后一个元素是{num2}")
index = age.index(31)
print(f"查找元素31，在列表中的下标位置是{index}")

 """


#              while  for   遍历循环

#使用while循环遍历
""" def func1():
    list = ['奥迪A6L','奔驰E300L','宝马7系']
    index = 0
    while index < len(list):
        element = list[index]
        print(f"列表中的元素是:{element}")
        index += 1

#使用for循环遍历

def func2():
    list = [1,2,3,4,5,6]
    for element in list:
        print(f"列表中的元素依次是{element}")

func1()
func2() """




#     练习       #
#while循环练习
""" list= [1,2,3,4,5,6,7,8,9,10]
new_list = []
index = 0
while index<len(list):
    element = list[index]
    index += 1
    if element % 2 == 0:
        new_list.append(element)
print(f"通过while循环，从列表中取出偶数，组成新列表{new_list}")c
 """

# for循环练习#
""" list = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for element in list:
    if element % 2 == 0:
        new_list.append(element)
print(f"通过for循环，从列表中取出偶数，组成新列表{new_list}")
 """


#            元组 tuple        #
""" 
t1 = ('hello',666,True)
t2 = ()
t3 = tuple()
print(f"{type(t1)},{t1}")
print(f"{type(t2)},{t2}")
print(f"{type(t3)},{t3}")
t4 = ('hello',)                # 要加，否则不是元组
print(f"{type(t4)},{t4}")

t5 = ((1,2,3),(4,5,6))
num = t5[1][2]
print(type(t5),t5,num) """

# 元组的 查找下标       index
""" t1 = ('奥迪A6L','奥迪A7L','奥迪A7L','奥迪A7L','奥迪A8L')
num = t1.index('奥迪A7L')
print(num)

#     count
num2 = t1.count('奥迪A7L')
print(num2)

num3 = len(t1)
print(num3)

index = 0
while index<len(t1):
    print(t1[index])
    index+=1

for element in t1:
    print(element)

t2 = (1,2,3,['itheima','itcast'])
print(t2)
t2[3][0] = '奥迪A6L'
t2[3][1] = '奥迪A7L'
print(t2)
 """

#        练习      #
""" student = ('周杰伦',11,['football','music'])
list = []
num = student.index(11)
print(num)
num2 = student[0]
print(num2)
del student[2][0]
print(student)
#student[2].append('codeing')
student[2].insert(0,'coding')
print(student) 

my_str = '12itheima and itcast21'
 value1 = my_str[2]
value2 = my_str[-4]
print(value1,value2) """

#          index  寻找下标  
""" value = my_str.index('and')
print(value)
 """

#           replace 替换
""" new_my_str = my_str.replace('it','程序')
print(new_my_str) """

#           split 分割
""" list = my_str.split()
print(list) """

#           strip  去除前后空格
""" 
new_my_list = my_str.strip()
new_my_list2 = my_str.strip('12')
print(new_my_list,new_my_list2)
 """
#           count


#           len


#         作业        #
#          while               和                for  遍历
""" my_str= '黑马程序员'
index = 0
while index<len(my_str):
    print(f"{my_str[index]}")
    index+=1

for element in my_str:
    print(element,end='') """


#                          练习案例： 分割字符串          #
""" my_Str = "itheima itcast boxuegu"
num = my_Str.count('it')
print(num)
num2 = my_Str.replace(" ","|")
print(num2)
num3 = num2.split("|")
print(num3) """

#                    序列的切片            # 
#         list                            # 
""" list = [0,1,2,3,4,5,6,7,8,9,10]
num = list[0:8:1]
print(num)
num4 = list[3:1:-1]
print(num4)"""

#         tuple                            #
"""tuple = (0,1,2,3,4,5,6)
num1 = tuple[:]
print(num1)
num5 = tuple[::-2]
print(num5)"""

#         str  进行切片                            #
"""
str = 'itheima itcast python'
num2 = str[::2]
print(num2) 
num3 = str[::-1]
print(num3) """

#                       练习案例             #
""" str = "万过月薪,员序程马黑来,nohtyp学"
num1 = str[-10:-15:-1]
print(num1)

num2 = str.split(",")
print(num2)
num3 = num2[1].replace("来","")
print(num3)
num4 =num3[::-1]
print(num4) """



#             集合 set    能够去重               #


""" my_set = {'黑马程序员','传智教育','itheima','黑马程序员','传智教育','itheima','黑马程序员','传智教育','itheima'}
my_set_empty = set()
print(my_set,type(my_set)) """


#              集合 add函数 添加               #
""" my_set = {'itheima','itcast','python'}
my_set.add('hello')
print(my_set)
 """
#              集合 remove  删去              #
""" my_set.remove('python')
print(my_set)
 """

#               集合 pop    随机取元素       #
""" element = my_set.pop()
print(element)
print(my_set) """

#               集合 clear    清空       #

""" my_set.clear()
print(my_set) """
#                集合 difference  两个集合的差集(改变集合1，去掉与集合2中相同的元素)    #
""" set1 = {1,2,3,4,5,6,7,10,11}
set2 = {1,2,3,8,9}
set3 = set1.difference(set2)
print(set1)
print(set2)
print(set3)  """

#                  集合 difference_update,消除两个集合的差集（在集合1 内，删除和集合2相同的元素，集合1改变，集合2 不变
""" set1 = {1,2,3,4,5,6,7,10,11}
set2 = {1,2,3,8,9}
set1.difference_update(set2)
print(set1)
print(set2) """

#                  集合  union 两个集合合并成一个新的集合
""" set1 = {1,2,3,4,5,6,7,10,11}
set2 = {1,2,3,8,9}
set3 = set1.union(set2)
print(set3)
print(set1)
print(set2) """

#                      集合 统计集合元素数量  len()


#                    集合 只有for循环遍历，     因为没有下标，所以不能用while

""" for element in set3:
    print(element,end='') """

#                练习案例           #
""" my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
set1 =set()
for element in my_list:
    set1.add(element)
print(my_list)
print(set1)
 """
#  2026-3-6-19.35      #明天来了先复习图片上的

#                       字典  dict         key:value

""" my_dict = {"王力宏":77, "周杰伦":88, "林俊杰":99}
my_dict2 = {}
my_dict3 = dict()
print(my_dict,type(my_dict))

print(my_dict["王力宏"])
print(my_dict["周杰伦"]) """


#               字典的嵌套   
""" stu_score_dict = {
    "王力宏":{
        "语文":77,
        "数学":66,
        "英语":33
    }, "周杰伦":{
        "语文":88,
        "数学":86,
        "英语":55
    },"林俊杰":{
        "语文":99,
        "数学":96,
        "英语":66
    }
}
print(stu_score_dict) """


#              从字典中取信息

""" score = stu_score_dict["周杰伦"]["英语"]
print(score) """

#               在字典中增加信息，更新信息  字典[key] = value
""" 
my_dict = {"a":99,"b":88,"c":77}
my_dict["d"]=66
my_dict["a"]=33
print(my_dict)
 """

#                 删除元素 字典.pop(key)

""" my_dict.pop("a")
print(my_dict) """

#            清空元素   字典.clear

""" my_dict.clear()
print(my_dict)
 """

#             获取全部的key  字典.keys()

""" my_dict = {"a":99,"b":88,"c":77}

keys = my_dict.keys()
rint(keys)
 """

#            遍历字典  通过keys 得到key  在通过key得到value
#  方法一
""" for key in keys:
    print(f"key是{key}")
    print(f"value值是{my_dict[key]}") """

# 方法二
""" for key in my_dict:
    print(f"key是{key}")
    print(f"value值是{my_dict[key]}")
 """
#                  len(字典)


#                                练习                      #

#        字典的嵌套    字典 = {key:value}
#                                 value嵌套一个字典
""" stu_message = {
    "王力宏":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2,
    },
    "林俊杰":{
        "部门":"市场部",
        "工资":7000,
        "级别":3,
    },
    "张学友":{
        "部门":"科技部",
        "工资":4000,
        "级别":1
    },
    "刘德华":{
        "部门":"市场部",
        "工资":6000,
        "级别":2,
    }

}
print(stu_message)
#  利用for循环，取出薪水的信息         # 利用for循环，字典[][]，取出级别的信息  
for key in stu_message:
     level = stu_message[key]["级别"]

# 利用if判断
     if level == 1:

        # 得到员工的信息   修改员工的信息        在传回员工的信息
        employee_stu_message = stu_message[key]
        employee_stu_message["级别"] = 2
        employee_stu_message["工资"]+=1000
        stu_message[key]=employee_stu_message

print(stu_message) """







# 容器之间的转换
""" my_list = [1,2,3,4,5,6]
my_tuple = (1,2,3,4,5,6)
my_str = "abcdefg"
my_set ={1,2,3.4,5,6}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5} """


""" #     都转列表
print(f"都转列表{list(my_list)}")
print(f"都转列表{list(my_tuple)}")
print(f"都转列表{list(my_str)}")
print(f"都转列表{list(my_set)}")
print(f"都转列表{list(my_dict)}")


#   都转元组
print(f"都转元组{tuple(my_list)}")
print(f"都转元组{tuple(my_tuple)}")
print(f"都转元组{tuple(my_str)}")
print(f"都转元组{tuple(my_set)}")
print(f"都转元组{tuple(my_dict)}")

#都转字符串
print(f"都转字符串{str(my_list)}")
print(f"都转字符串{str(my_tuple)}")
print(f"都转字符串{str(my_str)}")
print(f"都转字符串{str(my_set)}")
print(f"都转字符串{str(my_dict)}")


#都转集合
print(f"都转集合{set(my_list)}")
print(f"都转集合{set(my_tuple)}")
print(f"都转集合{set(my_str)}")
print(f"都转集合{set(my_set)}")
print(f"都转集合{set(my_dict)}")
 """
#进行容器排序  sorted           排序的结果会变成列表对象
""" print(f"进行容器排序{sorted(my_list)}")
print(f"进行容器排序{sorted(my_tuple)}")
print(f"进行容器排序{sorted(my_str)}")
print(f"进行容器排序{sorted(my_set)}")
print(f"进行容器排序{sorted(my_dict)}") """

# 进行容器排序结果反转  reverse = true
""" print(f"进行容器反排序{sorted(my_list,reverse = True)}")
print(f"进行容器反排序{sorted(my_tuple,reverse = True)}")
print(f"进行容器反排序{sorted(my_str,reverse = True)}")
print(f"进行容器反排序{sorted(my_set,reverse = True)}")
print(f"进行容器反排序{sorted(my_dict,reverse = True)}") """