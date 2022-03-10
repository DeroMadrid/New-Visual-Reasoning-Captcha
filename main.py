# 逻辑回归python实现
import numpy as np
import matplotlib.pyplot as plt


# sigmoid函数(逻辑函数),也即假设函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# 代价函数
def computeCost(X, Y, theta):
    z = X * theta.T
    # 训练数据个数,或者用m = y.shape[1]
    m = Y.size
    para1 = np.multiply(-Y, np.log(sigmoid(z)))
    para2 = np.multiply((1 - Y), np.log(1 - sigmoid(z)))
    # 代价函数Y
    J = 1 / m * np.sum(para1 - para2)
    return J


# 梯度下降
def gradientDescent(X, Y, theta, alpha, iters):
    # cost用来记录迭代每一次的代价函数值；用长度为iters的数组记录；初始化为0
    cost = np.zeros(iters)
    # 每迭代一次，就要循环更新一次所有参数的值
    for i in range(iters):
        theta = theta - (alpha / Y.size) * ((sigmoid(X * theta.T) - Y).T * X)  # 更新theta向量
        cost[i] = computeCost(X, Y, theta)
    return theta, cost


# 对训练数据预处理
def init_data(data_path):
    train_data = np.genfromtxt(data_path)  # <class 'numpy.ndarray'> 
    # 新增一列x0
    add_b = np.ones(train_data.shape[0])
    train_data = np.insert(train_data, 0, values=add_b, axis=1)
    # 提取特征矩阵
    X = train_data[:, [0, 1, 2]]
    # 提取结果向量,列向量
    Y = train_data[:, [3]]
    # print(X, type(X)) # <class 'numpy.ndarray'>
    # print(Y, type(Y)) # <class 'numpy.ndarray'>
    # 矩阵和数组的区别：https://blog.csdn.net/wyl1813240346/article/details/79806207
    # 由于会用到矩阵的乘法运算，因此最好都转化成矩阵
    X = np.mat(X)
    Y = np.mat(Y)
    return X, Y, train_data


# 预测函数
def predict(theta_min, predictX):
    probability = sigmoid(predictX * theta_min.T)
    return [1 if x >= 0.5 else 0 for x in probability]


# 绘制原始数据
def draw_data(train_data):
    # 数据可视化
    # 将Y=0和Y=1的数据分别用不同的点显示出来
    # x轴和y轴分别用Y=0和Y=1各自的feature1和feature2表示
    # 从train_data矩阵中获取Y=0的数据
    Y0 = train_data[train_data[:, 3] == 0]
    # 从train_data矩阵中获取Y=1的数据
    Y1 = train_data[train_data[:, 3] == 1]
    # 构造Y0数据的x,y轴
    x_Y0, y_Y0 = Y0[:, 1], Y0[:, 2]
    # 获取train_data矩阵第3列，作为y轴
    x_Y1, y_Y1 = Y1[:, 1], Y1[:, 2]

    plt.scatter(x_Y0, y_Y0, c='b', label='Not Admitted')
    plt.scatter(x_Y1, y_Y1, c='r', marker='x', label='Admitted')
    plt.xlabel('feature1')
    plt.ylabel('feature2')
    return plt


# 决策边界theta*x=0
def boundary(theta_min, train_data):
    x1 = np.arange(20, 110, 0.1)
    x2 = (theta_min[0, 0] + theta_min[0, 1] * x1) / (-theta_min[0, 2])
    plt = draw_data(train_data)
    plt.title('boundary')
    plt.plot(x1, x2)
    plt.show()


if __name__ == '__main__':
    # 获取数据
    X, Y, train_data = init_data('data1.txt')
    # 设置参数
    theta = np.mat(np.zeros(X.shape[1]))
    iters = 500000
    alpha = 0.1
    # 训练数据，获取theta_min
    theta_min, cost = gradientDescent(X, Y, theta, alpha, iters)
    print('最小参数theta向量:' + str(theta_min))

    # 预测数据;这里的预测数据集就采用训练数据集
    predictX = X
    res = predict(theta_min, predictX)
    # 预测准确率计算
    correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(res, Y)]
    # map()函数将correct转化为全部为int的列表
    accuracy = (sum(map(int, correct)) % len(correct))
    print('accuracy = {0}%'.format(accuracy))

    # draw_data(train_data)
    boundary(theta_min, train_data)