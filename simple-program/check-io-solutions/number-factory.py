'''
输入一个整数，将它分解质因数
如果不能分解，返回0
如果可以分解，判断所有分解后的情况（个位数）
将所有分解后的情况连接起来，返回最小的那个
'''


def checkio(number):
    digits = ['0']
    flag = True
    while flag:
        flag = False
        for i in range(9, 1, -1):
            if not number % i:
                digits.append(str(i))
                number /= i
                flag = True
                break
    if len(digits) == 2 or number != 1:
        return 0
    digits.sort()
    # print(digits)
    return int(''.join(digits))



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    assert checkio(3645) == 5999, "7th example"
    assert checkio(3275) == 0, "8th example"