# -*- coding:utf-8 -*-

'''使用字典作为伪数据库的图书管理系统，特别初级版，适用于windows

使用字典，所以如果你关闭程序它会失效！
后续版本尝试加入存储txt功能。

'''
__author__ = 'Kamilet (kamilet.cn)'
__version__ = '1.0'  # lastchanged:

import os
import logging  # 日志功能
import time
# from . import save-library-list  #预计加入的存储功能

'''------------------不存在的主界面--------------------
主功能输入: 直接显示当前几个人，几本书出借中，共几本书
    exit - 退出程序
    数字 - 符合4位/6位执行程序，否则等于输入'其他'
    newbook - 录入书
    newpeople - 录入人
    其他 - 重置主功能
    listbooks - 列出所有的书，并显示在不在库
    listlend - 列出所有被借的书，并显示借的人(编号)
    listpeople - 列出所有人，并显示借的书(编号)
    help - 下面列表
    log - 打开log
    refresh - 刷新'''


def lib_main_input():
    '''主函数，接受命令，判断命令类别，传递给其他函数处理'''
    sortlib()  # 整理全部内容
    lib_overview()  # 显示状态
    usercommand = str(input('\n输入“help”获取帮助，输入“exit”退出。\n输入人员/书籍编号/命令以开始：'))
    if usercommand == 'exit':
        global switch
        switch = False
        return
    elif str.isdigit(usercommand):
        inputnumber = int(usercommand)
        if inputnumber <= 9999 and inputnumber > 0:
            # 判断为人
            pull_people(inputnumber)
        elif inputnumber <= 999999 and inputnumber >= 100000:
            # 判断为书
            pull_book(inputnumber)
        else:
            errorinput()
            return
    elif usercommand == 'refresh':
        # 这个清屏是假的
        print('\n' * 20)
        return
    elif usercommand == 'log':
        print('------------------------------------------------------\
\n日志被保存在：\n', logging_file)
        os.startfile(logging_file)
        input('您可以随时手动打开或删除该文件，文件已纪录 {} 行。\
输入任意内容返回主菜单：'.format(countline(logging_file)))
        return
    elif usercommand == 'newbook':
        newbook()
    elif usercommand == 'newpeople':
        newpeople()
    elif usercommand == 'listpeople':
        listpeople()
    elif usercommand == 'listbooks':
        listbooks()
    elif usercommand == 'listlend':
        listlend()
    elif usercommand == 'help':
        print('''\n\n
您可使用以下命令：
 exit                       -退出程序
 4位数字(1-9999)            -检查这个编号的人员
 6位数字(100000-999999)     -检查这个编号的书籍
 newbook                    -录入书籍
 newpeople                  -录入人员
 listbook                   -列出所有的书，并显示在不在库
 listlend                   -列出所有被借的书，并显示借的人(编号)
 listpeople                 -列出所有人，并显示借的书(编号)
 log                        -打开日志文件
 refresh                    -刷新当前面板''')
        input('------------------------------------------------------\
\n输入任意内容返回主菜单：')
        return
    else:
        errorinput()


'''------------------逻辑--------------------
书不可以同时借给两个人，人也不可以同时借两本书，以opreation.key为依据
书被借与否：
    遍历:操作字典[2]，booknumber出现次数%2 == True
人是否借了书：
    遍历:操作字典[1]，peoplenumber%2 == True'''

def sortlib():
    '''整理函数，将现有的信息重新整理'''
    global changed
    if not changed:  # 之前的操作未涉及图书变化
        return
    else:  # 涉及书籍变化，重新整理
        global dict_books
        global dict_people
        dict_books.clear()
        dict_people.clear()
        for i in range(1, len(books)+1):  # 整理book
            dict_books[i] = sortbook(i)
        for p in range(1, len(people)+1):  # 整理people
            dict_people[p] = sortpeople(p)
        changed = False

