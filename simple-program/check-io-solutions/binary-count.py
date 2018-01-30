'''
计算输入的数在2进制用了几个1
'''
def checkio(num):
    count = 0
    for array in bin(num)[2:]:
        count += int(array)
    return count

assert checkio(4) == 1
assert checkio(15) == 4
assert checkio(1) == 1
assert checkio(1022) == 9