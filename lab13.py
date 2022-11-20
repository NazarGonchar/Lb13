import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + math.sin(y / math.sqrt(7))

x0 = 0,5
b = 1,5
h = 0.1
x = np.arange(x0,b+h,h)
n = len(x) - 1
y = np.empty(n+1)
y[0] = 0,6

for i in range (n):
     y[i+1] = y[i] + h/2 * (f(x[i], y[i]) + f(x[i+1], y[i] + h * f(x[i], y[i])))

y_rounded = np.round_(y,4)
print('x =',x, '\ny =',y_rounded)

plt.plot(x,y,'o',x,y,'red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод Ейлера-Коші')
plt.legend(['точки','x+sin(y/sqrt(7))'])
plt.grid()
plt.show()
