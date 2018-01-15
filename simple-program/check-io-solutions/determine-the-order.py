'''
输出字母唯一值的排序
'''


def checkio(data):
    # find every pair in data
    pairs = []
    for string in data:
        for i in range(len(string)-1):
            pairs.append([string[i],string[i+1]])
    # build a string without queue
    findata = ''.join(data)
    findata = sorted(set(findata))
    # print(pairs)
    # use a way like Bubble Sort
    while True:
        flag = True
        for pair in pairs:
            index_pair_1 = findata.index(pair[0])
            index_pair_2 = findata.index(pair[1])
            if index_pair_1 > index_pair_2:
                findata[index_pair_1], findata[index_pair_2] =\
                findata[index_pair_2], findata[index_pair_1]
                # print(findata)
                flag = False
        if flag: break
    # print(findata)
    # failed check ["jhgedba","jihcba","jigfdca"]
    # check every pair in findata and fin pairs that never in same string
    for i in range(len(findata)-1):
        flag = True
        for string in data:
            if findata[i] in string and findata[i+1] in string:
                flag = False
        if flag:
            findata[i], findata[i+1] =\
            min(findata[i], findata[i+1]), max(findata[i], findata[i+1])
    return ''.join(findata)


assert checkio(["jhgedba","jihcba","jigfdca"]) == 'jihgefdcba'
# Your result: "jihgfedcba"
assert checkio(["hfecba", "hgedba", "hgfdca"]) == "hgfedcba"
assert checkio(["b", "d", "a"]) == 'abd'
assert checkio(["ghi", "abc", "def"]) == "abcdefghi"
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
    assert checkio(["name", "my", "myke"]) == 'namyke'
    assert checkio(["my", "name", "myke"]) == 'namyke'
    assert checkio(["qwerty", "asdfg", "zxcvb", "yagz"]) == 'qwertyasdfgzxcvb'



'''第四轮凉了
def checkio(data):


    # find every pair in data
    pairs = []
    for string in data:
        for i in range(len(string)-1):
            pairs.append([string[i],string[i+1]])
    # build a string without queue
    findata = ''.join(data)
    findata = sorted(set(findata))
    # print(pairs)
    # use a way like Bubble Sort
    while True:
        flag = True
        for pair in pairs:
            index_pair_1 = findata.index(pair[0])
            index_pair_2 = findata.index(pair[1])
            if index_pair_1 > index_pair_2:
                findata[index_pair_1], findata[index_pair_2] =\
                findata[index_pair_2], findata[index_pair_1]
                flag = False
        if flag: break
    print(findata)
    # return ''.join(data)
    # this failed check with "jhgedba","jihcba","jigfdca"
    # fixed it with same idea

    # findata = ''.join(data)
    # findata = sorted(set(findata))

    length = len(findata)
    while True:
        print(findata)
        flag = True
        for i in range(length-1):
            for queues in data:
                try:
                    index_0 = queues.index(findata[i])
                    index_1 = queues.index(findata[i+1])
                    if index_0 > index_1:
                        findata[i], findata[i+1] = findata[i+1], findata[i]
                        flag = False
                except ValueError:
                    pass
        if flag: break
    print(findata)
    return ''.join(findata)
'''


'''这个方法也凉了……第三轮失败
def connector(strings):
    newstings = strings[0][0]
    repeat = 0
    while True:
        lenth = len(strings)
        if lenth == 0:
            break
        if strings[0][0] == newstings[-1]:
            newstings = ''.join([newstings, strings[0]])
            strings = strings[1:]
            repeat = 0
        elif strings[0][-1] == newstings[0]:
            newstings = ''.join([strings[0], newstings])
            strings = strings[1:]
            repeat = 0
        else:
            strings.append(strings[0])
            strings = strings[1:]
            print(strings,'rolling',newstings)
        if lenth == len(strings):
            repeat += 1
        if repeat >= len(strings):
            print('jump')
            break
    return [newstings] + strings



def checkio(strings):
    strings_copy = strings
    strings = connector(strings)
    print(strings)
    order = list(''.join(strings))
    # order = list(''.join(strings))
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
    if list(''.join(strings_copy)) == order:
        return ''.join(sorted(order))
    else:
        return ''.join(order)

assert checkio(["hfecba","hgedba","hgfdca"]) == "hgfedcba"
assert checkio(["b","d","a"]) == 'abd'
assert checkio(["ghi","abc","def"]) == "abcdefghi"
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
