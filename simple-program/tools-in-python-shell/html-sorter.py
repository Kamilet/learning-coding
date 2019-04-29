# -*- coding:utf-8 -*-
'''对纯HTML文档进行整理，测试版

待更新

思路：
1.处理目标文件所有的行，将行首的\t和&nbsp;去除干净。
2.将><之间的空白字符，包括换行处理干净
3.给所有<和</加上新行标记NL，除了：
	行级标签的尾标签a,em,blockquote,li,h1~h8,td,dd,q,label,del
	行内标签span,strong,u,b,s,i,big,abbr,acronym,strike,small,sub,sup,
	忽略的尾标签script,style
4.给单标签和特殊标签加上标记SL，替换NL：
	img,br,input,hr,meta,link,area,base,col,command,embed,keygen,param,source,track,wbr
	a,em,blockquote,li,h1~h8,td,dd,q,label
	span,strong,u,b
	script,style
5.以><为分割，分行
6.从上到下处理：
	遇到NL，此前和现在均为头标签则+1级，向下继承
	遇到NL，此前和现在均为尾标签则-1级，向下继承
	遇到NL，此前和现在分别为头尾则继承上面的等级，向下继承
	遇到SL，当前行+1级，不向下继承
	遇到不带标签的，继承上面的等级，向下继承
7.排错和提示，在顶部输出一个错误或提示信息：
	最末尾的标签级别不是0
	文档含有未处理的javascript或style等
	文档含有可能整理出现问题的标签：applet,button,iframe,ins,map,object,script,figure,video,embed,object,	
	
'''

'''
笔记

需要处理的内容：
①提取所有标签><之间的空白字符。
②将><作为分隔符，将HTML文档内容切片。
③切片每行一个存入数组。
④非/开头下一个是同类级数+1，/开头下一个是同类级数-1，异类同级
⑤单标签处理
⑥非封闭处理
⑦简单语法处理
⑧&nbsp;缩进处理

处理常见单标签
处理方式：将所有关闭改为不关闭，给后续标签降级
img,br,input,hr,meta,link,area,base,col,command,embed,keygen,param,source,track,wbr,

处理常见可能不被封闭的标签
处理方式：向后查询关闭与否，若未关闭，则尝试帮助关闭
thead查询到table
tbody查询到tbody或th或tr或table
th查询到tr或table
tr查询到tr或table
td查询到td或tr或table
li查询到li或ul
p查询到p，仅作降级从不处理
html查询末尾

'''

__author__ = 'Kamilet (kamilet.cn)'
__version__ = '1.0'  # lastchanged: 2019-04-29