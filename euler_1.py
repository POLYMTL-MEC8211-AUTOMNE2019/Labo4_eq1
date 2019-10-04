import numpy as np


def euler_1(function, y0, timeStep, finalTime):
    time = np.arange(0.0, finalTime, timeStep)
    y = np.array(y0)
    y = y.reshape(-1,1)
    Y = np.zeros(((int(finalTime/timeStep)), 2))

    i = 0
    for t in time:
        y = y + timeStep * function(y, t)
        Y[i, 0] = y[0]
        Y[i, 1] = y[1]
        i += 1

    return np.array(Y)

