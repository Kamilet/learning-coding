# -*- coding:utf-8 -*-
'''随机词语生成器

生成随机词语，用于个人的“每日话题”计划。
默认规则：
1.在常用2500字中，随机选出1枚，重复则提醒
（字典在data/words.html，重复字典在data/words-used.html）
（文字表：https://www.qqxiuzi.cn/zh/xiandaihanyu-changyongzi.php#cyz）
2.在字典中，提取内容
（备选字典-post/get：http://xh.5156edu.com/index.php?f_key=%C9%CF&f_type=zi&SearchString.x=16&SearchString.y=12）
（备选字典-get：https://www.zdic.net/hans/字）
'''

__author__ = 'Kamilet (kamilet.cn)'
__version__ = '1.0'  # lastchanged: 2019-08-01

import os, random
import linecache, urllib, requests
import re
# use the followed commant to get requests
# pip install requests

input('\n本程序将生成1个常用汉字，并生成5个使用该汉字词语。\n按下回车键开始：\n')

#生成单文字
pX = random.randint(1, 250)
pY = random.randint(0, 9)
singleWord = linecache.getline('data/words.html', pX)[pY]
usedWord = linecache.getline('data/words-used.html', 2)
hashXY = str(pX*1000+pY)    #查重
#print(usedWord)
if hashXY in usedWord:
    print('\n该关键字已被生成过至少1次！\n')
else:
    addUsed = open('data/words-used.html', 'w', encoding='UTF-8')
    addUsed.seek(0)
    addUsed.truncate()
    addUsed.write('# -*- coding:utf-8 -*-\n')
    addUsed.write(usedWord[:-1])
    addUsed.write(hashXY+',')
    addUsed.close()

#请求组词    #当前使用地址：http://xh.5156edu.com/
reqUrlLead = 'http://xh.5156edu.com/index.php?f_key=%'
reqUrlEnd = '&f_type=zi'
dictUrl = reqUrlLead + urllib.parse.quote(singleWord, encoding='gb2312')[1:] + reqUrlEnd
#以下为发送request并模拟环境的方法，没有必要暂时停用
'''
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'xh.5156edu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
data = {
    'f_key': urllib.parse.quote(singleWord, encoding='gb2312'),
    'f_type': 'zi',
    }
htmlText = requests.get('http://xh.5156edu.com/index.php', headers=headers, data=data)
'''
#以下为简易方法
htmlText = requests.get(dictUrl ,timeout=10)
htmlText = htmlText.content.decode('gbk', errors='ignore')

#处理内容
dRule = re.compile(r'<[^>]+>', re.S)
htmlText = dRule.sub('', htmlText)
htmlText = htmlText.split('\n')
lineFinder = 0
targetText = ''
for line in htmlText:
    if '相关词语' in line:
        lineFinder += 1
        continue
    if lineFinder == 1 and singleWord in line:
        targetText = line.split('  ')
        break
#词语质检
targetText.pop(0)
targetText[-1] = targetText[-1][:-1]

#词语输出
inputCom = '1'
def printWords(number):
    print('\n\n' + '-'*20)
    print('\n' + '基础字：{}'.format(singleWord))
    print('\n' + '-'*20)
    print('\n' + '词汇：{}'.format(random.sample(targetText, number)))
    print('\n' + '-'*20)
    return str(input('\n' + '对输出结果是否满意？输入1即可用基础字重新随机5个词。\n输入其他任意内容退出…'))
while inputCom == '1':
    inputCom = printWords(number = 5)
        
