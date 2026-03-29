#1-4
# print("Hello World!")
"""

ni niu B

#写一个整数字面量
print(666)
# 写一个浮点数字面量
print(13.14)
# 写一个字符串字面量
print("Hello World!1")

# 定义一个变量，用来记录钱包的余额
money = 1000000000.500
print("钱包还有：", money, "元") 

# 买了一量奥迪A8L 花费1500000元
money -= 1500000
print(money)
# 写一个整数字面量
print(666)
# 钱包剩的余额
money = 10000000
# 你买了一辆奥迪A8L花费2000000
money-=2000000
print("你的钱包还剩下",money)

print(type("dede的"))
name = "黑马程序元"
str_type=type(name)
print(str_type)"""
# 将数据类型转换成字符串
#num_str = str(11)
#print(type(num_str))
# 将字符串类型转换成数字类型
# 想要将字符串转换成数字类型，字符串中的内容必须是整数或者浮点数
# str_num =int("niubiclass")
# 只要加上双引号就是字符串。
# num = int ("11")
#print(type(num), num)
# 字符串 浮点型 整数型 
# str  float int
# type  类型检测
# 将数字类型转换为字符串类型
"""num_str = str(11)
print(type(num_str),num_str)
float_str= str(13.14)
print(type(float_str),float_str)"""
# 将字符串类型转换为数字类型，注意：只能是
#str_int = int("123")
#print(type(str_int),str_int)
#num = float("11.345")
#print(type(num),num)
# 万物皆可以转字符串 也就是 str(X)无要求
# 字符串转数字 字符串中的内容都是数字才行
#num = int(11.84)
#print(type(num),num)
"""print("1+1=",1+1)
print("2*3=",2*3)
print("5-4=",5-4)
print("11/2=",11/2)
print("11//2=",11//2)
print("11%2=",11%2)
print("2**2",2**2)"""


#print("'黑马程序员'")
#print('"黑马程序员"')
#print("\"黑马程序员\"")
"""
print("我是黑马程序员"+"月薪过万来黑马")

name = "黑马程序员"
address = "桂圆10栋801——30"
tel = str(15039468156)
print("我的名字是："+ name + ",我的地址是:" + address + "，我的电话是：" + tel )"""

#字符串格式化

