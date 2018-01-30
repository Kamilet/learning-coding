'''
辅音字母后随机加一个元音字母
元音字母重复2次
元音字母aeiouy
反向翻译
'''

def translate(song):
    s = 0
    word = []
    while s != len(song):
        word.append(song[s])
        if song[s] in 'aeiouyAEIOUY':
            s += 3
        elif song[s] in ' ?!.':
            s += 1
        else:
            s += 2
    return ''.join(word)

translate("hieeelalaooo") == "hello"
translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
translate("aaa bo cy da eee fe") == "a b c d e f"
translate("sooooso aaaaaaaaa") == "sos aaa"