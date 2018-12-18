class ShortCut:
    # 依赖词表
    word_list = ["确实", "的确", "实在", "在理", "刘仕阳", "205", "狗儿子"]
    nodes_num = 0
    edges = [[]]
    sentence = ""
    result_sequence = []
    result_sentence = ""

    def __init__(self, sen):
        self.create_nodes(sen)

    # 创建结点，参数为一个句子，字符串类型
    def create_nodes(self, sen):
        self.nodes_num = len(sen) + 1
        self.sentence = sen
        self.create_edges()
        self.find_short_road()
        self.calculate_result()

    # 导入词表，参数为一个字符串列表
    def create_word_list(self, word_list):
        self.word_list = word_list

    # 创建边
    def create_edges(self):

        sen = self.sentence
        # 构造结点数 * 结点数形状的矩阵，存储图信息
        self.edges = [[0 for i in range(len(sen) + 1)] for j in range(len(sen) + 1)]
        # 为矩阵赋予边的权重以及对应字符串
        for i in range(len(sen)+1):
            for j in range(len(sen)+1):
                if (i < j) and (sen[i:j] in self.word_list):
                    self.edges[i][j] = (sen[i:j], 1)
                elif j-i == 1:
                    self.edges[i][j] = (sen[i:j], 1)
                elif j == i:
                    self.edges[i][j] = ("", 0)
                else:
                    self.edges[i][j] = (sen[i:j], 10000)
        return self.edges

    # 计算最短路径信息表
    def find_short_road(self):
        # 记录源点到其他结点最短距离的向量，长度与结点数相同
        dst = [item[1] for item in self.edges[0][:]]
        # 最短路径信息表，初始化为-1，长度与结点数相同
        road = [-1 for i in range(self.nodes_num)]

        # 已找到最短路径的结点集合
        P = [0]
        # 未找到最短路径的结点集合
        Q = list(range(1, self.nodes_num))

        # 使用最短路算法计算信息表
        for item in range(self.nodes_num - 1):

            # 记录Q中最近的结点
            temp = 0
            min_dst = 100000
            # 选择Q中距离源点最近的结点
            for unmarked_nodes in Q:
                if dst[unmarked_nodes] < min_dst:
                    min_dst = dst[unmarked_nodes]
                    temp = unmarked_nodes

            # 将该结点从Q中移除，并添加到P中
            Q.remove(temp)
            P.append(temp)

            # 更新Q中结点的距离信息，并记录经过的中间结点
            for un_nodes in Q:
                if dst[un_nodes] < 100000:
                    if dst[un_nodes] > dst[temp] + self.edges[temp][un_nodes][1]:
                        road[un_nodes] = temp
                        dst[un_nodes] = dst[temp] + self.edges[temp][un_nodes][1]

        self.result_sequence = road
        return road

    # 计算分词结果
    def calculate_result(self):
        # 当前结点
        now_node = len(self.sentence)
        # 如果遇到最短路路径能直接从源点到达的就结束
        while now_node != -1:
            # 如果可以从源点到达当前结点，截取相应字符串
            if self.result_sequence[now_node] == -1:
                self.result_sentence = self.edges[0][now_node][0] + " " + self.result_sentence
            # 如果需要经过中间结点才能到达当前结点，截取相应字符串
            else:
                self.result_sentence = self.edges[self.result_sequence[now_node]][now_node][0] + " " + self.result_sentence
            # 到下一个结点去
            now_node = self.result_sequence[now_node]

        return self.result_sentence


class PShortCut:
    # 依赖词表
    pass


class NGramCut:
    pass


class CharacterBasedCut:
    pass


class AveragedPerceptionCut:
    pass


class MaxVectorCut:
    word_list = ""
    sentence = ""
    result_sentence = ""

    # 初始化
    def __init__(self, sen, word_list=None):
        self.sentence = sen
        self.word_list = word_list
        self.process()

    # 处理函数
    def process(self):
        sen = self.sentence

        while len(sen) > 0:
            # 通过若干次for循环找到一个词，并从sen中截取，只要sen长度不为0，就不停
            for i in range(len(sen), 0, -1):
                # 在词典中
                if sen[0:i] in self.word_list:
                    self.result_sentence += sen[0:i] + "/ "
                    sen = sen[i:]
                    break
                # 不在词典中
                else:
                    # 为单字
                    if len(sen[0:i]) == 1:
                        self.result_sentence += sen[0:i] + "/ "
                        sen = sen[i:]
                        break
                    continue


class CrfCut:
    import sys


s = "刘仕阳是205的狗儿子"
mv = MaxVectorCut(s, ["确实", "的确", "实在", "在理", "刘仕阳", "205", "狗儿子"])
print(mv.result_sentence)