#占位型拼接 %S %
"""
name = "黑马程序员"
message = "月薪过万就来 %s " % name
print(message)
tel = 15039468156

a = "我的电话是%s" % tel
print(a)
class_num = 57
avg_salary = 150000
print("python大数据学科,北京%s期,毕业平均工资:%s"%(class_num, avg_salary))

name = "王者荣耀"
set_up_year = 2016
stock_price = 19.9999
#message  = "我是%s,我成立于%d年,成立时的股价是%8.4f元" % (name,set_up_year,stock_price)
print(f"{name}成立于{set_up_year}年，成立时的股价是{stock_price}元")
#print(message)
print(f"{name}成立于{set_up_year}，成立时的股价是{stock_price}元")
print(f"{name}成立于{set_up_year}年，成立时的股价是{stock_price}元")

# 字符串中表达式格式化

print("1+1的结果是%d"%(1+1))
print(f"5*3的结果是{5*3}")
print("字符串在python中的类型是%s"% type("字符串"))

#  股价计算小程序

name = "王者荣耀"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
stock_price_all = stock_price * (stock_price_daily_growth_factor ** growth_days)
message1 = (f"公司：{name},股票代码{stock_code},当前股价是：{stock_price}")
message2 = ("每日增长系数是%.1f,经过%d天的增长后,股价达到了:%.2f"%(stock_price_daily_growth_factor,growth_days,stock_price_all))
print(message1+ message2)


print("请告诉我你是谁？")
name = input()
print("好的,马上联系乔总,你是%s" % name )
# ================ #
name = input("请告诉我你是谁")
print("好的我知道了，你是%s"%name)

num = input("你的支付宝密码是：")
print("你的密码类型是：",type(num))

user_name = input("姓名：")
user_type = input("车子：")
print(f"您好,{user_name}欢迎尊贵的{user_type}车主,欢迎您")

result = 10>5
print(f"结果是:{result},类型是:{type(result)}")

result = "itcast" == "ithima"
print(f"结果是{result},类型是{type(result)}")

age = 10
print(f"今年我已经{age}岁了")
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")


print("时间过得真快")

print("欢迎来到黑马儿童游乐场,儿童免费,成人收费")
age = input("请输入你的年龄:")
age = int(age)                               #input 输入的是 字符串类型，要转换为数字类型 需要加一步。
if age >= 18:
    print("您已成年,游玩需要补票10元")

print("祝您游玩愉快") 

print("欢迎来到黑马儿童游乐场,儿童免费,成人收费")
age = int(input("请输入您的年龄"))
if age >= 18:
    print("您已成年，如需游玩，请补票10元")
else:
    print("您是儿童，可以免费游玩")

print("祝您游玩愉快")

print("欢迎来到黑马动物园")
length = int(input("请输入你的身高(cm):"))
if length > 120:
    print("您的身高超出120cm，游玩需要购票10元")
else:
    print("您的身高未超出120cm,可以免费游玩。")

print("祝您游玩愉快")

print("欢迎来到黑马动物园")
#height = int(input("请输入你的身高"))
#vip_level = int(input("请刷你的VIP等级"))
#day = 
if int(input("请输入你的身高"))<120:
    print("您可以免费游玩")
elif int(input("请刷你的VIP等级"))>3:
    print("您的VIP卡大于3级，可以免费游玩")
elif int (input("请输入今天的日期（1-31）")) == 1:
    print("今天是1号，可以免费游玩。")
else:
    print("不好意思，所有条件都不满足，您需要支付10元")

print("祝您玩的开心！")


print("欢迎来到猜猜我心里数字的游戏，数字范围1-10，有3次机会")

num = int(input("输入你心里的数字"))
if int(input("第一次猜")) == num:
    print("恭喜您，猜对了")
elif int(input("第二次猜")) == num:
    print("恭喜您，猜对了")
elif int(input("第三次猜")) == num:
    print("恭喜您，猜对了")
else:
    print("3次都没有猜中哦")


print("欢迎来到黑马动物园")
if int(input("请告诉我你的身高:cm")) > 120:
    print("你的身高大于120cm,不能免票，如果你的VIP等级大于3，可以免票。请告诉我你的VIP等级")
    if int(input("VIP等级")) >3:
        print("您的VIP等级大于3，可以免费游玩")
    else:
        print("您的VIP等级小于3，不能免票，请花10元购票")
else:
    print("您的身高小于120，可以免费游玩。")

age = int(input("请输入你的年龄"))
year = 2
level =3
if age >= 18:
     if age < 30:
        if int(input("入职时间")) > year:
            print("您的年龄在18-30岁之间，入职时间大于两年，可领取")
        elif int(input("请输入您的级别")) > level:
            print("您的年龄在18-30岁之间，级别大于3，可领取")
        else :
            print("您的年龄在18-30岁之间，入职时间小于2年，并且级别小于3，不可领取")
     else :
        print("您的年龄超过30，不可领取")
else :
    print("您的年龄小于18，不可领取")

import random
num = random.randint(1,10)
guess_num = int(input("请输入你猜测的数字"))

if guess_num == num:
    print("恭喜您，第一次就猜中了")
else:
    if guess_num>num:
        print("第一次猜大了")
    else:
        print("第一次猜小了")
    guess_num = int(input("请第二次输入你猜测的数字"))
    if guess_num == num:
        print("恭喜您，第二次就猜中了")
    else:
        if guess_num>num:
            print("第二次猜大了")
        else:
            print("第二次猜小了")
        guess_num = int(input("请第三次输入你猜测的数字"))
        if guess_num == num:
            print("恭喜您，第三次就猜中了")
        else:
            print("三次机会用完，你没猜中")
print(f"随机数是{num}")
import random
num = random.randint(1,10)
guess_num=int(input("请输入你要猜的数"))
if guess_num == num:
    print("恭喜你第一次就猜中了")
else:
    if guess_num>num:
        print("第一次猜大了")
    else:
        print("第一次猜小了，再猜一次")
    guess_num=int(input("第二次请输入你要猜的数"))
    if guess_num == num:
        print("第二次猜中了")
    else:
        if guess_num>num:
            print("第二次你猜大了")
        else:
            print("第二次你猜小了")
        guess_num=int(input("第三次请输入你要猜的数"))
        if guess_num == num :
            printf("恭喜您，第三次猜中了")
        else:
            print("sorry,没猜中")
print(f"随机数是{num}")"""


