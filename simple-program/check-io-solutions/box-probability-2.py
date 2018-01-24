'''
n个棋子，黑白wb
替换n次
返回n次被换掉的为白的数学期望
'''

def checkio(pearls, steps):
    pw = 0
    for peal in pearls:
        if peal == 'w':
            pw += 1
    pb = len(peals) - pw
    



checkio('bbw', 3) == 0.48
checkio('wwb', 3) == 0.52
checkio('www', 3) == 0.56
checkio('bbbb', 1) == 0
checkio('wwbb', 4) == 0.5
checkio('bwbwbwb', 5) == 0.48