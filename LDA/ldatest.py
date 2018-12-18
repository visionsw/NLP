import numpy as np
import lda
import matplotlib.pyplot as plt
import lda.datasets

# 数据解析
X = lda.datasets.load_reuters()
# X矩阵为395*4258，共395个文档，4258个单词，主要用于计算每行文档单词出现的次数（词频）
vocab = lda.datasets.load_reuters_vocab()
# vocab为具体的单词，共4258个，它对应X的一行数据，其中输出的前5个单词
title = lda.datasets.load_reuters_titles()
# titles为载入的文章标题，共395篇文章

# 训练解析
model = lda.LDA(n_topics=20, n_iter=500, random_state=1)
model.fit(X)

# 主题=单词分布,20行（主题个数），4258列（单词个数）
topic_word = model.topic_word_

# 计算各主题topN的词
n = 5
for i, topic_list in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_list)][:-(n+1):-1]
    # print(i, topic_words)

# 文档-主题分布,文档数，主题数，数值为对应概率
doc_topic = model.doc_topic_
print(doc_topic.shape)

# 计算前十篇文章最可能的Topic
for n in range(10):
    topic_most_pr = doc_topic[n].argmax()
    print(n, topic_most_pr)

#   作图分析

# 各个主题中单词权重分布的情况
f, ax = plt.subplots(5, 1, figsize=(8, 6), sharex=True)
for i, k in enumerate([0, 5, 9, 14, 19]):
    ax[i].stem(topic_word[k, :], linefmt='b-',
               markerfmt='bo', basefmt='w-')
    ax[i].set_xlim(-50, 4350)
    ax[i].set_ylim(0, 0.08)
    ax[i].set_ylabel("Prob")
    ax[i].set_title("topic {}".format(k))

ax[4].set_xlabel("word")

plt.tight_layout()
plt.show()

# 文档具体分布在哪个主题
f, ax = plt.subplots(5, 1, figsize=(8, 6), sharex=True)
for i, k in enumerate([1, 3, 4, 8, 9]):
    ax[i].stem(doc_topic[k, :], linefmt='r-',
               markerfmt='ro', basefmt='w-')
    ax[i].set_xlim(-1, 21)
    ax[i].set_ylim(0, 1)
    ax[i].set_ylabel("Prob")
    ax[i].set_title("Document {}".format(k))

ax[4].set_xlabel("Topic")

plt.tight_layout()
plt.show()



