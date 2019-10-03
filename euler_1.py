import numpy as np


def euler_1(function, y0, timeStep, finalTime):
    numberSteps = finalTime/timeStep
    time = np.linspace(0, finalTime, numberSteps)
    results = np.zeros((1,len(time)))

    for equation in function:
