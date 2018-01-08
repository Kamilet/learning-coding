'''罗马数字转阿拉伯数字'''

'''
Numeral Value
I   1 (unus)
V   5 (quinque)
X   10 (decem)
L   50 (quinquaginta)
C   100 (centum)
D   500 (quingenti)
M   1,000 (mille)
'''


roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def reverse_roman(roman_string):
    number = 0
    for i in range(0, len(roman_string)-1):
        if roman_dict[roman_string[i]] < roman_dict[roman_string[i+1]]:
            number -= roman_dict[roman_string[i]]
        else:
            number += roman_dict[roman_string[i]]
    return abs(number) + roman_dict[roman_string[-1]]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
    assert reverse_roman('MMMCMXCIX') == 3999, '3999'