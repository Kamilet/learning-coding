'''读取当前文件夹下PY文件，并制作一份MD文件

默认文件头：
---
layout: postcn
title: "python:!!!YOUR FILE NAME!!!"
date: XXXX-XX-XX XX:XX:XX +0800
lang: cn
nav: post
category: python
tags: [python, file]
---

默认文件名：
XXXX-XX-XX-!!!YOUR FILE NAME!!!

以上请在相应位置修改！
'''
import os, sys, re, shutil, time

def trans(f):
	md = open(time.strftime("%Y-%m-%d-", time.localtime())+f[:-4]+'.MD','w')
	all_the_text = open(f,'w','utf-8').read()
	head = '\
	---\n\
	layout: postcn\n\
	title: "python:{}"\n\
	date: {} {} +0800\n\
	lang: cn\n\
	nav: post\n\
	category: python\n\
	tags: [python, file]\n\
	---\n\
	\n\
	* content\n\
	{}'.format(f[:-4], time.strftime("%Y-%m-%d", time.localtime()), time.strftime("%H:%M:%S", time.localtime()), '{:toc}')
	article = '\
	{}\n\
	<!-- more -->\n',format(re.findall(r"(?<=''')[\s\S]*+?(?=''')", all_the_text))
	md.write(head)
	md.write(article)
	md.write(all_the_text)
	md.close()


def checkpys():
	i = 0
	for root, dirs, files in os.walk(sys.path[0]):	#遍历当前文件夹
		for f in files:
			if '.py' in f:
				trans(f)
				i += 1
	print('有{}个py文件被处理'.format(i))

#主执行程序开始
print('当前操作目录：',sys.path[0])
#myorder = input('输入任意字符开始，输入exit退出。注意本程序会将目录内所有py文件转化为MD文件！\n仅复制，源文件不会删除。您要：')
#if myorder == "exit":
#	sys.exit()
print('------')
checkpys()
