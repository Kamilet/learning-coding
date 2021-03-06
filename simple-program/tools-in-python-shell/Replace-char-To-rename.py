'''替换当前文件夹下所有文件名内的某些字符

批量重命名，特别方便
'''
import os, sys, re, shutil

def delchar(ochar, f, rchar):
	newname = f.replace(ochar, rchar)
	print('The file "{}" has changed name to "{}"'.format(f, newname))
	return newname

def delnumber(f, rchar):
	times = input('------\n若干数字组合如"123"会被作为一个数字处理！\n确保您输入了一个数字！\n您要替换几个数字？输入"0"替换所有：')
	#newname = re.sub(r'\d', rchar, f, times)	#错误写法，没学会
	newname = re.sub(r'([\d]+)', rchar, f, times)	#网络摘抄
	print('The file "{}" has changed name to "{}"'.format(f, newname))
	return newname

def rename(ochar, rchar):
	i = 0
	for root, dirs, files in os.walk(sys.path[0]):	#遍历当前文件夹
		for f in files:
			if ochar != 'mum':	#处理非mum的情况
				if ochar in f:
					newname = delchar(ochar, f, rchar)
					shutil.move(f, newname)
					i += 1
			else:	#处理mum的情况
				if re.search(r'\d', f):	#摘抄
					newname = delnumber(f, rchar)
					shutil.move(f, newname)
					i += 1
	return i

#主执行程序开始
print('当前操作目录：',sys.path[0])
ochar = input('输入任意字符，当前文件夹下这些字符将被替换。\n注意这个操作是有风险的。\
	\n输入"mum"可替换所有的数字！\n输入"exit"可取消操作。\n你要替换的字符：')
if ochar == "exit":
	sys.exit()
rchar = input('------\n你要将"{}"替换为哪个字符？\n输入"exit"可取消操作。\n你要将它们替换成：'.format(ochar))
if rchar == "exit":
	sys.exit()
print('------')
i = rename(ochar, rchar)
print('处理完成，有{}被处理！'.format(i))
input('按任意键退出')
