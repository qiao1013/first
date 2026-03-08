#sklearn框架


#KNN实现分类任务
 #导包
from sklearn.neighbors import KNeighborsClassifier  #K近邻算法

#2 准备数据（模拟数据） x_train x_test y_train y_test
#模拟特征数据
x_train = [[0],[1],[2],[3]] #一个中括号代表一行，四个中括号代表4行，一个小中括号里面有俩就代表又两列
x_test = [[4]]
#模拟标签数据
y_train = [0,0,0,1]  #假设  1：垃圾邮件   0：正常邮件
#3预测x_test属于垃圾邮件还是正常邮件
#3.1创建分类模型
knn_model = KNeighborsClassifier(n_neighbors=3)
#3.2模型训练 fit代表训练
knn_model.fit(x_train,y_train)
#3.3模型预测
y_pred = knn_model.predict(x_test)
#3.4打印预测结果
print(y_pred)#因为分类中离4最近的3个距离是321，21都是0类型，3自己是1类型，所以把4归到0类型里面去



