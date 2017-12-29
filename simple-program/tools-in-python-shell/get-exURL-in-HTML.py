'''找到页面里的外链

下载一个页面，检查里面的外链，输出exurl.txt
需要requests库：
$ curl -OL https://github.com/kennethreitz/requests/zipball/master
$ python setup.py install
'''


import os, re, requests


htmlfile = input('键入一个网址，如kamilet.cn/about，抓取当前的html内容:')
mainurl = input('键入主域名，如kamilet.cn，或子站如coding.kamilet.cn:') #正式用
#mainurl = 'kamilet.cn' #测试用
print('在本页面上抓取：http://' + htmlfile)
r = requests.get('http://' + htmlfile) #正式用
#r = requests.get('http://kamilet.cn/about') #测试用
data = r.text

#查找data内符合条件的内容
#<loc>*</loc>标签为查找目标
link_list =re.findall(r"(?<=href=\").+?(?=\")" ,data)
#写入url.txt，方式为覆盖，不存在则创建
i = 0
k = 0
f = open('exurl.txt','w')	#改为'a'可进行追加，不推荐
for url in link_list:
	if mainurl in url:
		i +=1
	elif '//' in url:
		f.write('\n'+ url)
	else:
		i +=1
	k +=1
f.close()

input('抓取完成，本次抓取数据{}个，{}个被识别为外链，按任意键打开文件，关闭文件时本程序自动退出'.format(k, k-i))
os.popen('exurl.txt') 