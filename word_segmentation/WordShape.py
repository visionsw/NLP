class WordShape:
    # 词干词典
    root_list = []
    # 前缀词典
    prefis_list = []
    # 后缀词典
    suffix_list = []
    # 词尾变化规则
    lex_rules = []

    # 输入的词
    word = ""

    # 输出结果
    result = ""

    # 初始化函数
    def __init__(self, word, root_list, prefis_list, suffix_list, lex_rules):
        # 所有词统一为小写
        self.word = word.lower()
        self.root_list = root_list
        self.prefis_list = prefis_list
        self.suffix_list = suffix_list
        self.lex_rules = lex_rules
        self.process()

    # 分析算法
    def process(self):
        w = self.word
        length = len(w)

        if w in self.root_list:
            self.result = w
            return self.result

        # 后缀分析
        for i in range(length):
            w1 = w[:length-i]
            w2 = w[-i:]

            if w2 in self.suffix_list:
                w1 = w1 + "'"
                # 如果没有前缀,直接返回结果
                if w1 in self.root_list:
                    self.result = w1 + " " + w2
                    return self.result
                # 如果有前缀/这里没有考虑词根词典数量不足的情况，其实不只是这里，所有情况都在词典全面的情况下建立的
                else:
                    # 前缀分析
                    for j in range(len(w1)):
                        if j <= len(w1):
                            h1 = w1[:j]
                            h2 = w1[j:]

                            if h1 in self.prefis_list:
                                h1 = h1 + "'"
                                if h2 in self.root_list:
                                    self.result = h1 + " " + h2 + " " + w2
                                    return self.result




s1 = ["put'"]
s2 = ["ing"]
s = "computing"
test1 = WordShape(s, s1, ["com"], s2, [""])
print(test1.result)