#  梯度下降公式：  w1 = w0 - lr*grad(梯度值) 
# 导包
import torch


if __name__ == '__main__':
    #1创建张量  requires_grad为：是否自动计算梯度   dtype=torch.float32必须设置为float类型
    w0 = torch.tensor(10,requires_grad=True,dtype=torch.float32)
    print(w0)
    #自定义损失函数
    loss = 2*w0**2
    #进行反向传播 bp算法
    loss.sum().backward()
    #创建学习率
    lr = 0.1
    w1 =w0.data - lr*w0.grad
    print(w1)