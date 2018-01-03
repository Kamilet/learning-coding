#!/usr/bin/python  
# -*- coding: utf-8 -*-

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
    if not os.path.exists(f):
        return 0
    print(f)
    filename = time.strftime("%Y-%m-%d-", time.localtime())+f[:-3]+'.MD'
    if os.path.exists(filename):
        os.remove(filename)
    md = open(filename,'w', encoding='UTF-8')
    all_the_text = open(f,'r', encoding='UTF-8').read()
    briefing = re.compile("'''"+'(.*?)'+"'''",re.S).findall(all_the_text)
    head = '\
---\n\
layout: postcn\n\
title: "python:{}"\n\
date: {} {} +0800\n\
lang: [cn, en, tw]\n\
nav: post\n\
category: python\n\
tags: [python, file]\n\
---\n\
\n\
* content\n\
{}\n\n'.format(f[:-3], time.strftime("%Y-%m-%d", time.localtime()), time.strftime("%H:%M:%S", time.localtime()), '{:toc}')
    md.write(head)
    md.write(briefing[0])
    md.write('<!-- more -->\n')
    md.write('{% highlight ruby lineno %}\n')
    md.write(all_the_text)
    md.write('\n{% endhighlight %}')
    md.close()
    return 1


def checkpys():
    i = 0
    for root, dirs, files in os.walk(sys.path[0]):    #遍历当前文件夹
        for f in files:
            if '.py' in f:
                i += trans(f)
    input('有{}个py文件被处理'.format(i))

#主执行程序开始
print('当前操作目录：',sys.path[0])
#myorder = input('输入任意字符开始，输入exit退出。注意本程序会将目录内所有py文件转化为MD文件！\n仅复制，源文件不会删除。您要：')
#if myorder == "exit":
#    sys.exit()
print('------')
checkpys()