def sortbook(i):
    '''重要函数，返还一个词典的单项(实际是元组)：
    书名、作者、价格、被借次数、借阅人编号、借阅人名字、借出日期
        书名-价格：书籍原字典，直接得到
        被借次数：操作字典，遍历key内书编号出现次数，用int(a/2)
        借阅人编号：操作字典，遍历key内书编号直至找到，否则返还数字0
        借阅人名字：编号返还不是0，人员字典内直接得到
        用查找借阅人编号步骤的key，编号字典内直接得到'''
    global books
    global people
    global opreation
    global remainbook
    _count = 0
    _opnu = 0
    for k in range(1, len(books)+1):
        if opreation[k][1] == i + 100000:
            _count += 1
            _opnu = k
    _count = int((_count + 1) / 2)
    if _opnu != 0:
        return books[i+100000] + [_count, opreation[_opnu][0],
               people[opreation[_opnu][0]][0], opreation[_opnu][2]]
    else:
        remainbook += 1
        return books[i+100000] + [_count, '未借出',
               '无', '无']

def sortpeople(p):
    '''重要函数，返还一个词典的单项(实际是元组)：
    人名、年龄、借阅次数、当前在借书编号、当前在借书名字、借阅日期
        人名、年龄：原人员字典，直接得到
        借阅次数：操作字典，遍历key内人员编号出现次数，用int(a/2)
        当前在借书编号：操作字典，遍历key内人编号纸质找到，否则返回数字0
        当前在借书名字：非0即字典查找
        用查找当前在借书编号步骤的key，编号字典内直接得到'''
    global books
    global people
    global opreation
    _count = 0
    _opnu = 0
    for k in range(1, len(people)+1):
        if opreation[k][0] == p:
            _count += 1
            _opnu = k
    _count = int((_count + 1) / 2)
    if _opnu != 0:
        return people[p] + [_count, opreation[_opnu][0],
               books[(opreation[_opnu][0]) + 100000][0], opreation[_opnu][2]]
    else:
        return people[p] + [_count, '未借书',
               '无', '无']


'''------------------抓取和操作--------------------
主要负责直接抓取对应的值以及操作'''


def lib_overview():
    '''状态函数，主函数启动时运行'''
    print('------------------------------------------------------\n\
欢迎进入没有UI的图书管理系统，现在是{}！\n\
该系统当前有图书【{}】本，未借出的有【{}】本！\n\
有【{}】位注册会员喜欢这个书店，虽然它不存在！\n\
------------------------------------------------------'\
           .format(time.strftime("%Y-%m-%d %H:%M:%S",
                   time.localtime(time.time())),
            len(books), remainbook, len(people)), end='')


def errorinput():
    '''输入错误并写入log'''
    addlog(operror=1)
    input('无效的参数！\n输入任意内容返回主菜单：')
    return


def countline(filelib):
    '''检测行数，若不能则返回失败'''
    try:
        lines = len(filelib.readlines())
    except:     # 实际上是错误用法
        return '"统计失败"'
    else:
        return lines

'''------------------结果和二级界面命令--------------------
    数字4位:显示人员信息，不存在报错返回：
            name,age,peopletimes,borrowingnum,borrowingbook,date
            #人名、年龄、借阅次数、当前在借书编号、当前在借书名字、借阅日期
            若无当前再借，输出“未借书”
            exit - 返回主功能
            return - 有书则还书，不存在报错返回
            lend - 借出，输入书编号
    数字6位:显示书籍信息，不存在报错返回：
            bookname,author,price,booktimes,lendingnum,lendingpeople,date
            #书名、作者、价格、被借次数、借阅人编号、借阅人名字、借出日期
            若当前未被借，输出“在库”
            exit - 返回主功能
            return - 被借出则归还，未被借报错返回
            lend - 借出，输入人名
    newbook:新增一本书，要求输入一个列表：
            bookname,author,price    #书名，作者，价格
            输入错误则返回，无需额外的exit
            自动加入booknumber的key
    newpeople:新增一本书，要求输入一个列表：
            name,age
            输入错误则返回，无需额外的exit
            自动加入peoplenumber的key
    listbooks:输出书籍列表：
            booknumber(key),bookname,author,price,lend
            #编号，书名，作者，价格，借出状态
            lend为0输出“在”，lend为1输出“无”
            数字6位：显示书籍信息
    listpeople:输出会员列表：
            peoplenumber(key),name,age,borrow
            #编号，人名，年龄，借书状态
            borrow为0输出“借”，lend为1输出“无”
            数字4位：显示人员信息'''


