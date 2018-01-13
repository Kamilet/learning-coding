'''
输出字母唯一值的排序
'''
def checkio(strings):
    # order = list(strings[0])
    order = list(''.join(strings))
    for string in strings[1:]:
        print(order,'forbegin')
        print(string,'under')
        _temp = []
        for alpha in range(len(string)):
            _temp.append(string[alpha])
        for i in range(len(string)):
            _insert_point = order.index(string[i])
            order = order[:_insert_point] + _temp + order[_insert_point:]
        print(order,'forend')

    # sort the set(order) as origin queue
    order = sorted(set(order),key=order.index)
    print(order,'result')
    return ''.join(order)



assert checkio(["acb", "bd", "zwa"]) == "zwacbd"
assert checkio(["klm", "kadl", "lsm"]) == "kadlsm"
assert checkio(["a", "b", "c"]) == "abc"
assert checkio(["aazzss"]) == "azs"
assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg"


if __name__ == '__main__':

    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
    assert checkio(["name","my","myke"]) == 'namyke'
    assert checkio(["my","name","myke"]) == 'namyke'
    assert checkio(["qwerty","asdfg","zxcvb","yagz"]) == 'qwertyasdfgzxcvb'


'''
def checkio(strings):
    order = list(strings[0])
    for string in strings[1:]:
        _temp = []
        for alpha in range(len(string)):
            _temp.append(string[alpha])
        _flag = True
        for i in range(len(string)):
            if string[i] in order:
                _insert_point = order.index(string[i])
                order = order[:_insert_point] + _temp + order[_insert_point:]
                _flag = False
        if _flag:
            order = order + _temp
    # sort the set(order) as origin queue
    order = sorted(set(order),key=order.index)
    print(order)
    return ''.join(order)
失败：assert checkio(["qwerty","asdfg","zxcvb","yagz"]) == 'qwertyasdfgzxcvb'
    '''

'''
def checkio(strings):
    # 插入和后缀处理
    # order = list(strings[0])
    order = list(''.join(strings))
    for string in strings[1:]:
        print(order,'forbegin')
        print(string,'under')
        _temp = []
        for alpha in range(len(string)):
            _temp.append(string[alpha])
        for i in range(len(string)):
            _insert_point = order.index(string[i])
            order = order[:_insert_point] + _temp + order[_insert_point:]
        print(order,'forend')
    
    # sort the set(order) as origin queue
    order = sorted(set(order),key=order.index)
    print(order,'result')
    return ''.join(order)
    接近答案！'''