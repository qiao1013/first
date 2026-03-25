import torch

#创建权重值
w0 = torch.tensor(data=20,requires_grad=True,dtype=torch.float32)

#进行多次的梯度更新
epochs=100


for epoch in range(epochs):
    
    #创建损失函数
    loss = 2*w0**2
    #因为梯度值会累加，所以判断清零
    if w0.grad is not None:
        w0.grad.zero_()

    #进行反向传播累加  意义是： 计算d(loss)/d(w0)  把这个结果存到w0.grad
    loss.sum().backward()

    #设置学习率
    old_w0 = w0.data
    lr = 0.01
    w0.data = w0.data - lr*w0.grad
    print(f'第{epoch+1}次计算，原始的权重值{old_w0}，更新后的权重值{w0.data}')