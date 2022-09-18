'''
작성자 : 박현민 21900326
프로그램의 목적 : matplotlib을 이용하여 pie 그래프를 구현하는 프로그램이다.
'''

import matplotlib.pyplot as plt
import numpy as np

y = np.array([20, 20, 35, 15, 10])
mylabels = ["Kyunggi","Chungcheng","Seoul","Jellra","kyungsang"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Five Districts")
plt.show()
