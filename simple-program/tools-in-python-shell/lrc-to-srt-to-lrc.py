#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
srt和lrc的相互转换，只支持1小时内的文件！

注意，将处理所有同路径下的文件！

注意，同名存储（拓展名不同），会直接造成覆盖！
'''

import os
import sys
import re


def checkfills(o_file, mode):
    i = 0
    for root, dirs, files in os.walk(sys.path[0]):  # 遍历当前文件夹
        for f in files:
            if o_file in f:
                if mode == '1':
                    i += trans_srt(f)
                else:
                    i += trans_lrc(f)
    input('有{}个{}文件被处理'.format(i,o_file[1:]))

def trans_srt(f):
    '''srt文件转lrc文件'''
    #仅支持标准的4行一句的srt文件
    if not os.path.exists(f):
        return 0
    print('处理中：{}……'.format(f))
    filename = f[:-3]+'lrc'
    if os.path.exists(filename):
        os.remove(filename)
    t_file = open(filename, 'w', encoding='UTF-8')
    linecount = 0
    for line in open(f, 'r', encoding='UTF-8'):
        if linecount == 0:
            linecount +=1
        elif linecount == 1:
            lrc_t = '['+line[3:8]+'.'+line[9:11]+']'
            linecount +=1
        elif linecount == 2:
            lrc_b = line
            linecount +=1
        else:
            t_file.write(lrc_t+lrc_b)
            linecount = 0
    t_file.close()
    return 1

def trans_lrc(f):
    '''lrc文件转srt文件'''
    #注意，将会使用下一句开始作为上一句结束
    #最后一句会写成5秒
    if not os.path.exists(f):
        return 0
    print('处理中：{}……'.format(f))
    filename = f[:-3]+'srt'
    if os.path.exists(filename):
        os.remove(filename)
    t_file = open(filename, 'w', encoding='UTF-8')
    srt_s = ''
    srt_e = ''
    srt_count = 0
    srt_b = ''
    for line in open(f, 'r', encoding='UTF-8'):
        if srt_count == 0:
            srt_count +=1
            x = 0
            #首句校准
            while line[1+x] != '0':
                x +=1
            srt_e = '00:'+line[1+x:6+x]+','+line[7+x:9+x]+'0'
            srt_b = line[10+x:]+'\n'
        else:
            srt_s = srt_e
            srt_e = '00:'+line[1:6]+','+line[7:9]+'0'
            t_file.write(str(srt_count)+'\n')
            t_file.write(srt_s+' --> '+srt_e+'\n')
            t_file.write(srt_b+'\n')
            srt_b = line[10:]
            srt_count +=1
    t_file.write(str(srt_count)+'\n')
    t_file.write(srt_s+' --> '+srt_e+'\n')
    t_file.write(srt_b+'\n')
    
    if int(srt_s[6:7])<55:
        srt_e = srt_s[:6]+str(int(srt_s[6:7])+5)+srt_s[8:]
    else:
        srt_e = srt_s[:3]+str(int(srt_s[3:4])+1)+':'+str(int(srt_s[6:8])-55)\
                +srt_s[8:]
    t_file.close()
    return 1
    


#Main
mode = input('将srt转化为lrc，请输入1；将lrc转化为srt，请输入2；\n输入后按回车：\n')
if mode == '1':
    o_file = '.srt'
else:
    o_file = ".lrc"
#Go
checkfills(o_file, mode)
