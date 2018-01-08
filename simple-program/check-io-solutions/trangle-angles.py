'''
知边求角问题
'''
import math


def checkio(a, b, c):

    if max(a, b, c) * 2 >= a + b + c:
        return [0, 0, 0]

    C = math.acos((a**2 + b**2 - c**2)/ (2 * a * b))
    B = math.acos((a**2 + c**2 - b**2)/ (2 * a * c))
    A = math.acos((b**2 + c**2 - a**2)/ (2 * b * c))

    result = []
    result.append(round(C / math.pi * 180))
    result.append(round(A / math.pi * 180))
    result.append(round(B / math.pi * 180))

    print(sorted(result))

    return sorted(result)














'''

def checkio(a, b, c):
    # let's try without 'import math' !

    # judgement
    if max(a, b, c) / 2 >= a + b + c:
        return [0, 0, 0]
    # ok, use an formula
    # c**2 = a**2 + b**2 - 2*a*b*cos(C)
    # then
    # cos(C) = (a**2 + b**2 - c**2)/ 2*a*b
    cos_C = (a**2 + b**2 - c**2)/ (2 * a * b)
    cos_B = (a**2 + c**2 - b**2)/ (2 * a * c)
    cos_A = (b**2 + c**2 - a**2)/ (2 * b * c)
    # C = arccos( (a**2 + b**2 - c**2)/ 2*a*b )
    # there isn't a simple way to calculate arccos(X)
    # you can use:
    # import math
    # int(math.acos(cos_C)/math.pi*180)
    # to get C
    # here I'll calculate it
    # won't be too hard because the types of angles are int
    # let's finish this function and creat a new one for that!
    result = []
    result.append(arccos_angle(cos_C))
    result.append(arccos_angle(cos_A))
    result.append(arccos_angle(cos_B))
    return result.sort()


def arccos_angle(cos_angle):
    # how to do that?
    # once we get a angle, we can put it into a Right Triangle
    # like [angle, 90-angle, 90], and then the three sides will be:
    # [1*cos(angle), 1*cos(90-angle), 1]  # we just set the longest side to 1
    # the arccos(C) actually return radian but angle.

    # then let's think about how to get cos(angle) when we have an angle.
    # think about the new triangle above


'''


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

