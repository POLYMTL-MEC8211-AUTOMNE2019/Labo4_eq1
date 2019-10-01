# labo 4 de l'équipe 1 par Lucka Barbeau et Matthew Coffey

import numpy as np
import matplotlib.pyplot as plt

def F(y,t):
    return A_inv.dot(B.dot(y))


M=4.2
C=1.0
K=100.0

A=np.array([[1, 0], [-C/M,-K/M]])
A_inv=np.linalg.inv(A)
B=np.array([[1, 0], [C,K]])

X0=10
Y0=0
Y0_d=-10

time_step=0.001
time_range=10
nb_step=int(time_range/time_step)+1



X=np.zeros((int(time_range/time_step)+1,1))
X_2=np.zeros((int(time_range/time_step)+1,1))

Y=np.zeros((int(time_range/time_step)+1,1))
Y_2=np.zeros((int(time_range/time_step)+1,1))

Y_d=np.zeros((int(time_range/time_step)+1,1))
Y_d_2=np.zeros((int(time_range/time_step)+1,1))

time=np.zeros((int(time_range/time_step)+1,1))

time_2=np.zeros((int(time_range/time_step)+1,1))



S=np.zeros((2,1))
Y[0]=Y0
X[0]=X0
Y_d[0]=Y0_d

S[0]=X0
S[1]=Y0

Y_2[0]=Y0
X_2[0]=X0
Y_d_2[0]=Y0_d



t=0
i=1

while i<nb_step :

    Y[i,0]=Y_d[i-1,0]*time_step+Y[i-1,0]
    X[i,0]=Y[i-1,0]*time_step+X[i-1,0]
    Y_d[i,0]=-K*X[i,0]/M-C*Y[i,0]/M

    t+=time_step
    time[i,0]=t
    i+=1




plt.plot(time,X)