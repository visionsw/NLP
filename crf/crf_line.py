import numpy as np

# 矩阵形式
class CLineCrf:

    def __init__(self, M, x, y_list, start, stop):
        self.M = M  # 用于存储各个结点得到的矩阵
        self.Z = None  # 归一化因子
        self.MP = []  # 矩阵乘积结果
        self.start = start
        self.stop = stop
        self.features = []
        self.w = []  # 权值矩阵
        self.x = x  # 输入序列
        self.y_list = y_list  # 标签集合
        self.a = []  # 前向矩阵
        self.b = []  # 后向矩阵
        self.work()
        self.forward_algorithm()
        self.backward_algorithm()


    # n+1个矩阵相乘
    def work(self):
        print("Working.......")
        # 创建m阶矩阵，作为矩阵乘积的存储
        self.MP = np.full(shape=(np.shape(self.M[0])), fill_value=1.0)

        # 矩阵乘法作用于M
        for i in self.M:
            self.MP = np.dot(self.MP, i)

    def z_value(self):
        print(self.MP)
        return self.MP[self.y_list.index(self.start)][self.y_list.index(self.stop)]

    def forward_algorithm(self):

        a = []  # 定义前向概率矩阵,用于存储ai(x)，m维列向量
        # 初始化位置0上的向量
        a_0 = [1 if self.y_list[i] == self.start else 0 for i in range(len(self.y_list))]
        a.append(a_0)
        # 使用递推公式，给a赋值
        for i in range(len(self.x) + 1):
            temp_matrix = np.dot(a[i], self.M[i])
            a.append(temp_matrix)
        self.a = a

    def backward_algorithm(self):

        b = []  # 定义后向概率矩阵，用于存储Bi（x），m维列向量
        # 初始化位置n+1上的向量
        b_n_1 = [1 if self.y_list[i] == self.stop else 0 for i in range(len(self.y_list))]
        b.insert(0, b_n_1)
        # 使用递推公式，给b赋值
        for i in range(len(self.M), 0, -1):
            temp_matrix = np.dot(self.M[i-1], b[0])
            b.insert(0, temp_matrix)
        self.b = b

    def pro_calculate(self, i, y1, y2=None):
        if y2 is None:
            z = self.z_value()
            return self.a[i][self.y_list.index(y1)]*self.b[i][self.y_list.index(y1)]/z
        else:
            z = self.z_value()
            return self.a[i][self.y_list.index(y1)]*self.M[i-1][self.y_list.index(y1)][self.y_list.index(y2)]*self.b[i][self.y_list.index(y2)]/z


# 概率，在crf里面可以理解为出现的可能性，我们规定了特征函数，符合特征函数的局部结点我们让其势函数等于1，势函数怎么理解呢？这个
# 函数就可以认为是一个定义了我们想要的情况的计数器，符合情况的局部结点势函数为1表明出现一次，不符合的为0.也就是说我们设定各种的
# 特征函数其实就是定义了一种概率空间，定义了每种情况出现的概率（未定义的情况或定义为0的情况表明在我们的概率空间内，这种情况出现
# 的概率为0。对一个序列进行计数，我们得到这个序列在我们概率空间内，响应我们在这个空间定义的计数器的次数，（特征函数的就是函数，
# 就是计数器）。当然如果想要获得标准概率，还需要运用古典概型进行标准化。

# 关于概率计算，对于一个完整的模型而言，其参数只有特征函数，我们输入一个句子，首先我们用特征函数得到转移矩阵，然后我们就可以求出
# 一个标记序列的概率，之后我们可以在此基础上进行计算得到某个位置上为某个标记的概率。所以初始化的时候，应该是仅仅有特征函数
def CCRF_manual():
    M1 = np.array([[0.5, 0.5],
                   [0, 0]])

    M2 = np.array([[0.3, 0.7],
                   [0.7, 0.3]])

    M3 = np.array([[0.5, 0.5],
                   [0.6, 0.4]])

    M4 = np.array([[1, 0],
                   [1, 0]])

    M = []
    M.append(M1)
    M.append(M2)
    M.append(M3)
    M.append(M4)

    crf = CLineCrf(M, ['ni', 'men', 'hao'], [1, 2], 2, 1)
    ret = crf.z_value()
    print("The z-score is:", ret)
    print("The matrix a is:", crf.a)
    print("The matrix b is:", crf.b)
    print("The probability is:", crf.pro_calculate(1, 2, 2))

CCRF_manual()





