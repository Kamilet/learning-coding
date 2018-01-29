'''
输入一个数求圆面积
输入两个数求长方形面积
输入三个数求三角形面积
'''


def simple_areas(x, y=0, z=0):
    r = 0
    if z:
        # triangle
        p = (x + y + z)/2
        r = (p * (p-x)*(p-y)*(p-z)) ** 0.5
    elif y:
        # rectangle
        r = x * y
    else:
        # circle
        from math import pi
        r = pi * (x/2) ** 2
    return round(r, 2)


assert simple_areas(3) == 7.07
assert simple_areas(2, 2) == 4
assert simple_areas(2, 3) == 6
assert simple_areas(3, 5, 4) == 6
assert simple_areas(1.5, 2.5, 2) == 1.5