def listpeople():
    '''人员列表函数'''
    print('会员列表：\n会员编号|  会员姓名|  会员年龄|  借书次数|  \
借阅书籍|  书籍名称|  借阅日期|')
    for i in range(1, len(dict_people) + 1):
        if dict_people[i][4] == '无':
            print('{}|  {}|  {}|  {}|  {}|  {}|  {}|  '
                   .format(str(i).zfill(4),
                           dict_people[i][0], dict_people[i][1],
                           dict_people[i][2], dict_people[i][3],
                           dict_people[i][4], dict_people[i][5]))
        else:
            print('{}|  {}|  {}|  {}|  {}|  《{}》|  {}|  '
                   .format(str(i).zfill(4),
                           dict_people[i][0], dict_people[i][1],
                           dict_people[i][2], str(dict_people[i][3]).zfill(6),
                           dict_people[i][4], dict_people[i][5]))
    try:
        _temp = str(input('------------------------------------------------------\
\n输入任意内容返回主菜单，或会员编号(4位数字)查看详情：'))
        if str.isdigit(_temp) and int(_temp) <= 9999 and int(_temp) > 0:
            pull_people(int(_temp))
    except:
        errorinput()


def listbooks():
    '''书籍列表函数'''
    print('书籍列表：\n书籍编号|  书名|  作者|  价格|  \
被借次数|  借阅人|  姓名|  借阅日期|')
    for i in range(1, len(dict_books) + 1):
        if dict_books[i][5] == '无':
            print('{}|  {}|  {}|  {}|  {}|  {}|  {}|  {}|  '
                   .format(i + 100000,
                           dict_books[i][0], dict_books[i][1],
                           dict_books[i][2], dict_books[i][3],
                           dict_books[i][4], dict_books[i][5],
                           dict_books[i][6]))
        else:
            print('{}|  {}|  {}|  {}|  {}|  {}|  {}|  {}|  '
                   .format(i + 100000,
                           dict_books[i][0], dict_books[i][1],
                           dict_books[i][2], dict_books[i][3],
                           str(dict_books[i][4]).zfill(4), dict_books[i][5],
                           dict_books[i][6]))
    try:
        _temp = str(input('------------------------------------------------------\
\n输入任意内容返回主菜单，或书籍编号(6位数字)查看详情：'))
        if str.isdigit(_temp) and int(_temp) <= 999999 and int(_temp) > 100000:
            pull_book(int(_temp))
    except:
        errorinput()


def listlend():
    '''所有被借走的书'''
    print('所有被借走的书籍列表：\n书籍编号|  书名|  作者|  价格|  \
被借次数|  借阅人|  姓名|  借阅日期|')
    for i in range(1, len(dict_books) + 1):
        if dict_books[i][5] != '无':
            print('{}|  {}|  {}|  {}|  {}|  {}|  {}|  {}|  '
                   .format(i + 100000,
                           dict_books[i][0], dict_books[i][1],
                           dict_books[i][2], dict_books[i][3],
                           str(dict_books[i][4]).zfill(4), dict_books[i][5],
                           dict_books[i][6]))
    try:
        _temp = str(input('------------------------------------------------------\
\n输入任意内容返回主菜单，或书籍编号(6位数字)查看详情：'))
        if str.isdigit(_temp) and int(_temp) <= 999999 and int(_temp) > 100000:
            pull_book(int(_temp))
    except:
        errorinput()


def newpeople():
    '''录入函数'''
    pass


def newbook():
    '''录入函数'''
    pass


