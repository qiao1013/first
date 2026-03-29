#导包
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
#1.准备数据（特征2，标签）
x, y = make_blobs(
    n_samples=1000,
    n_features=2,
    cluster_std=[0.4,0.2,0.2,0.3],
    centers=[[-1,-1],[0,0],[1,1],[2,2]]
)
print(x.shape)
print(y.shape)

#2.提前绘制散点图看看数据据分布
# plt.scatter(x[:,0],x[:,1])
# plt.show()

# 3使用模型
#创建模型
model = KMeans(n_clusters=3)
y_pred = model.fit_predict(x)
#4按照预测值通过颜色划分类别：绘制散点图看看数据据分布

plt.scatter(x[:,0],x[:,1],c=y_pred)
plt.show()