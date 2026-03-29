""" #下面的导包会报错，从错误内容中获取数据代码
# from sklearn.datasets import load_boston


#1 准备数据
# 1.1 原始数据
import pandas as pd
import numpy as np
data_url = "http://lib.stat.cmu.edu/datasets/boston"    
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
# print(f'特征是{data}')
# print(f'标签是{target}')



#从sklearn模型选择中导入训练集测试集预测集的包
from sklearn.model_selection import train_test_split
#用的是标准化，而不是归一化，因为归一化受异常值影响比较多
from sklearn.preprocessing import StandardScaler
#梯度下降
from sklearn.linear_model import SGDRegressor,LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,root_mean_squared_error


# 1.2 数据切割   划分数据集
X_train, X_test, y_train, y_test = train_test_split(data,target,test_size=0.2,train_size=0.8)
# 1.3特征标准化处理
ss = StandardScaler()
new_x_train = ss.fit_transform(X_train)#训练集用fit_transform()训练并转换
new_x_test = ss.transform(X_test)#测试集只能用transform()转换，因为训练集已经训练了模型并计算了相关内容
# 2准备模型
#一个正规方程或者梯度下降
#invscaling动态调整学习率
#  梯度下降
model = SGDRegressor(loss="squared_error", learning_rate="invscaling",eta0=0.01)
# 线性方程
# model = LinearRegression()

# 3模型训练
model.fit(new_x_train,y_train)
print(f'训练后k参数{model.coef_}')
print(f'训练后b参数{model.intercept_}')

#4模型预测
y_pred = model.predict(new_x_test)

#5模型评估
print(f"平均绝对误差：{mean_absolute_error(y_test,y_pred)}")
print(f"平均平方误差：{mean_squared_error(y_test,y_pred)}")
print(f"均方根误差：{root_mean_squared_error(y_test,y_pred)}") """
