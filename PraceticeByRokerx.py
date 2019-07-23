# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pylab import *
import numpy as np

"""
x_float = array([0,pi/6,pi/4,pi/3,pi/2,])
plot(x_float,sin(x_float))


x = array([1,2,3],dtype = float)
y = x**2
z = array([4,5,6],dtype = float)
t = z**2
plot(y,t)

x = linspace(0, 360, 13)
y = radians(x)
print(sin(y))
figure()
plot(y,sin(y))


x = array([3,4], dtype=float)
m=norm(x)
print(m)


x = linspace(0,2*pi,500)
figure(1)
plot(x,sin(x),linewidth=10)
figure(2)
grid()
xlim([0, pi])
plot(x,cos(x))

a_start = 0
a_stop = 2
a_points = 100
a = logspace(a_start, a_stop, a_points)
b = log(a)
figure()
semilogy(a,b)

x = linspace(0,360,130)
y = radians(x)
figure()
plot(y,sin(y),"r:")
ylim = ([0,4*pi])
plot(y,sin(y))
plot(y,cos(y))
"""

r = rand(100)
print(r)
b = argmax(r)
print(b)
print(r>0.5)
print(sum(r>0.5))
a = arange(100)
print(a)















































