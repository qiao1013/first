import torch
import numpy as np
#1张量转numpy       默认共享内存
""" t1 = torch.tensor([11,22,33])
arr1 = t1.numpy()
print(t1)
print(arr1)
#copy不共享内存
arr1 = t1.numpy().copy()
t1[1]=999
print(t1)
print(arr1)
 """
#2numpy转张量
""" arr2 = np.array([11,22,33])
# print(type(arr2))
t2 = torch.from_numpy(arr2)
# print(type(t2))
#不会共享内存 torch.tensor(numpy)
t3 = torch.tensor(arr2)
arr2[1]=666
print(t3)
print(arr2)
 """
#3标量转张量    
""" t4 = torch.tensor(data=999)
print(t4) """

#4张量转标量
""" result = t4.item()
print(result)
print(type(result)) """