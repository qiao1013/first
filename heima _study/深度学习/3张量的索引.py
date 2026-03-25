import torch
#张量的索引操作，类似python列表中的操作
""" torch.manual_seed(325)
t1 = torch.randint(low=1,high=10,size=(3,4))
# print(t1)
#拿到第一行
t2 = t1[0]
print(t2)
#拿到第一列
t3 = t1[:,0]
print(t3)

#拿到第二行
t4 = t1[1]
print(t4)

#拿到第二列
t5 = t1[:,1]
print(t5) """

#张量的索引之  范围索引
""" torch.manual_seed(325)
t1 = torch.randint(low=1,high=9,size=(4,5))
print(t1)

# t2 = t1[1:3,1:3]    #从第一行开始，到第二行结束，左闭右开   ，从第一列开始到第二列结束，左闭右开
# print(t2)

#前两行，前3列的数据
t2 = t1[:2,:3]
print(t2) """
