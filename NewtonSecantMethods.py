# Hacer Akıncı
# 150200007

import math

eps = 0.00000000001

def F(x): # calculate f(x)
    f_x = 4*(math.log(x)) - x
    return f_x

def d_F(x): # calculate derivative of f(x)
    d_x = 4/x -1
    return d_x

def convergenceRate(errors):
    # according to formula there must be at least 3 error
    if len(errors) >= 3:
        r = math.log(abs(errors[-1] / errors[-2])) / math.log(abs(errors[-2] / errors[-3]))
    else:
        r = 0

    return r

def errorEstimation(errors):
    e = abs(errors[-1])
    return e

def NextonMethod():

    def x_next(x, f_x, d_x): # calculate x_n+1
        x_n = x - (f_x / d_x)
        return x_n
    
    print("For Newton Method enter initial value(x_0) and maximum number of iterations: ")
    i_0, max_itr = [float(x) for x in input().split()]

    n = 0
    x_n = i_0 # to keep next element
    x_p = x_n # to keep previous value of x
    f_x = F(x_n) 
    d_x = d_F(x_n)

    print("x_0 = {}".format(x_n))

    errors = [] # keep error values 

    for i in range (1, int(max_itr) + 1):

        n = i # step

        x_n = x_next(x_p, f_x, d_x) # find next element

        print("x_{} = {}".format(n, x_n))

        f_x = F(x_n) # calculate f(x)
        d_x = d_F(x_n) # calculate f'(x)

        error = abs(x_n - x_p) # find the difference
        x_p = x_n # update previous element

        # add error to the list after checking error not equal zero, otherwise log function will give an error
        if error < eps:
            break 
        errors.append(error)
        
    c_rate = convergenceRate(errors)
    e_estm = errorEstimation(errors)

    print("Convergence rate is {}".format(c_rate))    
    print("Error estimation is {}".format(e_estm))    


# secant method
def SecantMethod():
    
    def x_next(x_0, x_1):
        x_n = x_1 - (F(x_1)*(x_1 - x_0))/(F(x_1) - F(x_0))
        return x_n

    print("For Secant Method enter initial values(x_0 & x_1) and maximum number of iterations: ")

    i_0, i_1, max_itr = [float(x) for x in input().split()]
    
    x_0 = i_0 
    x_1 = i_1

    print("x_{} = {}".format(0, x_0))
    print("x_{} = {}".format(1, x_1))
    x_p = x_1

    errors = []

    for i in range (2, int(max_itr) + 2):
        
        n = i
        x_n = x_next(x_0, x_1)
        print("x_{} = {}".format(n, x_n))

        # update
        x_0 = x_1
        x_1 = x_n
        f_x = F(x_n)
        d_x = d_F(x_n)

        error = abs(x_n - x_p)
        x_p = x_n

                # add error to the list after checking error not equal zero, otherwise log function will give an error
        if error < eps:
            break
        errors.append(error)
       
    c_rate = convergenceRate(errors)
    e_estm = errorEstimation(errors)

    print("Convergence rate is {}".format(c_rate))  
    print("Error estimation is {}".format(e_estm))    


NextonMethod()
print()
SecantMethod()

