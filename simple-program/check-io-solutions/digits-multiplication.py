'''
 You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes). 
'''
from functools import reduce  # for method 2

def checkio(number):
    #method 1
    
    number = str(number)
    result = 1
    for i in range(len(number)):
        if number[i] != '0':
            result *= int(number[i])
    return result
    
    #method 2 like this
    #forget it
    #reduce(lambda x,y:x+y,l)
    '''
    number = list(str(number))
    print(reduce(lambda x,y: int(x)*int(y), number))
    return 120
    '''

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
