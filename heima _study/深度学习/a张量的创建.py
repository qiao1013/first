import torch
import numpy as np


""" #创建张量
#1基础创建
#1.1 - 创建标量   #把普通的基本类型封装为了张量
t1 = torch.tensor(data=999)
print(t1)

#1.2  -numpy 中的ndarray数组创建张量
arr1 = np.random.randn(2,3)#创建2行3列数组
t2 = torch.tensor(data=arr1)   #float64: 64位的小数
print(t2)

#1.3 通过容器创建张量
t3 = torch.tensor([11,22,33])
print(t3)
t4 = torch.tensor([1.99,2.88,3.77])
print(t4)

#查看张量中的元素的数据类型
print(t1.dtype)


#2其它创建方式
t5 = torch.Tensor(5)#5代表创建5个张量类型的元素，不是把5创建为张量元素
print(t5)
print(t5.dtype)


t5 = torch.Tensor([5])#带了[]，把5变成张量
print(t5)
print(t5.dtype)


#3创建指定类型的张量
# torch.IntTensor,torch.DoubleTensor,torch.FloatTensor
# 整数类型的张量     双精度类型的张量     小数类型的张量


#2---------创建线性张量
#2.1第一种方式
t6 = torch.arange(start=1,end=6,step=1) #a表示数组，range表示范围[stard , end)是一个左闭右开的
print(t6)
#2.2第二种方式
t7 = torch.linspace(start = 1,end=6,steps=6)#[]左闭右闭，steps是生成多少个元素

#3-------创建随机的小数张量
t7 = torch.rand(4)
print(t7)
t8 = torch.randn(size=(2,3,4))
print(t8)


#4---------创建全0或1的张量 仿numpy

t9 = torch.ones(size=(3,4))
t10 = torch.ones_like(t8)

#重点掌握
t11 = torch.zeros(size=(2,3))
print(t11) """

#张量的类型转换
t_1 = torch.tensor([11,22,33])
print(t_1.dtype)
t_2 = t_1.type(dtype=torch.float16)
print(t_2.dtype)
