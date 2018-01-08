'''
给定两组词，找出共有词
输入string1，string2
输出string3
'''

def checkio(first, second):
    first = first.split(',')
    second = second.split(',')
    fin = first[:]
    for item in first:
        if item not in second:
            fin.remove(item)
    fin.sort()
    return (','.join(fin) if len(fin) else '')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"