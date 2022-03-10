import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import data
from sklearn import svm
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC


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

    plt.scatter(x_Y0, y_Y0, c='b', label='Negative')
    plt.scatter(x_Y1, y_Y1, c='r', marker='x', label='Positive')
    plt.xlabel('feature1')
    plt.ylabel('feature2')
    return plt


# 法二：利用等高线绘制决策边界
def plot_decision_boundary(svc, x1min, x1max, x2min, x2max, ax):
    #     x1 = np.arange(x1min, x1max, 0.001)
    #     x2 = np.arange(x2min, x2max, 0.001)
    x1 = np.linspace(x1min, x1max, 1000)
    x2 = np.linspace(x2min, x2max, 1000)

    x1, x2 = np.meshgrid(x1, x2)
    y_pred = np.array([svc.predict(np.vstack((a, b)).T) for (a, b) in zip(x1, x2)])

    ax.contour(x1, x2, y_pred, colors='r', linewidths=5)


if __name__ == '__main__':
    X, Y, train_data = init_data('data2.txt')
    plt = draw_data(train_data)
    plt.title('svm')
    x1 = train_data[:, 1]
    x2 = train_data[:, 2]
    svc2 = svm.SVC(C=100, gamma=10, probability=True)

    svc2.fit(X, Y)
    svc2.score(X, Y)

    fig, ax = plt.subplots(figsize=(12, 8))

    plot_decision_boundary(svc2, 0, 1, 0.4, 1, ax)

    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.legend()
    plt.show()

    # 10秒


