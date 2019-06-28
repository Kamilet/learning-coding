'''用自定义函数数值替换指定字符串并保存

假设每行只有一个。

当前：读取slide-01.svg，用递增16位字符串替换#FFFFFF。

用于个人一个绘图项目，希望把#000000到#FFFFFF，按照1步进递增的条带画出来。
'''

import os

def exchangeInMyWay(fileName):
    writeC = ''
    counterA = 0
    fileOpen = open(fileName,'r')
    # replace this
    target = '#FFFFFF'
    targetLong = len(target)
    for line in fileOpen:
        if target in line:
            # replace this
            hexA = hex(counterA)[2:]
            hexA = (6 - len(hexA)) * '0' + hexA
            line = line.replace(target, '#'+hexA, 1)
            counterA += 1
        writeC += line
    writeFile = open('1_'+fileName, 'w')
    writeFile.write(writeC)
    writeFile.close()
    fileOpen.close()
    #input(counterA)



exchangeInMyWay('slide-01.svg')
