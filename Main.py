# labo 4 de l'équipe 1 par Lucka Barbeau et Matthew Coffey

import numpy as np
import math
import matplotlib.pyplot as plt
from euler_1 import euler_1

m = 4.2
c = 1.0
k = 100.0

y0 = [0, 10]

eulerTimeStep = 0.0001
timeRange = 5
euler_Time = np.arange(0.0, timeRange, eulerTimeStep)


def function(y, t):
    s = -10*m*math.pi**2 * math.cos(math.pi*t) - 10*math.pi*c*math.sin(math.pi*t) + 10*k*math.cos(math.pi*t)
    A = np.array([[m, 0], [0, 1]])
    B = np.array([[c, k], [-1, 0]])
    F = np.array([[s], [0]])

    return np.linalg.inv(A).dot(F - B.dot(y))


outputEuler = euler_1(function, y0, eulerTimeStep, timeRange)

plt.plot(euler_Time, outputEuler[:, 1])

