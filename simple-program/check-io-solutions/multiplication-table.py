'''https://py.checkio.org/mission/multiplication-table/
神经病乘法
将两个数(1-100)转化二进制。
对位，AND一次，OR一次，XOR一次……
把对位之后的数字转化为十进制，加起来。
如果没看懂请看原网页……
'''
def checkio(alpha, beta):
    alpha = bin(alpha)
    beta = bin(beta)
    result = 0
    for a in alpha[2:]:
        _num_and = []
        _num_or = []
        _num_xor = []
        for b in beta[2:]:
            _num_and.append(str(int(int(a) and int(b))))
            _num_or.append(str(int(int(a) or int(b))))
            _num_xor.append(str(int(((int(a) and (not int(b)) or ((not int(a)) and int(b)))))))
        result = result + int(''.join(_num_and),2) + int(''.join(_num_or),2) + int(''.join(_num_xor),2)
    return result

checkio(4, 6) == 38
checkio(2, 7) == 28
checkio(7, 2) == 18
