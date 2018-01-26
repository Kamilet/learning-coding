'''
插入、替换和删除均为1步
求前变换为后的步数
'''


def steps_to_convert(line1, line2):
    if len(line1) > len(line2):
        line1, line2 = line2, line1
    if len(line1) == 0:
        return len(line2)-len(line1)
    line1 = list(line1)
    line2 = list(line2)
    _line1 = line1[:]
    _line2 = line2[:]
    k = 0
    switch = 0
    for i in range(len(line2)):
        if line1[k] == line2[i]:
            _line1.remove(line1[k])
            _line2.remove(line2[i])
            switch = 1
        if switch and k < len(line1)-1:
            k += 1
    # print(_line1)
    # print(_line2, '\n')
    return max(len(_line2), len(_line1))


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert steps_to_convert('line1', 'line1') == 0, "eq"
    assert steps_to_convert('line1', 'line2') == 1, "2"
    assert steps_to_convert('line', 'line2') == 1, "none to 2"
    assert steps_to_convert('ine', 'line2') == 2, "need two more"
    # 4, "everything is opposite"
    assert steps_to_convert('line1', '1enil') == 4
    assert steps_to_convert('', '') == 0, "two empty"
    assert steps_to_convert('l', '') == 1, "one side"
    assert steps_to_convert('', 'l') == 1, "another side"
    print("You are good to go!")
