
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score#预测准确率
from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error
data = pd.read_csv(r'D:\BaiduNetdiskDownload\黑马课程\dd-狂野mac window\源码 课件资料\阶段3 机器学习\1月25日-机器学习\breast-cancer-wisconsin.csv',sep = ',')
# print(data.shape)#形状
# print(data.ndim)#维度 

#2数据预处理
#注意 数据中有？特殊字符，无效字符，需要先转换为numpy中的nan,然后使用dropna()删除或者fillna()填充
new_data = data.replace('?',np.nan,).dropna()#inplace是否原地修改一个原对象，而不是创建一个新对象
# print(new_data.shape,new_data.ndim)

# 3数据预处理
# 3.1从数据中获取特征和标签
#iloc格式： 数据.iloc[行索引，列索引]
x = new_data.iloc[:,1:-1]#683行9列
y = new_data.iloc[:,-1]#683行一列
# print(x.shape,x.ndim)
# print(y.shape,y.ndim)
# 3.2 使用xtrain_test_split（）按照比例切割4部分
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
# 4特征处理(标准化)
ss = StandardScaler()
new_x_train = ss.fit_transform(X_train)
new_x_test = ss.transform(X_test)

# 5创建逻辑回归模型
lr_model = LogisticRegression()

# 6训练
lr_model.fit(new_x_train,y_train)

# 7 模型预测
y_pred = lr_model.predict(new_x_test)

# 8 模型评估
print(f'准确率：{accuracy_score(y_test,y_pred)}')

# 8.2模型评估第二种方法
print(f'准确率：{lr_model.score(new_x_test,y_test)}')