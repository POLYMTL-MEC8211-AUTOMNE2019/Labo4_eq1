# labo 4 de l'équipe 1 par Lucka Barbeau et Matthew Coffey

import numpy as np
import math
import matplotlib.pyplot as plt
from euler_1 import euler_1
from runge_kutta_4 import runge_kutta4

m = 4.2
c = 1.0
k = 100.0

y0 = [0, 10]

timeRange = 5

solManufacturee = 10*math.cos(math.pi*timeRange)

timeStep = [.1, .05, .025, .0125, .00625, .003125, .0015625]
erreurEuler = []
erreurRungeKutta = []

for dt in timeStep:
    eulerTime = np.arange(0.0, timeRange, dt)
    rungeKuttaTime = np.arange(0.0, timeRange, dt)

    def function(y, t):
        s = -10*m*math.pi**2 * math.cos(math.pi*t) - 10*math.pi*c*math.sin(math.pi*t) + 10*k*math.cos(math.pi*t)
        A = np.array([[m, 0], [0, 1]])
        B = np.array([[c, k], [-1, 0]])
        F = np.array([[s], [0]])

        return np.linalg.inv(A).dot(F - B.dot(y))

    outputEuler = euler_1(function, y0, dt, timeRange)
    outputRungeKutta = runge_kutta4(function, y0, dt, timeRange)

    errEuler = solManufacturee - outputEuler[-1, 1]
    errRungeKutta = solManufacturee - outputRungeKutta[-1, 1]

    erreurEuler.append(errEuler)
    erreurRungeKutta.append(errRungeKutta)

    #plt.figure()
    #plt.plot(eulerTime, outputEuler[:, 1])
    #plt.plot(rungeKuttaTime, outputRungeKutta[:, 1])

plt.loglog(timeStep, erreurEuler)
plt.loglog(timeStep, erreurRungeKutta)
plt.xlabel("Log(timeStep)")
plt.ylabel("Log(erreur)")
plt.legend(("Erreur avec la méthode d'Euler d'ordre 1", "Erreur avec la méthode de Runge Kutta d'ordre 4"))
plt.title('Ordre de convergence des erreurs')

pEuler = math.log(erreurEuler[-2]/erreurEuler[-1])/math.log(timeStep[-2]/timeStep[-1])
pRungeKutta = math.log(erreurRungeKutta[-2]/erreurRungeKutta[-1])/math.log(timeStep[-2]/timeStep[-1])

print("L'ordre de convergence pour la méthode d'Euler d'ordre 1 est : {:5.2f}".format(pEuler))
print("L'ordre de convergence pour la méthode Runge Kutta d'ordre 4 est : {:5.2f}".format(pRungeKutta))

