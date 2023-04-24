# Hacer Akıncı
# 150200007

def Bisection(num, eps):
    l = 0
    r = num
    x = (l + r)/2

    while abs(num - x**5) > eps:
        if x**5 > num:
            r = x
            x = (l + x)/2
        else:
            l = x
            x = (r + x)/2

    return x



num,error_rate = [float(x) for x in input().split()]


if num < 0:
    print(Bisection((num*-1), error_rate)*-1)
else:
    print(Bisection((num), error_rate))


