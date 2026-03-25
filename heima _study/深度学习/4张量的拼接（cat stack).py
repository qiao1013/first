#cat  concat   stack


#1创建数据
import torch
torch.manual_seed(333)
""" t1 = torch.randint(low=1,high=10,size=(2,3))
t2 = torch.randint(low=1,high=10,size=(2,3))
print(t1)
print(t2)
 """
#2     cat 进行拼接
#2.1   0维度进行拼接。组成了4行3列，   竖着连接起来
""" t3 = torch.cat(tensors=[t1,t2],dim=0)
print(t3) """

#2.2    1维度进行拼接   组成了2行6列， 横着连接起来
""" t4 = torch.cat([t1,t2],dim=1)
print(t4) """


#2.3       除了拼接的维度以外，其他维度必须相同
""" t3 = torch.randint(low=1,high=10,size=(2,3))
t4 = torch.randint(low=1,high=10,size=(2,5))
# print(t3)
# print(t4)
# t3_ = torch.cat([t3,t4],dim=0)#0维度时   列必须相同，行可以不同
# print(t3_)
t4_ = torch.cat([t3,t4],dim=1)#1维度时   行必须相同， 列可以不同
print(t4_)
 """

#3       stack进行拼接  行数列数必须相同才能进行拼接