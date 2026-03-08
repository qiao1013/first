#案例-----------------------------------------------------
# 升级版自动查核酸

""" def test(num):
    print('欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！体温测量中，您的体温是：',end='')
    if num<=37.5:
        print(f'{num}，体温正常请进')
    else:
        print(f'{num},需要隔离')

test(37.6) """

#案例 -------------------------------------------------------
# 黑马ATM

""" #全局变量
name = input("输入姓名")
money = 5000000
choice = None
import time
#查询余额效果
def balance():
    print("-------------查询余额-----------")
    print(f'{name},您好，您的余额剩余:{money}元')
#存款效果
def deposit():
    print("-------------存款-------------")
    num1 = int(input("请输入您存款的金额"))
    print(f'{name},您好，您存款:{num1}元成功')
    global money
    money += num1
    print(f"{name},您好，您的余额剩余：{money}元")
#取款效果
def withdrawal():
    print("-------------取款-------------")
    num2 = int(input("请输入您取款的金额"))
    global money
    if num2>money:
        print("您的余额不足")
    else:
        print(f'{name},您好，您取款:{num2}元成功')
        money -= num2
        print(f"{name},您好，您的余额剩余：{money}元")
        print('操作成功，3秒后返回主菜单')
        time.sleep(3)
# 主菜单效果
def menu():
    print("-------------主菜单-------------")
    print(f"{name},您好，欢迎来到黑马银行ATM，请选择操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择")
 
while True:
    choice = menu()
    if choice == '1':
        balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdrawal()
    elif choice == '4':
        break
    else:
        print("输入错误,重新输入")
         """


# 案例 -----------------------------------------------
#1列表
""" age_list = [21,25,21,23,22,20]
age_list.append(31)
age_list2 = [29,33,30]
age_list.extend(age_list2)
age_list.remove(21)                     #remove只修改原来的列表，没有返回新列表
age_list.remove(30)
print(age_list.index(31))



 """
#2字符串

""" my_str = 'itheima itcast boxuegu'
# print(my_str.count('it'))
# print(my_str.replace(' ','|'))
my_str = my_str.replace(' ','|')
print(my_str.split("|"))                 #字符串分割会得到列表
 """

#3序列的切片实践
""" 
my_str = '万过薪月,员序程马黑来,nohtyp学'
#1
my_str1= my_str[-10:-15:-1]
print(my_str1) 

#2
my_str = my_str.replace('来','')
my_list = my_str.split(',')         #字符串分割会得到列表
my_str1 = str(my_list[1])
print(my_str1[::-1])

 """

# ------------------------------------------------------------
#信息去重


# 集合        可以去重
# 空set()
# my_set=set()
""" my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']

my_set = set()
for my_str in my_list:
    my_set.add(my_str)
print(type(my_set))
 """


#-------------------------------------------------------------------
#字典
     #         {}里面的是value也是嵌套的字典，
     #{ 'key':{key:value}}
#案例   升职加薪

""" my_dict ={'王力宏':
          {'部门':'科技部',
           '工资':3000,
           '级别':1},
          '周杰伦':
          {'部门':'市场部',
           '工资':5000,
           '级别':2},
          '林俊杰':
          {'部门':'市场部',
           '工资':7000,
           '级别':3},
          '张学友':
          {'部门':'科技部',
           '工资':4000,
           '级别':1},
          '刘德华':
          {'部门':'市场部',
           '工资':6000,
           '级别':2}
          }
#通过for循环找到KEY对应的value就出来了
for name in my_dict:
    if my_dict[name]['级别']==1:
        # my_dict[name]['级别']= my_dict[name]['级别']=2      这是无效语法里面有两个==号
        employee_name = my_dict[name]
        employee_name['级别'] = 2
        my_dict[name]['工资'] += 1000
        # my_dict[name] = employee_name   沉余操作

print(my_dict)  """

#bill账单  去掉测试的这一行

""" fr = open('D:/bill.txt','r',encoding='UTF-8')
fw = open('D:/bill.txt.bak','w',encoding='UTF-8')

for line in fr:
    line = line.strip()
    if line.split(',')[4] =='测试':
        continue
    fw.write(line)
    fw.write('\n')

print(fw)
print(fr)

fr.close()
fw.close()
 """

#单词计数

""" fr = open('D:/word.txt','r',encoding='UTF-8')
my_str = fr.read()
count = my_str.count('itheima')
print(count) """