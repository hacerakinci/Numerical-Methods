# Hacer Akıncı
# 150200007

from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt

def implementFx (x, f_x, i):
    return (f_x[i] - f_x[i -1])/(x[i][1]- x[i-1][0])


# This list keeps x_i starting and ending values for next step 
x = [[0, 0], [1, 1], [2, 2], [4, 4], [6, 6]]
f_x = [1, 9, 23, 93, 259]

# Divided difference table store x and f_x list for every step
divDiffTable = []
divDiffTable.append([x, f_x])

n = len(f_x)
i = 0 
while (i < n):
    # for this step create new lists
    x_i = []
    f_x_i = []

    for j in range( 1, len(divDiffTable[i][0]) ):
        x_i.append( [divDiffTable[i][0][j-1][0], divDiffTable[i][0][j][1]] )
        f_x_i.append( implementFx(divDiffTable[i][0], divDiffTable[i][1], j) )

    divDiffTable.append([x_i, f_x_i])
    
    # last step
    if len(x_i) == 1:
        break
    i = i + 1

def constructPolynomial(a):
    n = len(divDiffTable)
    result = 0
    for i in range(len(divDiffTable)):    
        q_i = 1
        for j in range(n - len(divDiffTable[i][0])):
            q_i = q_i * (a - divDiffTable[0][0][j][0])
        result += q_i * divDiffTable[i][1][0]
    return result


X = np.array([0, 1, 2, 4, 6])
f_x = np.array([1, 9, 23, 93, 259])

d = np.arange(0.0, 7, 0.001)

plt.plot(X, f_x, 'bo', label= 'Data')
plt.plot(d, constructPolynomial(d), 'y-')
plt.legend(loc='best')
plt.show()

""" 
Print the Divided Difference Table
head = ["x_i","fx[xi,..xj]"] 
print(tabulate(divDiffTable, headers = head))

Print the result of input for the constructed polynomial
num = float(input("Enter x: "))
print(constructPolynomial(num)) """