'''
You are given an array of integers.
You should find the sum of the elements with even indexes
(0th, 2nd, 4th...) then multiply this summed number and the final element of the array together.
Don't forget that the first element has an index of 0. 
'''

def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    _output = 0
    for i in range(0,len(array),2):
        _output += array[i]
    try:
        _output *= array[len(array)-1]
    except:
        pass
    return _output

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
