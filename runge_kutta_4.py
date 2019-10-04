import numpy as np


def runge_kutta4(function, y0, timeStep, finalTime):
    time = np.arange(0.0, finalTime, timeStep)
    y = np.array(y0)
    y = y.reshape(-1,1)
    Y = np.zeros(((int(finalTime/timeStep)), 2))

    i = 0
    for t in time:
        k1 = timeStep * function(y, t)
        k2 = timeStep * function(y + k1 * 0.5, t + 0.5 * timeStep)
        k3 = timeStep * function(y + k2 * 0.5, t + 0.5 * timeStep)
        k4 = timeStep * function(y + k3, t + timeStep)
        y = y + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        Y[i, 0] = y[0]
        Y[i, 1] = y[1]
        i += 1

    return np.array(Y)

