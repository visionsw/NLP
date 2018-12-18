import numpy as np
import matplotlib.pyplot as plt
STATE_NUM = 5
X = [0]
P = [[0.1, 0.3, 0.6],
     [0.5, 0.2, 0.3],
     [0.3, 0.3, 0.4]]
THRESHOLD = 1000
LOOP_NUM = 10000
# 要采样的分布
PI = [0.1, 0.1, 0.8]

for i in range(LOOP_NUM):
    temp_state = X[i]
    # 采样y
    u = np.random.uniform()
    if 0 <= u < P[temp_state][0]:
        y = 0
    elif P[temp_state][0] <= u < P[temp_state][0] + P[temp_state][1]:
        y = 1
    else:
        y = 2
    # 均匀分布采样
    v = np.random.random_sample()
    # 判断是否接受转移
    if v < PI[y] * P[y][temp_state]:
        X.append(y)
    else:
        X.append(temp_state)

num = [X.count(0), X.count(1), X.count(2)]
print(num)
plt.hist(X)
plt.show()
