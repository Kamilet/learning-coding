# -*- coding:utf-8 -*- 

'''使用字典作为伪数据库的图书管理系统，特别初级版，适用于windows

使用字典，所以如果你关闭程序它会失效！
后续版本尝试加入存储txt功能。

'''
__author__ = 'Kamilet (kamilet.cn)'
__version__ = '1.0'	#lastchanged:

import os, sys
import logging	#日志功能
#from . import save-library-list	#预计加入的存储功能

'''------------------不存在的主界面--------------------
主功能输入: 直接显示当前几个人，几本书出借中，共几本书
			exit - 退出程序
			数字 - 符合4位/6位执行程序，否则等于输入'其他'
			newbook - 录入书
			newpeople - 录入人
			其他 - 重置主功能
			listbook - 列出所有的书，并显示在不在库
			listlend - 列出所有被借的书，并显示借的人(编号)
			listpeople - 列出所有人，并显示借的书(编号)
			help - 下面列表
			log - 打开log
			refresh - 刷新
'''
def lib_main_input():
	'''主函数，接受命令，判断命令类别，传递给其他函数处理'''
	lib_overview()	#显示状态
	global switch
	usercommand = input('\n输入“help”获取帮助，输入“exit”退出。\n输入人员或书籍编号以开始：')
	if usercommand == 'exit':
		switch = False
		return
	elif str.isdigit(usercommand):
		inputnumber = str(inputnumber)
		if usercommand <=9999 and usercommand >0:
			#判断为人
			pull_people()
		elif usercommand <=999999 and usercommand >=100000:
			#判断为书
			pull_book()
		else:
			errorinput()
			return
	elif usercommand == 'refresh':
		#这个清屏是假的
		print('\n'*20)
		return
	elif usercommand == 'log':
		print('------------------------------------------------------\n日志被保存在：\n',logging_file)
		os.startfile(logging_file)
		input('您可以随时手动打开或删除该文件，文件已纪录 {} 行。输入任意内容返回主菜单。',countline(logging_file))
		return
	elif usercommand == 'newbook':
		newbook()
	elif usercommand == 'newpeople':
		newpeople()
	elif usercommand == 'listpeople':
		listpeople()
	elif usercommand == 'listbook':
		listbook()
	elif usercommand == 'listlend':
		listlend()
	elif usercommand == 'help':
		print('''
您可使用以下命令：
 exit						-退出程序
 4位数字(1-9999)			-检查这个编号的人员
 6位数字(100000-999999)		-检查这个编号的书籍
 newbook					-录入书籍
 newpeople					-录入人员
 listbook					-列出所有的书，并显示在不在库
 listlend					-列出所有被借的书，并显示借的人(编号)
 listpeople					-列出所有人，并显示借的书(编号)
 log 						-打开日志文件
 refresh					-刷新当前面板'''
)
		input('------------------------------------------------------\n输入任意内容返回主菜单：')
		return
	else:
		input('无效的参数！\n输入任意内容返回主菜单：')
		return


def lib_overview():
	'''状态函数，主函数启动时运行'''
	pass

def listpeople():
	'''人员列表函数'''
	pass

def listbook():
	'''书籍列表函数'''
	pass

def listlend():
	'''所有被借走的书'''
	pass

def newspeople():
	'''录入函数'''
	pass

def newbook():
	'''录入函数'''
	pass

def checkbook():
	'''检查书状态，返还对应人或0，以及借阅次数'''
	pass

def checkpeople():
	'''检查人状态，返还对应书或0，以及借阅次数'''
	pass

def pull_book():
	'''使用编号拉取书的全部状态'''
	pass

def pull_people():
	'''使用编号拉人的全部状态'''
	pass

def countlist():
	'''返回列表的最大编号'''
	pass

def countnowbooks():
	'''返回当前还剩的书'''
	return 0

def errorinput():
	'''输入错误并写入log'''
	pass