#2026-3-4-20:54;



#i =  1
#while i < 100:
 #   print("一百天看自己，一百天后看世界")
  #  i+=1


"""i = 1
sum = 0
while i<=100:
    print(f"i的值是{i}")
    sum = sum+i
    i+=1
print("结果是%d" %sum)


#                                while语句猜数字游戏。
#生成1-100的随机整数
import random
num = random.randint(1,100)

#让用户猜一个数
flag = True
i=0
while flag:
    i=i+1
    guess_num=int(input(f"请第{i}次输入你猜测的数字"))
    if guess_num == num:
        print(f"恭喜您第{i}次猜中了")
        flag = False
    elif guess_num>num:
        print(f"第{i}次猜大了.请在猜一次")
    else:
        print(f"第{i}次猜小了，请在猜一次")

#生成1-100的随机数
import random
num = random.randint(1,100)
flag=True
count=0
while flag:
    guess_num = int(input("输入你猜测的数"))
    count+=1
    if guess_num == num:
        print("恭喜您猜中了")
        flag = False
    else:
        if guess_num > num:
            print("你猜的数大了")
        else:
            print("你猜的数小了")
print(f"{count}次猜中结果")

#            给小美表白100天送玫瑰花            #

#外层循环
i=1
while i<=100:
    print(f"今天是第{i}天,准备找小美表白。。。。。")
    
#内层循环：
    j=1
    while j <=10:
        print(f"送给小美{j}支玫瑰花")
        j+=1
    i+=1
print(f"今天是第{i-1}天，找小美表白成功")"""

#  __________________________________________________________#


"""print("Hello ",end='')
print("World")
print("Hello\tWorld")
print("itheima\tbest")"""


#                               99乘法表                     #

"""i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={i*j}\t",end ='')
        j+=1
    i+=1
    print()


day = input("今天是星期几")
match day:
    case "1":
        print("周1")
    case "2":
        print("周2")
    case "3":
        print("周3")
    case "4":
        print("4")
    case "5":
        print("5")
    case "6"|"7":
        print("6|7")
    case _:
        print("输入错误")

count=0
name = "itheima is a brand of itcast"
for x in name:
    if x == "a":
        count+=1
print(f"{count}个a")"""
"""
#              1-num之间有多少个偶数           #

count = 0
import random
num = random.randint(1,100)
#不含num 本身
for x in range(1,num):
    if x % 2 == 0:
        count=count+1
        print(f"偶数是{x}")
print(f"1到{num}之间有{count}个偶数")
 """

#             利用for循环找小美表白，每天去送10朵玫瑰花。                #
""" i = 1
for i in range(1,101):
    print(f"今天是第{i}天，准备向小美表白。。。。")
    for j in range(1,11):
        print(f"给小美送{j}朵玫瑰花")
    if i == 100:
        print(f"第{i}天，小美接受了我的玫瑰花，同意做我女朋友了")
    else:
        print("小美说，送够100天，做你女朋友") """

#                  利用for循环打印9*9乘法表            #
"""i = 1 
for i in range(1,10):
    j = 1
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t",end='')
    print()"""

"""for i in range(1,7):
    print("语句1")
    for j in range(1,3):
        print("语句2")
        break
        print("语句3")
    print("语句4")"""
#                     给员工发工资                 #
#           员工绩效分 1-10分，低于5分不发工资
# 总的金额10000元，高于5分的发工资。
#第一种
""" money = 10000
salary = 1000

for i in range(1,21):
    import random
    score = random.randint(1,10) """


