import math
import random
import seaborn as sns

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
from scipy.stats import norm, expon

# 2 b
for n in [2,4,6,8,10,40]:
    obsNum = 70000

    Xn = [0 for i in range(obsNum)]
    for i in range(n):
        randObservations = expon.rvs(size=obsNum, scale=1 / 0.5)
        Xn = [a + b for a, b in zip(Xn, randObservations)]
    Xn = [item / n for item in Xn]
    sns.kdeplot(data=Xn)
    plt.show()
    # 2c
    meanXn = np.mean(Xn)
    print(meanXn)
    sdX2 = math.sqrt(sum([(item - meanXn) ** 2 for item in Xn]) / obsNum)
    print(sdX2)

    # 2d

    x = np.linspace(-1, 7, 1000)
    y = [norm.pdf(val, 1/0.5, math.sqrt((1/0.25) / n)) for val in x]
    plt.plot(x, y, '-b')
    plt.show()
    f
    print(norm.ppf(0.95, 3.5, math.sqrt((35 / 12) / n)))
print(1-norm.cdf(1/26))