# -*- coding:utf-8 -*-
'''抽鬼牌游戏，15牌

如果电脑被发8张牌，你则被发7张。
凑对则丢弃。第一轮弃完后牌少的先抽。
只剩一张鬼牌时，拿着鬼牌的人失败。'''

__author__ = 'Kamilet (kamilet.cn)'
__version__ = '1.0'  # lastchanged: 2018-01-01


import random
from os import system
from sys import exit


def card_sender():
    '''发牌器'''
    global flag
    _cards = genpair()
    _sender = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    random.shuffle(_sender)
    # 初始化牌组
    for i in range(1, 13):
        cards[i] = [_cards[i - 1], _sender[i - 1]]
    cards[15] = ['【Joker】', random.randint(1, 2)]
    _temp = random.randint(1, 2)
    if _temp == 1:
        cards[13] = [_cards[12], cards[15][1]]
        cards[14] = [_cards[13], 3 - cards[15][1]]
    else:
        cards[13] = [_cards[12], 3 - cards[15][1]]
        cards[14] = [_cards[13], 3 - cards[15][1]]
    # 发牌
    # cards[i]的数值
    # cards[i]由花色+数字的列表构成
    # 数字有三种情况: 0表示在弃牌堆
    #                 1表示在玩家手中
    #                 2表示在电脑手中
    flag = 1


def genpair():
    '''生成对子'''
    temp = system("cls")
    suitlist = ['♥', '♠', '♦', '♣']
    # GBK排错
    try:
        print('♥♠♦♣欢迎来到抽鬼牌游戏！♥♠♦♣\n系统正为你发牌和弃牌！\n')
    except UnicodeEncodeError:
        print('****欢迎来到抽鬼牌游戏！****\n系统正为你发牌和弃牌！\n')
        suitlist = ['Heart|', 'Spade|', 'Diamond|', 'Club|']
    numberlist = ['A', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K']
    random.shuffle(numberlist)
    _cards = []
    for i in range(0, 7):
        random.shuffle(suitlist)
        _cards.append(suitlist[0] + numberlist[i])
        _cards.append(suitlist[1] + numberlist[i])
    return _cards


def card_lister():
    '''列出你们的牌'''
    global mycards
    mycards.clear()
    comcards.clear()
    _my = 1
    _com = 1
    for i in range(1, 16):
        if cards[i][1] == 1:
            mycards[_my] = cards[i][0]
            _my += 1
        elif cards[i][1] == 2:
            comcards[_com] = cards[i][0]
            _com += 1


def card_checker():
    '''测试器，丢弃同样的牌'''
    for i in range(1, 8):
        if cards[i * 2 - 1][1] == cards[i * 2][1]:
            _discard = cards[i * 2 - 1][1]
            if _discard == 1:
                print('你凑成了对子，弃掉了牌 {} 和 {} ！'
                      .format(cards[i * 2 - 1][0], cards[i * 2][0]))
            elif _discard == 2:
                print('电脑凑成了对子，弃掉了牌 {} 和 {} ！'
                      .format(cards[i * 2 - 1][0], cards[i * 2][0]))
            cards[i * 2 - 1] = [cards[i * 2 - 1][0], 0]
            cards[i * 2] = [cards[i * 2][0], 0]


def gameplay():
    '''主程序'''
    card_checker()
    card_lister()
    screen()
    global flag
    command = input('输入任意继续(或输入exit退出)：')
    if command == 'exit':
        exit()
    if flag == 1:
        if cards[15][1] == 1:
            picker(1)
        else:
            picker()
            flag = 2
    else:
        picker()
    return flag


def picker(first=2):
    '''挑牌'''
    # 检查pick条件
    global flag
    _check = 0
    for i in range(1, 15):
    	_check += cards[i][1]
    if _check == 0:
    	flag = False
    	return
    # 开始pick
    _pick = random.randint(1, len(comcards))
    try:
        _pickfake = int(input('你选择对手第几张手牌？请输入(1-{})：'.format(len(comcards))))
        temp = system("cls")
        print('你拿走了电脑的第{}张手牌{}！'.format(_pickfake, comcards[_pick]))
    except KeyError:
    	_pickfake = 1
    	print('不存在这张牌，系统帮你选择第一张~')
    	temp = system("cls")
    	print('你拿走了电脑的第{}张手牌{}！'.format(_pickfake, comcards[_pick]))
    except ValueError:
    	_pickfake = 1
    	print('错误的输入，系统帮你选择第一张~')
    	temp = system("cls")
    	print('你拿走了电脑的第{}张手牌{}！'.format(_pickfake, comcards[_pick]))
    while True:
        _picked = random.randint(1, len(mycards))
        if comcards[_pick][1] != mycards[_picked][1]:
        	break
    print('电脑拿走了你的第{}张手牌{}！'.format(_picked, mycards[_picked]))
    for i in range(1, 16):
    	if cards[i][0] == comcards[_pick]:
    		cards[i] = [cards[i][0], 1]
    		continue
    	elif cards[i][0] == mycards[_picked]:
    		cards[i] = [cards[i][0], 2]
    		continue


def summeray():
    '''宣布胜负并开始下回合'''
    temp = system("cls")
    if len(mycards) == 0:
    	print('恭喜你获得胜利！')
    else:
    	print('你输了！')
    command = input('输入任意内容开始新的一轮(或输入exit退出)：')
    temp = system("cls")
    if command == 'exit':
    	exit()


def screen():
    '''显示器'''
    print('-' * 60)
    print('电脑的手牌：')
    print('[ ??? ]，' * len(comcards), end='')
    print('共{}张！\n'.format(len(comcards)))
    print('你的手牌：')
    for i in range(1, len(mycards) + 1):
        print('[', mycards[i], ']，', end='')
    print('共{}张！'.format(len(mycards)))
    print('-' * 60)


# 进程开始
cards = {}
mycards = {}
comcards = {}
flag = 1  # 判断是否游戏结束，0则游戏结束，1则是第一回合，2则是非第一回合
while True:
    card_sender()
    while flag:
        flag = gameplay()
    summeray()