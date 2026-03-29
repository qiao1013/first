#搭建基础神经网络的步骤：
"""
  1、定义一个类，用来继承torch.nn.Moudle
  2、实现的两个方法：
    2.1、__init__ 初始化方法：实现步骤
        a、初始化父类
        b、设置属性值
        c、定义神经网络结构，隐藏层几层，输出层是怎样的
        d、参数初始化，w,b如何进行初始化
    2.2、forward:前向传播 将样本数据送到模型训练中进行训练
"""
#导包
import torch.nn as nn
import torch
from torchsummary import summary
class Module(nn.Module):
    def __init__(self):
        # a、初始化父类
        super().__init__()
        # b、设置属性值[没有可以不写]
        # c、定义神经网络结构，隐藏层几层，输出层是怎样的
        #第一层隐藏层：上一层in_features=3,本层out_features=3
        self.linear1 = nn.Linear(in_features=3,out_features=3)
        #第二层隐藏层：
        self.linear2 = nn.Linear(in_features=3,out_features=2)
        #输出层：
        self.out = nn.Linear(in_features=2,out_features=2)
        # d、参数初始化，w,b如何进行初始化
        #第一层初始化：
        nn.init.xavier_normal_(self.linear1.weight)#对w进行初始化【用泽维尔xavier】
        nn.init.zeros_(self.linear1.bias)#对b进行初始化【全0】
        #第二层初始化：
        nn.init.kaiming_normal_(self.linear2.weight)
        nn.init.zeros_(self.linear2.bias)
        #输出层初始化：[一般不用自己写]
    def forward(self,data):
        #1数据经过第一层隐藏层：
        """ #1.1 分开版
        #线性求和
        linear1_result = self.linear1(data)
        #激活函数得到激活值
        data = torch.sigmoid(linear1_result) """
        #1.2合并版：[推荐]
        data = torch.sigmoid(self.linear1(data))
        #2数据经过第二层隐藏层：
        data = torch.relu(self.linear2(data))
        #3数据经过输出层：
        return torch.softmax(self.out(data),dim=-1)
    
if __name__ == '__main__':
    data = torch.randn(10,3)#10条随机数据，每条数据里面有3个特征值
    my_module = Module()


    output = my_module(data)
    print(f'预测结果是：{output}')
    print(f'预测结果形状：{output.shape}')

    print('-'*30)


    #查看神经网络的概要信息

    summary(my_module,(3,),2)
