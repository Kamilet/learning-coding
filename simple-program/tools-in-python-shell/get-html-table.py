# -*- coding:utf-8 -*-
'''table抽取器

提取页面上的所有表格（不支持嵌套），不做其他处理。
个人测试用。

'''

__author__ = 'Kamilet (kamilet.cn)'
__version__ = '1.0'  # lastchanged: 2019-09-28

import os, random
import linecache, urllib, requests, html
import re
# use the followed commant to get requests
# pip install requests
targetUrl = input('输入抓取表格的目标链接：\n')
if targetUrl[:4] == 'http':
    data = requests.get(targetUrl ,timeout=10)
    htmlText = data.text
else:
    data = requests.get('https://'+targetUrl ,timeout=10)
    if str(data.status_code) == '200':
        htmlText = data.text
    else:
        data = requests.get('http://'+targetUrl ,timeout=10)
        htmlText = data.text

table_list = re.findall(r"(?<=table).+?(?=\/table>)" ,htmlText)

for table in table_list:
    print(html.unescape(table))
    print('\n')

input('完成')
