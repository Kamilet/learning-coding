'''输入字符串，返回连续出现次数最多的字符'''
def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    '''
    BAD!!!!!

    if len(line) == 0:
        return 0
    lenth = 1
    max_lenth = 1
    for i in range(1, len(line)):
        lenth += 1
        if line[i] != line[i-1]:
            if lenth - 1 > max_lenth:
                max_lenth = lenth - 1
            lenth = 1
    return max_lenth
    '''
    lenth = 1
    max_lenth = 0
    for i in range(0, len(line)-1):
        if line[i] == line[i+1]:
            lenth += 1
            if max_lenth < lenth:
                max_lenth = lenth
        else:
            if max_lenth < lenth:
                max_lenth = lenth
            lenth = 1
    return max_lenth

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert long_repeat('sdsffffse') == 4, "First"
    #assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('') == 0, "blank"
    assert long_repeat('aa') == 2, "aa"
    print('"Run" is good. How is "Check"?')