""" if score<5:
        print(f"员工{i},绩效分{score}，小于5分，不发工资，下一位")
        continue
    if money >=1000:
        money -= 1000
        print(f"员工{i},满足条件，发放工资1000，账户余额{money}元")
    else:
        print("余额不足，下个月再发工资")
        break"""
#                     给员工发工资                 #
#           员工绩效分 1-10分，低于5分不发工资
# 总的金额10000元，高于5分的发工资。
#第二种
""" import random

money = 10000
salary = 1000

for i in range(1, 21):
    if money < salary:  # 先判断余额是否足够，不够就直接终止循环
        print("余额不足。下个月再发")
        break
    score = random.randint(1, 10)
    if score >= 5:
        money -= salary
        print(f"员工{i},绩效分大于等于5分，发放工资{salary}元，余额{money}")
    else:
        print(f"员工{i}绩效分不足，不发工资，下一位")

 """

""" def add(x,y):
    return x+y
sum = add(3,4)
print(sum) """

#--------------------------------------------------------------------------------------------------5-6

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
# my_set_empty = set()
print(my_set,type(my_set))

 """
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
set3 = set1.difference(set2)       #A.difference(b)生成C，A不变，B不变，生成的C是A和B的差集
print(set1)
print(set2)
print(set3)  """

#                  集合 difference_update,消除两个集合的差集（在集合1 内，删除和集合2相同的元素，集合1改变，集合2 不变
set1 = {1,2,3,4,5,6,7,10,11}
set2 = {1,2,3,8,9}
set1.difference_update(set2)        #A.difference_update(B)改变了集合A,没有生成集合C
print(set1)
print(set2)

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

#---------------------------------------------------------------------------------------------------7-9
""" import sys
# 将 my_package 所在的父目录（python 目录）添加到 sys.path
sys.path.append(r'C:\Users\乔\Desktop\python') """
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
f.close
#第二种方法
f = open("D:/练习.txt",'r',encoding="UTF-8")
count = 0
for line in f:
    line = line.strip()  #去掉首尾的空格和换行符
    words = line.split(' ')  # 按照中间的空格分割成一个一个单词
    for word in words:
        if word == 'itheima':
            count+=1
print(count)
f.close """




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

#-------------------------------------------------------------------------------------10-13
#           10章

# import json
#把列表转换成json
""" data=[{"name":"张三","age":"18"},{"name":"李四","age":"19"},{"name":"王五","age":"20"}] 
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

data1 = {"name":"周杰伦","addr":"台北"}
json_str2 = json.dumps(data1,ensure_ascii=False)
print(json_str2) """
# 把json转换为python的数据格式
""" data = '[{"name": "张三", "age": "18"}, {"name": "李四", "age": "19"}, {"name": "王五", "age": "20"}]'#       因为是字符串所以加''
l = json.loads(data)
print(type(l))
print(l)

data1 = '{"name": "周杰伦", "addr": "台北"}'
l = json.loads(data1)
print(type(l))
print(l) """

#    ------------------------------------第10章-------------------------------#
#             pyecharts模块基础使用 全局配置
""" from pyecharts.charts import Line                                       # 从pyecharts包中的charts模块引入 Line函数  其实就是画了一个x轴一个Y轴
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
line = Line()                                                           # line =的作用 将创建好的折线图对象赋值给变量 line    这样后续就可以通过 line这个变量来操作图表
line.add_xaxis(['中国','美国','日本'])                                   #x轴
line.add_yaxis("GDP",[50,20,10])                                        #y轴
line.set_global_opts(
    title_opts = TitleOpts("全国GDP",pos_top="center",pos_left="50%"),
    legend_opts= LegendOpts(is_show =True),
    toolbox_opts= ToolboxOpts(is_show = True),
    visualmap_opts= VisualMapOpts(is_show = True)
)

line.render()                                #进行图像显示 生成浏览器可以打开的文件 """

