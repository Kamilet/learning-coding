'''
返还第二个字符串在第一个字符串中第二个的位置
如果第二个不是空格，返回忽略空格的字母位置
如果第二个是空格，返回空格位置
从0开始
'''
def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    count = 0
    #if symbol != ' ':
    #    text = ''.join(text.split(' '))
        # split方法把str变成了list
        # 虽然是额外的发现，但是是我审题不清，不需要去掉空格！
    for i in range(len(text)):
        if text[i] == symbol:
            count += 1
            if count == 2:
                return i
    return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
