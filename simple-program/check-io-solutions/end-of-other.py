'''
判断所给的一组字符串中，是否某些是某些的结尾。
只要存在一个，返回True
'''


def checkio(words_set):
    words_list = list(words_set)
    for word in words_list:
        for every in words_list:
            flag = True
            if word == every or len(word) >= len(every):
                continue
            # print('check [', word, '] in [ ', every, ' ]')
            for i in range(-1, -len(word)-1, -1):
                # print(word[i], 'in word, and', every[i], 'in every')
                if word[i] != every[i]:
                    flag = False
                    break
            if flag:
                return True
    return False

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
