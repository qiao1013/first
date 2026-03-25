# sum   dim - dimension维度
import torch
t1 = torch.tensor([[1,2,3],[4,5,6]],dtype=torch.float)
# print(t1)
t1_ = t1.sum()
print(t1_)#sum里面不添加数的话，就是1+2+3+4+5+6=21
t2 = t1.sum(dim=0)#按照第一个维度计算，就是竖着加，1+4  2+5  3+6
t3 = t1.sum(dim=1)#按照第二个维度计算，就是横着加， 1+2+3   4+5+6
t4 = t1.sum(dim=-1)#按照最后一个维度计算，
print(t2)
print(t3)
print(t4)
