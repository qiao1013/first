import torch
import numpy as np


#              张量和标量计算
""" torch.manual_seed(325)
t1 = torch.randint(low=-3,high=5,size=(3,4))
print(t1)
t2 = t1+10
t3 = t1*10
print(f'张量的加法\n{t2}')
print(f'张量的乘法\n{t3}') """

#add sub  mul div neg
#加  减   乘   除   取-1
""" t2_ = t1.add(10)
t3_ = t1.mul(10)
t4_ = t1.neg()
print(f'张量的加法\n{t2_}')
print(f'张量的乘法\n{t3_}')
print(f'张量的取负数\n{t4_}')

 """
#add_ sub_  mul_ div_ neg_   带下划线的原始数据会受到影响
""" t1.add_(20)
print(t1) """


#2       张量的点乘  就是1*5   2*6 3*7  4*8
""" A = torch.tensor(data=[[1,2],[3,4]])
B = torch.tensor(data=[[5,6],[7,8]])
result = A*B
#另外一个写法result = A.mul(B)
print(A)
print(B)
print(result) """

#3张量的矩阵乘法运算        matmul 矩阵的英文matrix  乘法的英文multi
""" torch.manual_seed(325)
A = torch.randint(low=1,high=5,size=(2,3))
B = torch.randint(low=3,high=6,size=(3,3))
# result = A@B
#第二种写法
result = A.matmul(B)
print(f'A的张量是\n{A}')
print(f'B的张量是\n{B}')
print(f'矩阵相乘的结果是\n{result}') """