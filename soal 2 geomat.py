import numpy as np
import matplotlib.pyplot as plt
import math

def myfunc_(n, x, t):
    nx1 = []
    #nx2 = []

    
    for i in range(1, n+1, 2): ### melakukan operasi perulangan sigma dengan persamaan solusi
        Uxt1 = 1/i*math.exp(-1*((i*math.pi)/20)*t) * math.sin(((i*math.pi)/20) * x)
        #Uxt2 = 1/i*math.exp(-1*((i*math.pi)/20)*t) * math.sin(((i*math.pi)/20) * x)

        nx1.append(Uxt1)
        #nx2.append(Uxt2)

    ans = (200*sum(nx1)/math.pi)

    return ans

def myfunc2_(n, x, t):
    #nx1 = []
    nx2 = []

    
    for i in range(2, n+1, 4): ### melakukan operasi perulangan sigma dengan persamaan solusi
        #Uxt1 = 1/i*math.exp(-1*((i*math.pi)/20)*t) * math.sin(((i*math.pi)/20) * x)
        Uxt2 = 1/i*math.exp(-1*((i*math.pi)/20)*t) * math.sin(((i*math.pi)/20) * x)

        #nx1.append(Uxt1)
        nx2.append(Uxt2)

    ans = -1*(400*sum(nx2)/math.pi)

    return ans

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

x = np.arange(0, 20, 0.5)
t = np.arange(0, 10, 0.5)
x, t = np.meshgrid(x, t)
n = 100

zu1 = np.array([myfunc_(n, x, t) for x,t in zip(np.ravel(x), np.ravel(t))])
zu2 = np.array([myfunc2_(n, x, t) for x,t in zip(np.ravel(x), np.ravel(t))])  ### convert variabel sumbu-Z menjadi 1-Dimensi

Uxt1 = zu1.reshape(x.shape)   ### convert variabel sumbu-Z menjadi 2-Dimensi
Uxt2 = zu2.reshape(x.shape)   ### convert variabel sumbu-Z menjadi 2-Dimensi

ax.plot_surface(x, t, Uxt1+Uxt2, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')   ### melakukan plot grafik

ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('u')

plt.show()