# 2020年疫情折线图——————————————————————————————————————————————————设计
""" from pyecharts.charts import Line       #导入图表
from pyecharts.options import TitleOpts,LabelOpts                   #导入的两个类
import json
#   处理数据
us_file = open("D:/美国.txt",'r',encoding='UTF-8')
us_file_data = us_file.read()

jp_file = open("D:/日本.txt",'r',encoding='UTF-8')
jp_file_data = jp_file.read()

in_file = open("D:/印度.txt",'r',encoding='UTF-8')
in_file_data = in_file.read()
# 去掉json不合规的开头
us_file_data = us_file_data.replace("jsonp_1629344292311_69436(",'')
jp_file_data = jp_file_data.replace("jsonp_1629350871167_29498(",'')
in_file_data = in_file_data.replace("jsonp_1629350745930_63180(",'')

# 去掉json不合规的结尾
us_file_data = us_file_data[:-2]
jp_file_data = jp_file_data[:-2]
in_file_data = in_file_data[:-2]

#json转字典
us_dict = json.loads(us_file_data)
jp_dict = json.loads(jp_file_data)
in_dict = json.loads(in_file_data)

#取到trend key
us_trend_dict = us_dict['data'][0]['trend']
jp_trend_dict = jp_dict['data'][0]['trend']
in_trend_dict = in_dict['data'][0]['trend']

#取到日期，换做为x轴数据 
us_x = us_trend_dict['updateDate'][:314]#x轴公用
#取到确诊人数， 换做为y轴数据
us_y = us_trend_dict['list'][0]['data'][:314]
jp_y = jp_trend_dict['list'][0]['data'][:314]
in_y = in_trend_dict['list'][0]['data'][:314]
#x轴y轴都有了，可以创建图表了，将创建好的Line图标对象赋值给line
# 构建Line折线图表对象
line = Line()
#添加x轴数据到折线图中
line.add_xaxis(us_x)
#添加y轴数据
line.add_yaxis("美国确诊人数",us_y,label_opts=LabelOpts(is_show = False))
line.add_yaxis("日本确诊人数",jp_y,label_opts=LabelOpts(is_show = False))
line.add_yaxis("印度确诊人数",in_y,label_opts=LabelOpts(is_show = False))
#设置全局选项
line.set_global_opts(
    #标题设置
    title_opts=TitleOpts(title='2020年美日印三国确诊人数对比图',pos_left='center',pos_top='1%')
    #
)

#调用render生成图表
line.render()
#关闭
us_file.close()
jp_file.close()
in_file.close()

#如果最后要关闭文件，那么打开文件的变量只能用一次，后面更新变量
"""

#           数据可视化 ----------------------------地图
# 导入地图
""" from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
#构建地图对象
map = Map()
#引入数据       列表里面是元组
data = [
    ('北京市',99),
    ('上海市',199),
    ('广东省',299),
    ('江苏省',399),
    ('河南省',499),
    ('台湾省',1000)
]
#把数据加到地图上
map = map.add("测试地图",data,'china')

# 引入全局变量
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min':1,'max':9,'lable':'1-9','color':'#FFFAFA'},
            {'min':10,'max':99,'lable':'10-99','color':'#FFDAB9'},
            {'min':100,'max':500,'lable':'100-500','color':'#FFFF00'},
            {'min':500,'max':1000,'lable':'500-1000','color':'#FF6A6A'}
        ]

    )

)
#render1显示一下
map.render() """