def pull_book(num):
    '''使用编号拉取书的全部状态并编辑'''
    global changed
    try:
        if num > len(books):
            input('无效的输入，书籍编号应该是可用的6位数字！\
\n您可以在主菜单使用listbooks命令查看可用的编号。输入任意内容回到主菜单：')
            return
    except:
        errorinput()
        return
    print('------------------------------------------------------\
\n当前图书代码：{}|  书名：{}|  作者：{}|  价格：{}|\
\n被借次数：{}|  '.format(str(num).zfill(6), dict_books[num][0],
                   dict_books[num][1], dict_books[num][2],
                   dict_books[num][3], end=''))
    if dict_books[num][5] != '无':  #书被借走的情况
        print('当前借阅：{}|  借阅人姓名：{}|  借阅日期：{}'
               .format(dict_books[num][4], dict_books[num][5],
                dict_books[num][6]))
        _command = input('------------------------------------------------------\
\n输入return确认该书归还，否则退出：')
        if _command == 'return':
            opreation[len(opreation) + 1] = [dict_books[num][4], num,
            time.strftime("%Y-%m-%d", time.localtime(time.time()))]
            changed = True
            addlog(booknumber=num, peoplenumber=dict_books[num][4])
            input('------------------------------------------------------\
\n还书成功，输入任意内容返回主菜单：')
    else:  #书没被借走
        _command = input('这本书当前未借出。输入会员代码借给某会员，输入exit返回：')
        try:
            if _command > len(people):
                input('无效的输入，会员代码应该是可用的4位数字！\
\n您可以在主菜单使用listpeople命令查看可用的编号。输入任意内容回到主菜单：')
                return
            elif _command == 'exit':
                return
        except:
            errorinput()
            return
        opreation[len(opreation) + 1] = [_command, num,
        time.strftime("%Y-%m-%d", time.localtime(time.time()))]
        changed = True
        addlog(booknumber=num, peoplenumber=_command, lend=1)
        input('------------------------------------------------------\
\n借书成功，输入任意内容返回主菜单：')


def pull_people(num):
    global changed
    '''使用编号拉取人的全部状态并编辑'''
    try:
        if num > len(people):
            input('无效的输入，会员代码应该是可用的4位数字！\
\n您可以在主菜单使用listbooks命令查看可用的编号。输入任意内容回到主菜单：')
            return
    except:
        errorinput()
        return
    print('------------------------------------------------------\
\n当前会员代码：{}|  姓名：{}|  年龄：{}|\
\n借书次数：{}|  '.format(str(num).zfill(4), dict_people[num][0],
                   dict_people[num][1],  dict_people[num][2], end=''))
    if dict_people[num][4] != '无':  # 借了书的情况
        print('当前借阅：{}|  书名：{}|  借阅日期：{}'
               .format(dict_people[num][3], dict_people[num][4],
                dict_people[num][5]))
        _command = input('------------------------------------------------------\
\n输入return确认该书归还，否则退出：')
        if _command == 'return':
            opreation[len(opreation) + 1] = [num, dict_people[num][3],
            time.strftime("%Y-%m-%d", time.localtime(time.time()))]
            changed = True
            addlog(booknumber=num, peoplenumber=dict_books[num][4])
            input('------------------------------------------------------\
\n还书成功，输入任意内容返回主菜单：')
    else:
        _command = input('该会员未借书，请输入书籍代码借给他某本书，输入exit返回：')
        try:
            if _command > len(people):
                input('无效的输入，书籍代码应该是可用的6位数字！\
\n您可以在主菜单使用listbooks命令查看可用的编号。输入任意内容回到主菜单：')
                return
            elif _command == 'exit':
                return
        except:
            errorinput()
            return
        opreation[len(opreation) + 1] = [num, _command,
        time.strftime("%Y-%m-%d", time.localtime(time.time()))]
        changed = True
        addlog(booknumber=_command, peoplenumber=num, lend=1)
        input('------------------------------------------------------\
\n借书成功，输入任意内容返回主菜单：')


'''------------------生产log--------------------
希望在下述场景产生log并存入：
    系统开启：
    {time} : -----------------------------------
             The library sys is running
             -----------------------------------
    系统关闭：
    {time} : -----------------------------------
             The library sys is over
             -----------------------------------
    新书添加成功：
    {Time} : A new book {booknumber}:{bookname} added.
             Now we have {booknumber} books.
    新人添加成功：
    {Time} : A new people {peoplenumber}:{name} added.
             Now we have {peoplenumber} books.
    有人借书：
    {Time} : A book {booknumber}:{bookname} lend to {peoplenumber}:{name}.
             Now {countbooks} books here.
    有人还书：
    {Time} : People {peoplenumber}:{name} returned {booknumber}:{bookname}.
             Now {countbooks} books here.
    产生任何可挽回的错误：
    {time} : An ERROR occurred.'''


logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                            os.getenv('HOMEPATH'),
                            'library_log.log')  # 将log放在:'用户/library.log'下

# print('Logging to', logging_file)	#测试用
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='a',
)


def addlog(operror=0, opsys=0, add=0, booknumber=0, peoplenumber=0, lend=0):
    '''输出log的函数'''
    if operror != 0:
        logging.warning("An ERROR occurred.")
    elif opsys == 1:
        logging.debug("\n------------------------------------------------------\n\
The library sys is running\n\
------------------------------------------------------")
    elif opsys == 2:
        logging.debug("\n------------------------------------------------------\n\
The library sys is over\n\
------------------------------------------------------")
    elif (booknumber != 0 and add != 0):  # 传入判断的数
        logging.info('A new book 【{}:《{}》】 added.\n\
                      Now we have {} books.'
                     .format(str(booknumber).zfill(6),
                             books[booknumber][0], str(booknumber).zfill(6)))
        # 用zfill补位
    elif (peoplenumber != 0 and add != 0):  # 传入判断的数
        logging.info('A new people 【{}:《{}》】 added.\n\
                      Now we have {} books.'
                     .format(str(peoplenumber).zfill(6),
                             people[peoplenumber][0],
                             str(peoplenumber).zfill(6)))
    elif (booknumber != 0 and peoplenumber != 0 and lend == 0):  # 传入判断的数
        print(people[peoplenumber][0])
        logging.info('People 【{}:《{}》】 returned {}:{}.\n\
                      Now we have {} books here.'
                     .format(str(peoplenumber).zfill(4),
                             people[peoplenumber][0],
                             str(booknumber).zfill(6), books[booknumber][0],
                             remainbook))
    elif (booknumber != 0 and peoplenumber != 0 and lend != 0):  # 传入判断的数
        logging.info('A book 【{}:《{}》】 lend to {}:{}.\n\
                      Now we have {} books here.'
                     .format(str(booknumber).zfill(6), books[booknumber][0],
                             str(peoplenumber).zfill(4),
                             people[peoplenumber][0],
                             remainbook))
    else:
        logging.warning("Warning! An unknow opreation.")


'''------------------字典--------------------
书字典：
    booknumber,bookname,author,price
    #书编号、书名、作者、价格
人字典：
    peoplenumber,name,age
    #人编号、人名、年龄
操作字典：
    opnumber,peoplenumber,booknumber
    #操作代码，人编号，书编号

------------------初始--------------------
给图书馆里放几本书，人员里加一些人'''

people = {
    1: ['kamilet', 24],
    2: ['grucy', 15],
    3: ['tom', 87],  # 没借过书
    4: ['jerry', 17],
}
books = {
    100001: ['时间简史', '史蒂芬霍金', 12],
    100002: ['史记', '司马迁', 14],
    100003: ['巴黎圣母院', '雨果', 16],
    100004: ['大英百科全书', '博物院', 60],
    100005: ['营销管理', '菲利普·科特勒', 32],
}
opreation = {
    1: [1, 100002, '2017-11-12'],
    2: [2, 100005, '2017-11-12'],
    3: [4, 100001, '2017-11-12'],
    4: [1, 100002, '2017-11-13'],
    5: [4, 100001, '2017-12-17'],
    6: [4, 100002, '2017-12-18'],
}
# 1次借书+1次还书，会产生1次借阅增加和2次操作
# 本来people和books内有'最后操作'和'借书次数'参数，可以计算得到故忽略
# 注意key必须从1开始，在程序内新加值不需要担心这个问题，但默认列表不行


'''程序开始'''


switch = True  # 主函数开关
changed = True  # 修改检查
dict_books = {}  # 存储书籍的空字典
dict_people = {}  # 存储人员的空字典
remainbook = 0  #剩下几本书
addlog(opsys=1)
while switch:
    lib_main_input()
    '''
    try:
        lib_main_input()
    except:     # 错误用法
        print('执行中发生了一个意外，程序将退出！')
        addlog(operror=1)
        # 反正都出错了，这里尝试为你打开log文件
        os.startfile(logging_file)
        break
    '''
# 后续这里加存储函数
addlog(opsys=2)
input('按任意键退出程序')
