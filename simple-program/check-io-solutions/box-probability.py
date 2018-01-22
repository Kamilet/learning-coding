'''
n个棋子，黑白wb
替换n次
返回n次被换掉的为白的数学期望
'''


def checkio(pearls, steps):
    peals_now = [pearls]
    for i in range(steps-1):
        peals_new = []
        for p in peals_now:
            peals_new += turner(p)
        peals_now = peals_new[:]
    # print(peals_now)
    wincount = 0
    for p in peals_now:
        casecount = 0
        for i in p:
            if i == 'w':
                casecount += 1
        wincount += casecount/len(p)
    wincount /= len(peals_now)
    print(wincount)
    return round(wincount, 2)


def turner(peal):
    peal = list(peal)
    wcount = 0
    while 'w' in peal:
        peal.remove('w')
        wcount += 1
    pcount = len(peal)
    return ['w'*(wcount-1)+'b'*(pcount+1)]*wcount + ['w'*(wcount+1)+'b'*(pcount-1)]*pcount


checkio('bbw', 3) == 0.48
checkio('wwb', 3) == 0.52
checkio('www', 3) == 0.56
checkio('bbbb', 1) == 0
checkio('wwbb', 4) == 0.5
checkio('bwbwbwb', 5) == 0.48
