from sklearn.linear_model import LinearRegression
#1准备数据 2 准备模型 3准备训练 4 模型预测
#准备数据
x_train = [
    [160],
    [166],
    [172],
    [174],
    [180]
]
y_train = [56.3,60.6,65.1,68.5,75]
x_test  = [[182]]
#准备模型
model = LinearRegression()
#模型训练   训练的目的是找线性规律，找出最优的K和b，找出了就能画出最优的一条线
#训练前找           找不出来
""" print(f'最优的斜率：k是{model.coef_}')
print(f'最优的b：k是{model.intercept_}') """

model.fit(x_train,y_train)

#训练后找  ，找出来了
print(f'最优的斜率：k是{model.coef_}')
print(f'最优的b：b是{model.intercept_}')

y_test = model.predict(x_test)
print(f'体重是{y_test}')