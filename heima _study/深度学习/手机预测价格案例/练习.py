#1导包
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import numpy as np
import torch.nn as nn

#2数据处理  文件->DataFrame->Tensor->Dataset->Dataloader
#2.1读取数据
def create_dataset():
    df = pd.read_csv(r'D:\BaiduNetdiskDownload\黑马课程\dd-狂野mac window\源码 课件资料\阶段4 深度学习\2月1日-深度学习\06-数据集\手机价格预测.csv',encoding='UTF-8')
    #2.2把数据分开
    x = df.iloc[:,:-1]#多行多列数据DF
    y = df.iloc[:,-1]#多行一列数据Series
    #2.3划分这些数据
    X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=328)
    #2.4量纲统一，标准化 要训练集是fit_transform 测试集是transform 
    ss = StandardScaler()
    x_train = ss.fit_transform(X_train)#ndarray
    x_test = ss.transform(X_test)#ndarray

    #2.5 DataFrame->Tensor  x可以直接转  ，y需要.values
    tensor_x_train = torch.tensor(x_train,dtype=torch.float32)
    tensor_x_test = torch.tensor(x_test,dtype=torch.float32)

    tensor_y_train = torch.tensor(y_train.values,dtype=torch.int64)
    tensor_y_test = torch.tensor(y_test.values,dtype=torch.int64)
    #2.6Tensor->Dataset
    train_data = TensorDataset(tensor_x_train,tensor_y_train)
    test_data = TensorDataset(tensor_x_test,tensor_y_test)
    #2.7其他数据信息 特征值目标值
    #x.shape[0]样本数量
    #x.shape[1]特征数量
    features_num = x.shape[1]
    #标签，目标值
    target_num = len(np.unique(y.values))

    return train_data,test_data,features_num,target_num
#3自定义网络结构  隐藏层多少层，输出层是怎样的
class module(nn.Module):
    def __init__(self,features_num,target_num):
        super().__init__()
        #3.1设置属性值：
        self.features_num=features_num
        self.target_num=target_num

        #3.2隐藏层第一层
        self.liner1 = nn.Linear(in_features=self.features_num,out_features=512)
        #隐藏层第二层
        self.liner2 = nn.Linear(in_features=512,out_features=256)
        #输出层
        self.out = nn.Linear(in_features=256,out_features=self.target_num)

    def forward(self,data):
        #上边是线性求和，这边是激活函数
        #第一层激活函数
        data = torch.relu(self.liner1(data))
        #第二层激活函数
        data = torch.relu(self.liner2(data))
        #输出层 下面有crossentropyloss里面自带softmax
        return self.out(data)
#4模型训练
def model_train(train_data,features_num,target_num):
     #设置随机数种子
    torch.manual_seed(328)
    #设置数据加载器，为了防止内存溢出
    dataloder = DataLoader(dataset=train_data,batch_size=8,shuffle=True)
    #创建实例化模型
    model = module(features_num,target_num)
    #损失函数
    loss = nn.CrossEntropyLoss()
    #优化器
    optimzer = torch.optim.Adam(params=model.parameters(),lr=1e-4,betas=[0.9,0.99])
    #循环
    #外层控制轮次，内层控制批次
    epochs = 50
    #进入训练模式
    model.train()
    for epoch in range(epochs):
        #设置损失值，损失量
        total_loss_num = 0.0
        total_sample_num = 0
        for x,y in dataloder:
            #预测损失值
            y_pred = model(x)
            #损失值
            loss_values = loss(y_pred,y)
            #更新损失值
            total_loss_num+=loss_values.item()
            #更新样本数量
            total_sample_num+=len(x)
            #固定代码
            #1梯度清零
            optimzer.zero_grad()
            #反向传播
            loss_values.sum().backward()
            #优化器更新
            optimzer.step()
        print(f'第{epoch+1}次，平均损失是：{total_loss_num/total_sample_num}')

    #保存
    torch.save(model.state_dict(),'phone_price_model2.pkl')


#5模型预测
def pred_model(test_data,features_num,target_num):
    #设置存储器
    dataloder = DataLoader(dataset=test_data,batch_size=8,shuffle=True)
    #创建实例化模型
    model = module(features_num,target_num)
    #把训练后的模型拿来预测
    model.load_state_dict(torch.load('phone_price_model2.pkl'))
    #预测
    model.eval()
    correct_cnt = 0
    for x,y in dataloder:
        y_pred = model(x)
        pred_id = torch.argmax(y_pred,dim=-1)
        correct_cnt+=(pred_id==y).sum()
    #计算准确率：
    acc_rate = correct_cnt/len(test_data)
    print(f'准确率：{acc_rate},预测正确的样本条数{correct_cnt},总的样本条数{len(test_data)}')



if __name__ == '__main__':
    train_data,test_data,features_num,target_num = create_dataset()
    model_train(train_data,features_num,target_num)
    pred_model(test_data,features_num,target_num)