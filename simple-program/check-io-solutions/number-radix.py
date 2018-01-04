def checkio(str_number, radix):
    _dict = radix_dict(radix)
    _corvered_number = 0
    try:
        for i in range(0, len(str_number)):
            _corvered_number += _dict[str_number[-i-1]] * radix ** i
        return _corvered_number
    except:
        return -1


def radix_dict(radix):
    '''generate a dict with radix'''
    _dict = {}
    for i in range(radix):
        if i < 10:
            _dict[str(i)] = i
        if i >= 10:
            _dict[chr(55+i)] = i
    return _dict


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
