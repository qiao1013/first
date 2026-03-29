#1 导包
#数据处理用的包
import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import TensorDataset
import numpy as np
from sklearn.preprocessing import StandardScaler
#自定义网络结构用的包
import torch.nn as nn

#模型训练用的包
from torch.utils.data import DataLoader #Dataloder就是数据加载器
#2数据处理：文件->DataFrame->Tensor->Dataset->Dataloader
def create_dataset():
    #1 读取文件
    df = pd.read_csv(r'D:\BaiduNetdiskDownload\黑马课程\dd-狂野mac window\源码 课件资料\阶段4 深度学习\2月1日-深度学习\06-数据集\手机价格预测.csv',encoding='UTF-8')

    #2 拆分特征数据得到目标值
    x = df.iloc[:,:-1]#DataFrame只要iloc取的是多列就返回DataFrame类型
    y = df.iloc[:,-1]#series，series.values才是ndarray

    #3 划分训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=201)
    
    #特征预处理，要量纲统一，因为电池大多都是4000毫安，而其他数据则是100以内的数字，模型只认数字，而量纲统一，刚好把他们消除了，变成相对大小
    transformer = StandardScaler()
    x_train = transformer.fit_transform(x_train)#StandardScaler.fit_transform返回值永远是ndarray
    x_test = transformer.transform(x_test)
    #4 DataFrame->Tensor
    #index  只取索引
    #values 只取值
    x_train = torch.tensor(x_train,dtype=torch.float32)
    x_test = torch.tensor(x_test,dtype=torch.float32)
    #values只取内容，字段名称不需要
    y_train = torch.tensor(y_train.values,dtype=torch.int64)
    y_test = torch.tensor(y_test.values,dtype=torch.int64)

    #5 Tensor->Dataset，tensordataset是一个“把多个tensor按样本对其打包"的容器
    #**打包是为了把“一个样本的 x 和 y”绑定在一起，组成一个样本
    # 让 PyTorch 在 shuffle、batch、并行加载时永远不出错。
    train_dataset = TensorDataset(x_train,y_train)
    test_dataset = TensorDataset(x_test,y_test)

    #6 其他数据信息
    #6.1获得特征个数
    #x.shape[0]    样本数量
    #x.shape[1]    特征数量
    feature_nums = x.shape[1]
    #6.2获得目标值个数 只要获得1234，所以要去重
    target_nums = len(np.unique(y.values))

    return train_dataset,test_dataset,feature_nums,target_nums

#3 自定义网络结构
class module(nn.Module):

    #a继承父类
    #b设置属性
    #c设置隐藏层多少层，输出层是什么样的
    #d参数初始化，w和b
    def __init__(self,feature_nums,target_nums):
        #继承父类的基本属性
        super().__init__()
        #设置属性
        self.feature_nums = feature_nums
        self.target_nums = target_nums

        #设置隐藏层第一层
        self.linear1 = nn.Linear(in_features=self.feature_nums,out_features=512)
        #设置隐藏层第二层
        self.linear2 = nn.Linear(in_features=512,out_features=256)
        #设置输出层
        self.out = nn.Linear(in_features=256,out_features=self.target_nums)
    #定义前向传播，预测模型的
    def forward(self,data):
        #线性求和，激活函数
        #第一层
        data = torch.relu(self.linear1(data))
        #第二层
        data = torch.relu(self.linear2(data))
        #输出层   因为要调用CrossEntropyLoss，里面有softmax，
        return self.out(data)

#4 模型训练
def train_model(train_dataset,feature_nums,target_nums):
    #1得到数据加载器，Dataset->Dataloader 为了防止内存溢出
    torch.manual_seed(201)#设置随机数种子，让数据的划分固定下来
    #dataset:数据集合
    # batch_size是同一时刻送入到神经网络中的样本条数
    # shuffle 是数据打散，随机抽牌
    dataloader = DataLoader(dataset=train_dataset,batch_size=8,shuffle=True)

    #2创建网络模型实例对象
    model = module(feature_nums,target_nums)
    #3创建损失函数对象  #多分类问题需要使用交叉熵函数
    loss = nn.CrossEntropyLoss()
    #4创建优化器对象
    """ 
     SGD随机梯度下降法：每次随机选一条样本计算梯度值
     params:告诉梯度下降算法要帮我对什么参数进行优化（梯度下降）这里就是w和b
       """
    # optimzer = torch.optim.SGD(params=model.parameters(),lr=1e-3)
    optimzer = torch.optim.Adam(params=model.parameters(),lr=1e-3,betas=(0.9,0.99))
    #循环训练  假设总样本条数100，每个批次中有8条样本，一个轮次中则有13个批次
    epochs = 50#对总样本，总共训练多少个轮次
    #开启Dropout随机失活开关
    model.train()#进入模型训练模式，也就是允许神经网络随机失活
    for epoch in range(epochs):
        #外层循环控制轮次

        #记录损失值的变化过程 ：也就是计算平均损失total_loss_value/total_sample_num
        total_loss_value = 0.0#每个轮次中总的损失值
        total_sample_num = 0 #每个轮次中已经训练的样本条数
        for x,y in dataloader:
            #5.1内层循环控制批次
            #x是样本中的特殊数据，y是样本中的真实值
            #前向传播
            pred_y = model(x)
            #5.2计算损失值
            loss_values = loss(pred_y,y)
            #更新损失值
            total_loss_value =total_loss_value+loss_values.item()#item把张量变标量
            total_sample_num = total_sample_num+len(x)

            #5.3固定代码
            #梯度清零 ：默认会对梯度值进行累计
            optimzer.zero_grad()
            #反向传播   只有标量张量能进行反向传播
            loss_values.sum().backward()
            #更新参数
            optimzer.step()
        print(f'第{epoch+1}次，总的平均损失是{total_loss_value/total_sample_num}')
    
    #6保存训练好的模型
    #写到磁盘中保存参数w和b
    torch.save(model.state_dict(),'phone_price_model.pkl')

#5 模型预测  模型训练的简化版：
def predict_model(test_dataset,feature_nums,target_nums):
    #5.1创建数据加载器：
    #模型预测的时候shuffle要设置为False,不让数据打散，为了预测结果稳定
    dataloder = DataLoader(dataset=test_dataset,batch_size=8,shuffle=False)
    #5.2创建算法模型
    model = module(feature_nums,target_nums)
    #5.3加载训练好的模型
    model.load_state_dict(torch.load('phone_price_model.pkl'))
    #5.4预测
    model.eval() #切换为预测模式，禁止随即失活
    correct_cnt = 0
    for x,y in dataloder:
        # 5.4.1-前向传播预测
        pred_y = model(x)
        # 5.4.2获得预测值概率高的索引，实际是获得预测目标值的类别
        pred_id = torch.argmax(pred_y,dim =-1)
        #5.4.3统计预测正确的条数
        correct_cnt +=(pred_id==y).sum()
    #6计算准确率
    acc_rate = correct_cnt/len(test_dataset)
    print(f'预测的准确率是：{acc_rate},预测正确的样本条数{correct_cnt},预测的总样本条数{len(test_dataset)}')


if __name__ == '__main__':
    train_dataset,test_dataset,feature_nums,target_nums = create_dataset()
    # print(f'训练集数据：{train_dataset}')
    # print(f'测试集数据：{test_dataset}')
    # print(f"特征个数：{feature_nums}")
    # print(f'目标值个数：{target_nums}')


    train_model(train_dataset,feature_nums,target_nums)
    predict_model(test_dataset,feature_nums,target_nums)