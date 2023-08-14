# Hacer Akıncı
# 150200007

# Lagrange Interpolation Method

import numpy as np
import matplotlib.pyplot as plt

x = np.array([-1.2, 0.3, 1.1])
y = np.array([-5.76, -5.61, -3.69])

def LImethod(num):
    f_x = 0
    for i in range(len(x)):
        res = 1
        for j in range(len(x)):
            if i != j:
                res = res * ((num - x[j]) / (x[i] - x[j]))
        f_x = f_x + res*y[i]
    return f_x

d = np.arange(-2.0, 2, 0.0001)

plt.plot(x, y, 'bo', label= 'Data')
plt.plot(d, LImethod(d), 'y-')
plt.legend(loc='best')
plt.show()


# 0Print the result of input for the constructed polynomial

num = float(input("Enter x: "))    
print(LImethod(num))