#           数据可视化 ----------------------------河南省疫情地图
""" from pyecharts.charts import Map
from pyecharts.options import *
import json
#打开文件读取数据
f = open("D:/疫情.txt",'r',encoding='UTF-8')
f_data = f.read()
f.close()
# 将json转化为字典  通过json.loads()
data_dict = json.loads(f_data)
#从字典中取出省份的数据
province_data_list = data_dict['areaTree'][0]['children']
#利用循环将每个省份和确诊人数组成元组
data_list = []       #绘图要用到列表      #外面是列表，里面是元组
for province_data in province_data_list:
    # province_name = province_data['name']   #取到省份名
    # province_confirm = int(province_data['total']['confirm'])     #取到确诊人数
    # data_list.append((province_name, province_confirm))    #通过append方法，将省份名和确诊人数封装到list中
    province_name = province_data['name']
# 手动添加后缀（根据你的数据源调整）
    if province_name in ['北京', '天津', '上海', '重庆']:
        province_name += '市'
    elif province_name in ['内蒙古',  '西藏']:
        province_name += '自治区'
    elif province_name in ['新疆']:
        province_name += '维吾尔自治区'
    elif province_name in ['宁夏']:
        province_name += '回族自治区'
    elif province_name in ['广西']:
        province_name += '壮族自治区'
    else:
        province_name += '省'
    province_confirm = int(province_data['total']['confirm'])     #取到确诊人数
    data_list.append((province_name, province_confirm))
#有了列表数据以后加到地图上
#给地图一个变量，通过变量来赋予地图资源
map = Map()
map.add('各个省份确诊地图',data_list,'china')

#加到地图上以后，要引入全局变量来优化地图
map.set_global_opts(
    title_opts= TitleOpts(title='各个省份确诊人数',pos_left='center',pos_top='1%'),#添加地图标题
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min':1,'max':99,'label':'1-99人','color':'#CCFFFF'},
            {'min':100,'max':999,'label':'100-999人','color':'#FFFF99'},
            {'min':1000,'max':4999,'label':'1000-4999人','color':'#FF9966'},
            {'min':5000,'max':9999,'label':'5000-9999人','color':'#FFFF66'},
            {'min':10000,'max':99999,'label':'10000-99999人','color':'#CC3333'},
            {'min':100000,'label':'100000+人','color':'#990033'}
        ]#最小最大标签，颜色
    )# 视觉手动化，自己设置
)


#rander生成数据，用浏览器打开
map.render('全国疫情确诊地图.html') """

#      -------------------河南省疫情数据---------------------#
""" import json
from pyecharts.charts import Map
from pyecharts.options import *
f = open('D:/疫情.txt','r',encoding='UTF-8')
data = f.read()
f.close()
data_dict = json.loads(data)
#从字典中取出河南省份数据
henan_dict = data_dict["areaTree"][0]['children'][3]['children']
#建立列表组成元组[(),()]
city_data = []
#利用for循环取出各个市和确诊人数
for city_dict in henan_dict:
    city_name = city_dict['name']+'市'#市名
    city_confirm = city_dict['total']['confirm']#市确诊人数
    city_data.append((city_name,city_confirm))
city_data.append(('济源市',5))
#拿到数据进行地图    #构建地图对象
map = Map()
#有了数据以后，把数据加载到地图上
map.add("河南省疫情地图",city_data,'河南')
#设置全局选项
map.set_global_opts(
    title_opts= TitleOpts(title='各个省份确诊人数',pos_left='center',pos_top='1%'),#添加地图标题
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min':1,'max':99,'label':'1-99人','color':'#CCFFFF'},
            {'min':100,'max':999,'label':'100-999人','color':'#FFFF99'},
            {'min':1000,'max':4999,'label':'1000-4999人','color':'#FF9966'},
            {'min':5000,'max':9999,'label':'5000-9999人','color':'#FFFF66'},
            {'min':10000,'max':99999,'label':'10000-99999人','color':'#CC3333'},
            {'min':100000,'label':'100000+人','color':'#990033'}
        ]#最小最大标签，颜色
    )# 视觉手动化，自己设置
)
map.render("河南疫情地图.html") """





#捕获异常

# try:                     可能发生错误的代码

# except Exception as e:
#                            如果出现异常执行的代码


#类成员变量的方法

""" class Student:
    name = None                  #成员属性，

    def say_hi1(self):
        print(f"我是{self.name}")
    def say_hi2(self,msg):                        #成员方法，要调用成员属性需要加上self
        print(f"我是{self.name},{msg}")
    
stu1 = Student()
stu1.name='周杰伦'
stu1.say_hi1()
stu1.say_hi2('我看好你哟')

 """
