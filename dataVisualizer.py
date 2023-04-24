# Hacer Akıncı
# 150200007

import math
import numpy as np
import matplotlib.pyplot as plt

# data points
x = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10])
y = np.array([0.72, 1.63, 1.88, 3.39, 4.02, 3.89, 4.25, 3.99, 4.68, 5.03, 5.27, 4.82, 5.67, 5.95, 5.72, 6.01, 5.5, 6.41, 5.83, 6.33])

l_x = lambda x: 1.9320 + 0.5003*x

p_x = lambda x: -0.0686*x*x + (1.2203*x) + 0.6029

f_x = lambda x: 1.8259 + 1.9161*math.log(x)

F_x = np.vectorize(f_x)

plt.plot(x, y, 'bo', label= 'Data')
plt.plot(x, l_x(x), 'r-', label ='Linear Function')
plt.plot(x, p_x(x), 'y-', label = 'Second Degree Function')
plt.plot(x, F_x(x), 's-', label = 'Logarithmic Function')
plt.legend(loc='best')
plt.show()