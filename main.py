import math
import random
import seaborn as sns

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
from scipy.stats import norm
for n in [2,4,6,8,10] :
    # 2 b

    obsNum = 70000
    Xn = [0 for i in range(obsNum)]
    for i in range(n):
        randObservations = [random.randint(1, 6) for i in range(obsNum)]
        Xn = [a + b for a, b in zip(Xn, randObservations)]
    Xn = [item / n for item in Xn]
    sns.kdeplot(data=Xn)
    # plt.show()

    # 2c
    meanXn = np.mean(Xn)
    print(meanXn)
    sdX2 = math.sqrt(sum([(item - meanXn) ** 2 for item in Xn]) / obsNum)
    print(sdX2)

    # 2d

    x = np.linspace(0, 7, 1000)
    y = [norm.pdf(val, 3.5, math.sqrt((35 / 12) / n)) for val in x]
    plt.plot(x, y, '-b')
    plt.show()
    # f
    # print(norm.ppf(0.95, 3.5, math.sqrt((35 / 12) / n)))
