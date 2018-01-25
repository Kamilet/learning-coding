'''
n个棋子，黑白wb
替换n次
返回n次被换掉的为白的数学期望
'''

'''
数学归纳法纸上证出公式……
'''

def checkio(pearls, step):
    p = len(pearls)
    pw = 0
    for peal in pearls:
        if peal == 'w':
            pw += 1
    for i in range(1, step):
        pw = (p-2)*pw + p**i
    pw /= (p**step)
    # print(round(pw,2))
    return round(pw,2)
    



checkio('bbw', 3) == 0.48
checkio('wwb', 3) == 0.52
checkio('www', 3) == 0.56
checkio('bbbb', 1) == 0
checkio('wwbb', 4) == 0.5
checkio('bwbwbwb', 5) == 0.48