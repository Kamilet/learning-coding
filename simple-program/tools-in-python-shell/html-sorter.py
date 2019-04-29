# -*- coding:utf-8 -*-
'''对纯HTML文档进行整理，测试版

待更新

思路：
①提取所有标签><之间的空白字符。
②将><作为分隔符，将HTML文档内容切片。
③切片每行一个存入数组。
④非/开头下一个是同类级数+1，/开头下一个是同类级数-1，异类同级
⑤单标签处理
⑥非封闭处理
⑥简单语法处理

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