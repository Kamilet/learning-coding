'''
找到出现2次以上的最长的字符串
返回它的长度
'''

def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    maxlen = 0
    lenth = len(line)
    for i in range(lenth):
        for k in range(i,lenth):
            if line[i:k] in line[0:i] or line[i:k] in line[k:lenth]:
                if maxlen <= k-i:
                    maxlen = k-i
    return maxlen

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    assert double_substring("abababaab") == 3, '3'
    print('"Run" is good. How is "Check"?')