def countline(filelib):
	'''检测行数，若不能则返回失败'''
	try:
		lines = len(filelib.readlines())
	except:
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
			bookname,author,price	#书名，作者，价格
			输入错误则返回，无需额外的exit
			自动加入booknumber的key
	newpeople:新增一本书，要求输入一个列表：
			name,age
			输入错误则返回，无需额外的exit
			自动加入peoplenumber的key
	listbook:输出书籍列表：
			booknumber(key),bookname,author,price,lend
			#编号，书名，作者，价格，借出状态
			lend为0输出“在”，lend为1输出“无”
			数字6位：显示书籍信息
	listpeople:输出会员列表：
			peoplenumber(key),name,age,borrow
			#编号，人名，年龄，借书状态
			borrow为0输出“借”，lend为1输出“无”
			数字4位：显示人员信息
'''


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
	{time} : An ERROR occurred.
'''
logging_file = os.path.join(os.getenv('HOMEDRIVE'),
							os.getenv('HOMEPATH'),
							'library_log.log')	#将log放在:'用户/library.log'下

#print('Logging to', logging_file)	#测试用
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s : %(levelname)s : %(message)s',
	filename=logging_file,
	filemode = 'a',
)

def addlog(operror = 0, opsys = 0, add = 0, booknumber = 0, peoplenumber = 0, lend = 0):
	'''输出log的函数'''
	if operror !=0:
		logging.warning("An ERROR occurred.")
	elif opsys == 1:
		logging.debug("\n------------------------------------------------------\n\
The library sys is running\n\
------------------------------------------------------")
	elif opsys == 2:
		logging.debug("\n------------------------------------------------------\n\
The library sys is over\n\
------------------------------------------------------")
	elif (booknumber !=0 and add != 0):	#传入判断的数
		logging.info('A new book 【{}:《{}》】 added.\n\
Now we have {} books.'\
			 .format(str(booknumber).zfill(6),books[booknumber][0],str(booknumber).zfill(6)))
		#用zfill补位
	elif (peoplenumber !=0 and add != 0):	#传入判断的数
		logging.info('A new people 【{}:《{}》】 added.\n\
Now we have {} books.'\
			 .format(str(peoplenumber).zfill(6),people[peoplenumber][0],str(peoplenumber).zfill(6)))
	elif (booknumber !=0 and peoplenumber !=0 and lend == 0):	#传入判断的数
		print(people[peoplenumber][0])
		logging.info('People 【{}:《{}》】 returned {}:{}.\n\
Now we have {} books here.'\
			 .format(str(peoplenumber).zfill(4), people[peoplenumber][0], str(booknumber).zfill(6), books[booknumber][0], countnowbooks()))
	elif (booknumber !=0 and peoplenumber !=0 and lend != 0):	#传入判断的数
		logging.info('A book 【{}:《{}》】 lend to {}:{}.\n\
Now we have {} books here.'\
			 .format(str(booknumber).zfill(6), books[booknumber][0], str(peoplenumber).zfill(4), people[peoplenumber][0], countnowbooks()))
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
给图书馆里放几本书，人员里加一些人
'''
people = {
	1:['kamilet', 24],
	2:['grucy', 15],
	3:['tom', 87],		#没借过书
	4:['jerry', 17],
}
books = {
	1:['时间简史', '史蒂芬霍金',12],
	2:['史记', '司马迁', 14],
	3:['巴黎圣母院', '雨果', 16],
	4:['大英百科全书', '博物院', 60],
	5:['营销管理', '菲利普·科特勒', 32],
}
opreation = {
	1:[1, 2],
	2:[2, 5],
	3:[4, 1],
	4:[1, 2],
	5:[4, 1],
	6:[4, 2],
}
#1次借书+1次还书，会产生1次借阅增加和2次操作
#本来people和books内有'最后操作'和'借书次数'参数，可以计算得到故忽略
#注意key必须从1开始，在程序内新加值不需要担心这个问题，但默认列表不行

'''------------------逻辑--------------------
书不可以同时借给两个人，人也不可以同时借两本书，以opreation.key为依据
书被借与否：
	遍历:操作字典[2]，booknumber出现次数%2 == True #被借出
人是否借了书：
	遍历:操作字典[1]，peoplenumber%2 == True #借书了
'''


'''
程序开始
'''
global switch
switch = True
global inputnumber
addlog(opsys = 1)
while switch == True:
	try:
		lib_main_input()
	except:
		print('执行中发生了一个意外，程序将退出！')
		addlog(operror = 1)
		#反正都出错了，这里尝试为你打开log文件
		os.startfile(logging_file)
		break
#存储函数
addlog(opsys = 2)
input('按任意键退出程序')
