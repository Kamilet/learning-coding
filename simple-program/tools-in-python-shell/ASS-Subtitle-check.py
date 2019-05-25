# -*- coding:utf-8 -*-
'''ass字幕处理

1.对ass字幕按照起始时间进行排序
2.保存文件为new-filenamed.ass
3.寻找样式相同且时间重合的字幕

可能仅适用于由Aegisub生成的ass文件！
'''


def kCheckAss(assName):
    assHeader = ''
    assFooter = ''
    assBody = []
    assLineConunt = 0
    formatLine = ''
    for line in open(assName):
        line=line.strip('\n')
        if line[0:8] != 'Dialogue':
            if line[0:6] == 'Format':
                formatLine = line[6:]
            elif assLineConunt == 0:
                assHeader = assHeader + line +'\n'
            else:
                assFooter = assFooter + line +'\n'
        else:
            assBody.append(line[9:])
    assBody = kSortAss(formatLine,assBody)
    writeFile = open('new'+assName,'w')
    writeFile.write(assHeader)
    writeFile.write(assBody[0])
    assFooter.write(assFooter)
    writeFile.close()
    
    input('检查完成，下面的行数可能需要您检查是否时间重叠：\n{}\n'.format(warnLine))
    
def kSortAss(formatLine,assBody):
    tFormatLine = formatLine.strip(',')
    sTime = 0
    eTime = 0
    aStyle = 0
    sortAss = []
    warnLine = []
    newBody = []
    for i in range(0,len(tFormatLine)-1):
        if tFormatLine[i] == 'Start':
            sTime = i
        elif tFormatLine[i] == 'End':
            eTime = i
        elif tFormatLine[i] == 'Style':
            aStyle = i
    for line in assBody:
        tempLine = line.strip(',')
        sTime = converTime(sTime)
        eTime = converTime(eTime)
        sortAss.append[sTime,eTime,tempLine[aStyle],line]
    sortAss.sort()
    assBody = []
    assBody.append('Format:'+formatLine)
    for i in range(0,len(sortAss)-2):
        if sortAss[i][1]>sortAss[i+1][0] and sortAss[i][2] == sortAss[i+1][2]:
            warnLine.append[i]
            assBody.append('Dialogue:'+sortAss[3]+'\n')
    assBody.append('Dialogue:'+sortAss[-1][3]+'\n')
    return assBody,warnLine
    
            

def converTime(time):
    time = time.strip(':')
    return time[0]*60*60+time[1]*60+time[2]
        

    
#Main

import os

assName = input('请输入文件名（可以不包括后缀的.ass）\n')
if assName[-4:] != '.ass':
    assName += '.ass'
if not os.path.exists(assName):
    input('当前文件"{}"不存在，请按回车键退出。\n\n\n'.format(assName))
else:
    kCheckAss(assName)