#面向对象的编程
#创建好类，由类创建无数个对象，由对象去完成，这就是面向对象的编程思想

""" class Clock():
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000) """
#第一个是频率，第二个数字是秒数 3000毫秒=3秒

#创建好类以后，面向对象的编程就开始了。 
""" clock1 = Clock()
clock1.id = '100001'
clock1.price = 21.99
print(f'闹钟的序列是{clock1.id}，闹钟的价格是{clock1.price}')
clock1.ring() """


# __init__()        构造方法，自动执行

""" class Student():

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("类的构造方法创建好了")

stu = Student('周杰伦',31,18500006666)
print(stu.name)
print(stu.tel)
print(stu.age)
 """

#练习案例

""" class Student:
    
    def __init__(self,name,age,adrs,count):
        self.name = name
        self.age = age
        self.adrs =adrs
        self.count = count
        print(f'学生{count}信息录入完成，信息为【学生姓名："{self.name}",年龄{self.age},地址{self.adrs}')

for count in range(1,11):
    print(f"当前录入第{count}位学生信息，总共需录入10位学生信息")
    name = input("请输入学生姓名")
    age = input("请输入学生年龄")
    adrs = input("请输入学生地址")
    stu = Student(name,age,adrs,count)           #在创建类对象的时候会自动执行__init__方法的
#                                                将参数传递给__init__使用
    
 """


#             魔术方法         python内置方法             __str__  ,__lt__,  __le__  , __eq__
#        __str__   字符串方法
""" 
class Student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student类的对象名称，name = {self.name},age = {self.age}"
stu = Student('周杰轮',35)
print(stu)
print(str(stu)) """

#      __lt__小于符号比较方法    通过__lt__可以比较两个类对象的大小

""" class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __lt__(self,other):
        return self.age<other.age

stu1 = Student('周杰轮',35)
stu2 = Student('林俊杰',38)
print(stu1>stu2)
print(stu1<stu2)
 """

#         __le__  小于等于或大于等于

""" class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __le__(self,other):
        return self.age<=other.age
    
stu1 = Student('周杰轮',35)
stu2 = Student('林俊杰',38)
print(stu1>=stu2)
print(stu1<=stu2)
 """

#          __eq__  用来比较相等的判断的

""" class  Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self,other):
        return self.age==other.age
    
stu1 = Student('周杰轮',31)
stu2 = Student("林俊杰",31)
print(stu1 == stu2)
 """

#            私有成员变量和私有成员的方法，都是没有办法调用的

""" class Phone:
    __current__voltage = None

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

phone = Phone()
phone.__keep_single_core()
phone.__current__voltage = 35.3
 """
#--------------------------封装，所谓封装就是把现实世界中的事物封装成程序中的属性和方法             


#                 对于私有的成员变量和成员方法 ，类的对象无法调用，但可以在类里面调用
#                 私有的只可以自己使用，如果到了类对象那里，不可以调用

""" class Phone:

    __current__voltage  = 1.0


    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):                     #定义了一个成员方法，在这个成员方法里可以调用私有的成员变量和成员方法
        if self.__current__voltage>=1:
            print("可以进行5G通话")
        else:
            print("电量不足，无法进行5G通话")
            self.__keep_single_core()

phone = Phone()
phone.call_by_5g() """

#     ----------------------------------练习，设计带有私有成员的手机

""" class Phone:
    #私有成员变量
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5g开启")
        else:
            print("5g关闭，使用4G网络")
    
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()

phone.call_by_5g() """

#  -------------------------继承  class类（父类）

""" class Phone:
    IMEI = None
    product = 'heima'

    def call_by_4g(self):
        print("使用4G通话") """

#继承一下

""" class Phone2022(Phone):             #这就是继承
    Face_id = '1001'

    def call_by_5g(self):
       print("现在是2022年可以进行5G通话和面部识别功能了")

phone  = Phone2022()
phone.call_by_4g()
print(phone.product)
phone.call_by_5g() """

#-----------------------多继承 也就是有多个父亲
#class phone2022(phone,Phone2022,....)

