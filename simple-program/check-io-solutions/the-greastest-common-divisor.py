'''
最大公约数
'''

# 为解决


def greatest_common_divisor(*args):
    args = sorted(args)
    for div in range(min(args[-1]//2, args[0]), 0, -1):
        flag = 1
        for a in args:
            if a % div:
                flag = 0
                break
        if flag:
            return div
    # print(diversor)
    return 1


greatest_common_divisor(6, 4) == 2
greatest_common_divisor(2, 4, 8) == 2
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
