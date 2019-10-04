# labo 4 de l'équipe 1 par Lucka Barbeau et Matthew Coffey

import numpy as np
import matplotlib.pyplot as plt

M = 4.2
C = 1.0
K = 100.0

A = np.array([[M, 0], [0, 1]])
A_inv = np.linalg.inv(A)
A = np.array([[C / M, K / M], [-1, 0]])


def F(t, y):
    return -A.dot(y)


def runge_kutta(F, y, t, dt):
    k1 = dt * F(t, y)
    k2 = dt * F(t + 0.5 * dt, y + k1 * 0.5)
    k3 = dt * F(t + 0.5 * dt, y + k2 * 0.5)
    k4 = dt * F(t + dt, y + k3)
    return y + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


X0 = 10
Y0 = 0
#Y0_d = -10

time_step = 0.01
time_step_2 = 0.01

time_range = 10

time = np.arange(0, time_range, time_step)
time2 = np.arange(0, time_range, time_step_2)

y = np.array([Y0, X0])
y2 = np.array([Y0, X0])

Y = []
Y2 = []

for t in time:
    y = y + time_step * F(t, y)
    Y.append(y[1])
for t2 in time2:
    y2 = runge_kutta(F, y2, t2, time_step_2)
    Y2.append(y2[1])

t = [i for i in time]
t2 = [i for i in time2]
plt.plot(t, Y, t2, Y2)