""" class NFCReader:
    nfc_type = '第五代'
    producer = 'HM'

    def read_care(self):
        print("NFC读卡")
    
    def write_care(self):
        print("NFC写卡")


class RemoteControl:
    re_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

    

class myphone(Phone,NFCReader,RemoteControl):
    pass

phone = myphone()
phone.call_by_4g()
phone.read_care()
phone.write_care()
phone.control() """

#复写父类成员和调用父类成员
#复写父类成员
""" class Phone:
    IEMA = '10001'
    producer = 'itcast'

    def call_by_5g(self):
        print("使用5G通话")

 """
""" class myphone(Phone):

    producer = 'itheima'

    def call_by_5g(self):
        print("在打电话时，开启单核性能模式，省电")
        print("使用5G通话")
        print("通话结束后恢复双核模式")

phone = myphone()
phone.call_by_5g()
print(phone.producer) """

""" class myphone(Phone):

    producer = 'itheima'

    def call_by_5g(self):
        print("在打电话时，开启单核性能模式，省电")
        #方式1
        print(Phone.producer)
        Phone.call_by_5g(self) 

        #方式2
        print(f"父类的厂商是{super().producer}")
        super().call_by_5g()
        print("通话结束后恢复双核模式")
phone = myphone()
phone.call_by_5g()
print(phone.producer) 
"""


#变量的类型注解：      只是建议性的，不是决定性的


# var1 : int = 10


#容器类型的详细注解

""" my_list : list[int] = [1,2,3]
my_dict : dict[str,int] = {'itheima',666}
my_tuple : tuple[int,str,bool] = (666,'itheima',True)
#在注释中进行类型注解
import random

var1 = random.randint(1,10)  #type: int """


#函数和方法类型注解           形参和返回值

""" def func(data:list):          #因为data:list所以下面data.就会出现append
    data.append

def add(x:int,y:int):
    return x+y

add(5,10)

def func(data:list)->list:
    return data """


#union 类型注解

""" my_list :list[int] = [1,2,3]
my_dict :dict[str,int] = {'age':10,'num':3}

from typing import Union

my_list : list[Union[str,int]] = [ 1,2,'itheima','itcast']
my_dict : dict[Union[str,int]] = {'age':13,'num':3}


def func(data:Union[str,int]) ->Union[str,int]:
    pass

func() """

#多态     多种状态，完成某个行为时，使用不同的对象会得到不同的状态
""" 
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

 """

#抽象类

""" class AC:

    def cool_wind(self):
        # 制冷 
        pass
    def hot_wind(self):
        # 制热 
        pass   
    def swing_l_r(self):
    #    左右摆风 
        pass

class Midea_AC(AC):

    def cool_wind(self):
        print("美的空调制冷")
    def hot_Wind(self):
        print("美的空调制热")
    def swing_l_r(self):
        print('美的空调左右摆风')

class GREE_AC(AC):

    def cool_wind(self):
        print("格力空调制冷")
    def hot_Wind(self):
        print("格力空调制热")
    def swing_l_r(self):
        print('格力空调左右摆风')

def make_cool(ac:AC):
    ac.cool_wind()

midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac) """

#MY sql

""" from pymysql import Connection

conn = Connection(
    host = 'localhost',  #主机名
    port = 3306 ,     #端口
    user = 'root',   #账户
    password = '8055241013'   #密码

)
# print(conn.get_server_info())
cursor = conn.cursor() #获取游标对象

conn.select_db("test")  #选择数据库

cursor.execute("create table test_pymysql(id int)")

conn.close()
 """
""" 
from pymysql import Connection

conn = Connection(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '8055241013',
    autocommit= True   #自动确认
)

#获取游标
cursor = conn.cursor()
#选择数据库
conn.select_db("world")
#使用游标对象，执行sql
# cursor.execute("insert into student values(6,'周杰轮他哥',31)")
cursor.execute("select * from student")
#conn.commit()
results = cursor.fetchall()
for r in results:
    print(r)
conn.close() """