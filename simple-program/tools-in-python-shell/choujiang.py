# -*- coding:utf-8 -*-
'''抽奖，一二三等奖

1.不允许重复
2.名单一行一个放在choujiang.txt里，同目录
'''

__author__ = 'Kamilet (kamilet.cn)'
__version__ = '1.0'  # lastchanged: 2019-06-01

import os, random

#初始化
def readFile():
    if os.path.exists('choujiang.txt'):
            id_list = []
            for line in open('choujiang.txt','r', encoding='UTF-8'):
                    line = line.strip('\n')
                    if line != '':
                        id_list.append(line)
            return id_list
    else:
            input('错误，文件choujiang.txt不存在')
            return 0
                

#开始
id_list = readFile()
if id_list:
    num = len(id_list)
    prize1st = int(input('本次将从{}人中抽奖。\n请输入一等奖数量：'.format(num)))
    prize2st = int(input('\n请输入二等奖数量：'))
    prize3st = int(input('\n请输入三等奖数量：'))
    if prize1st + prize2st + prize3st > num:
        input('\n错误，中奖人数不能大于总人数！按回车退出。')
    else:
        prize1st_list = []
        prize2st_list = []
        prize3st_list = []
        #开始抽1等奖
        i = 0
        while i < prize1st:
            prize_who = random.randint(0, len(id_list)-1)
            prize1st_list.append(id_list[prize_who])
            id_list.pop(prize_who)
            i+=1
        #开始抽2等奖
        i = 0
        while i < prize2st:
            prize_who = random.randint(0, len(id_list)-1)
            prize2st_list.append(id_list[prize_who])
            id_list.pop(prize_who)
            i+=1
        #开始抽3等奖
        i = 0
        while i < prize3st:
            prize_who = random.randint(0, len(id_list)-1)
            prize3st_list.append(id_list[prize_who])
            id_list.pop(prize_who)
            i+=1
        input('\n一等奖：{}\n二等奖：{}\n三等奖：{}'.format(prize1st_list,prize2st_list,prize3st_list))
