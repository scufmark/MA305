#!/usr/bin/env python3 
import numpy as np
from matplotlib import pyplot as plt

"""
========================================================================
MA305 - cw 7: Chapman, Piers - 15NOV18
Purpose: Use a function to plot some stuff. Yeah.
========================================================================
"""
def g(x,mu=0,sig=1.5):
	expon = np.exp(-(((x-mu)**2)/(2*sig**2)))
	return (1/(sig*np.sqrt(2*np.pi)))*expon

mu = 0
sig = 0.5
i = 20
xs = -10

y0 = []
y1 = []
y2 = []
y3 = []

x,dx = np.linspace(-10,10,100,retstep=True)
y0 = g(x)
y1 = g(x,0,0.5)
y2 = g(x,0,1.0)
y3 = g(x,0,1.5)
area = sum(y0)*dx
print('area=',area)
gp = (g(x+dx)-g(x))/dx

f=plt.figure()
plt.plot(x,y0,x,gp)
plt.show()

f=plt.figure()
plt.plot(x,y1,x,y2,x,y3)
plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend(['$\sigma=0$','$\sigma=1$','$\sigma=1.5$'],loc='best')
plt.title('Gaussian function with $\mu=0$ and different values of $\sigma$')
plt.show()
f.savefig('Gauss_function.pdf')


