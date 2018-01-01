# -*- coding:utf-8 -*-

'''使用python写的2048游戏

操作说明：
1.输入w,a,s,d来进行上下左右的移动
2.输入exit结束游戏
3.输入restart重新开始
4.输入sort作弊'''

__author__ = 'Kamilet (kamilet.cn)'
__version__ = '1.0'  # lastchanged: 2018-01-01

import random
from os import system
from sys import exit


def initialization():
    '''初始化'''
    global gamepad
    global scorce
    global step
    scorce = 0
    step = 0
    gamepad = [[' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ']]
    new_2()
    new_2()
    refresh(1)


def new_2():
    '''在空位中随机插入一个2'''
    global gamepad
    _newdone = False
    #新方法
    _templist = []
    for i in range(0, 4):
        for k in range(0, 4):
            if gamepad[i][k] == ' ':
                _templist.append(i*10+k)
    _cl = random.choice(_templist)
    _column = int(_cl / 10)
    _line = _cl % 10
    gamepad[_column][_line] = 2
    #下面是曾用方法
    '''
    while not _newdone:
        _column = random.randint(0, 3)
        _line = random.randint(0, 3)
        if gamepad[_column][_line] == ' ':
            gamepad[_column][_line] = 2
            _newdone = True
    '''


def refresh(isnew = 0):
    '''清屏并重置显示状态'''
    global gameoverflag
    global step
    global scorce
    global gamepad
    if gameoverflag == 1:
        gameover()
        gameoverflag = 0
        initialization()
        return
    temp = system("cls")
    print('-'* 65)
    print('欢迎游玩2048游戏，输入help获取帮助！\n当前分数：{}，\
历史高分：{}！'.format(scorce, highscorce))
    print('-'* 65)
    print('|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\n\n\
|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\n\n\
|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\n\n\
|\t{}\t|\t{}\t|\t{}\t|\t{}\t|'
          .format(gamepad[0][0], gamepad[0][1], gamepad[0][2], gamepad[0][3],
                  gamepad[1][0], gamepad[1][1], gamepad[1][2], gamepad[1][3],
                  gamepad[2][0], gamepad[2][1], gamepad[2][2], gamepad[2][3],
                  gamepad[3][0], gamepad[3][1], gamepad[3][2], gamepad[3][3]))
    print('-' * 65)
    if isnew:
        temp = input('欢迎开始新游戏，输入w,a,s,d移动：')
        maincontrol(temp)
    else:
        temp = input('第{}步，输入w,a,s,d移动：'.format(step))
        maincontrol(temp)


def maincontrol(temp):
    '''判断用户输入和分发任务的函数'''
    if temp == 'exit':
        exit()
    elif temp == 'restart':
        initialization()
    elif temp in ['w', 'a', 's', 'd']:
        doact(temp)
    elif temp == 'sort':
        sort_cheat()
    elif temp == 'test':
        test()


def sort_cheat():
    global gamepad
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = gamepad
    _count1 = 0
    _count2 = 0
    for i in range(0, 4):
        for k in range(0, 4):
            if gamepad[i][k] != ' ':
                a[_count1] = gamepad[i][k]
                _count1 += 1
            else:
                a[_count1] = 0
    a.sort(reverse = True)
    a[_count1] = 'over'
    for i in range(0, 7):
        for k in range(0, i + 1):
            if k > 3 or i - k > 3:
                continue
            elif a[_count2] == 'over':
                gamepad[k][i - k] = ' '
            else:
                gamepad[k][i - k] = a[_count2]
                _count2 += 1


def doact(temp):
    '''检查是否失败并使用命令'''
    global gameoverflag
    global scorce
    global step
    gameoverflag = 1
    _stepscorce = 0
    for i in range(0, 4):
        for k in range(0, 4):
            if gamepad[i][k] == ' ':
                gameoverflag = 0
            else:
                _stepscorce += gamepad[i][k]
    if gameoverflag:
        return
    # 开始执行输入的命令
    moved = 0
    for i in range(0, 5):
        moved += wasd(temp)
    if moved:
        new_2()
        step += 1
        scorce += _stepscorce
        print(_stepscorce)


def wasd(temp):
    '''执行wasd，1次'''

    global gamepad
    moved = 0
    if temp == 'w':
        for i in range(0, 3):
            for k in range(0, 4):
                if gamepad[i][k] == ' ':
                    if gamepad[i + 1][k] != ' ':
                        moved += 1
                    gamepad[i][k] = gamepad[i + 1][k]
                    gamepad[i + 1][k] = ' '
                else:
                    if gamepad[i][k] == gamepad[i + 1][k]:
                        gamepad[i][k] = gamepad[i][k] * 2
                        gamepad[i + 1][k] = ' '
                        moved += 1
    if temp == 's':
        for i in range(0, 3):
            for k in range(0, 4):
                if gamepad[3 - i][k] == ' ':
                    if gamepad[2 - i][k] != ' ':
                        moved += 1
                    gamepad[3 - i][k] = gamepad[2 - i][k]
                    gamepad[2 - i][k] = ' '
                else:
                    if gamepad[3 - i][k] == gamepad[2 - i][k]:
                        gamepad[3 - i][k] = gamepad[3 - i][k] * 2
                        gamepad[2 - i][k] = ' '
                        moved += 1
    if temp == 'a':
        for i in range(0, 3):
            for k in range(0, 4):
                if gamepad[k][i] == ' ':
                    if gamepad[k][i + 1] != ' ':
                        moved += 1
                    gamepad[k][i] = gamepad[k][i + 1]
                    gamepad[k][i + 1] = ' '
                else:
                    if gamepad[k][i] == gamepad[k][i + 1]:
                        gamepad[k][i] = gamepad[k][i] * 2
                        gamepad[k][i + 1] = ' '
                        moved += 1
    if temp == 'd':
        for i in range(0, 3):
            for k in range(0, 4):
                if gamepad[k][3 - i] == ' ':
                    if gamepad[k][2 - i] != ' ':
                        moved += 1
                    gamepad[k][3 - i] = gamepad[k][2 - i]
                    gamepad[k][2 - i] = ' '
                else:
                    if gamepad[k][3 - i] == gamepad[k][2 - i]:
                        gamepad[k][3 - i] = gamepad[k][3 - i] * 2
                        gamepad[k][2 - i] = ' '
                        moved += 1
    return moved


def gameover():
    '''游戏结束'''
    global scorce
    global highscorce
    if highscorce < scorce:
        highscorce = scorce
    print('-'* 65)
    print('游戏结束！您的得分是{}，历史最高分是{}！'.format(scorce, highscorce))
    input('输入任意键重新开始：')


def test():
    '''直接投降，测试用'''
    global gamepad
    gamepad = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [5, 6, 7, 8]]




step = 0  #用于记录步数
scorce = 0  #用于记录分数
highscorce = 100  #用于记录最高分（不做固化，关闭失效）
gameoverflag = 0
initialization()
while True:
    refresh()