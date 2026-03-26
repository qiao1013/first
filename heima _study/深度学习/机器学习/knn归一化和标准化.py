from sklearn.preprocessing import MinMaxScaler#归一化
from sklearn.preprocessing import StandardScaler#标准化

# 一、归一化
# 2准备数据
x_train = [
    [90,2,10,40],
    [60,4,15,45],
    [75,3,13,46]
]
#3在模型训练特征之前进行规范化操作
#3.1创建归一化模型
mm_model = MinMaxScaler()
#3.1规范化数据
new_x_train = mm_model.fit_transform(x_train)#训练并转化
print(new_x_train)

#----------------------------------------------------------
#二、标准化
sm_model = StandardScaler()
new_sm_model = sm_model.fit_transform(x_train)
print(new_sm_model) 