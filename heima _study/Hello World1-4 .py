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

def add(x,y):
    return x+y
sum = add(3,4)
print(sum)


 




