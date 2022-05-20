import numpy as np
import matplotlib.pyplot as plt
import math


def myfunc_(n, x, y):
    kx = []

    for k in range(1, n+1): ### melakukan operasi perulangan sigma dengan persamaan solusi
        Txy = ((120*np.power(-1, k))/((2*k+1)**2)*((math.pi)**2)) * \
            math.exp((-1*(2*k+1)*math.pi*y)/30) * \
            math.sin(((2*k+1)*math.pi*x)/30)
            
        kx.append(Txy)

    ans = sum(kx)

    return ans


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

x = np.arange(0, 10, 0.5)
y = np.arange(0, 20, 0.5)
x, y = np.meshgrid(x, y)
n = 50

zu = np.array([myfunc_(n, x, y) for x, y in zip(np.ravel(x), np.ravel(y))]) ### convert variabel sumbu-Z menjadi 1-Dimensi
Txy = zu.reshape(x.shape)   ### convert variabel sumbu-Z menjadi 2-Dimensi


grafik = ax.plot_surface(x, y, Txy, rstride=1, cstride=1,   ### melakukan plot grafik
                cmap='coolwarm', edgecolor='none')

fig.colorbar(grafik, shrink=0.5, aspect=5)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u')

plt.show()
