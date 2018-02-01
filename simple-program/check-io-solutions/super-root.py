'''
x**x=N
已知N，求x
1 ≤ number ≤ 10 ** 10 
'''


def super_root(num, accurate=0.0001):
    x = 0
    n = 1
    while True:
        if abs(x ** x - num) <= accurate:
            break
        nn = 1/10**(n-1)
        for i in range(0, 10):
            if (x + i * nn)**(x + i * nn) <= num and (x + (i+1) * nn)**(x + (i+1) * nn) >= num:
                x = round(x + i * nn, n)
                break
        n += 1
        # print(n)
        # input(x)
    return x


super_root(4) == 2
super_root(27) == 3
super_root(81) == 3.504339593597054
