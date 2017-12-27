'''在XML文件里抓取url

用于百度手工提交，每次都复制下来删东西太麻烦了
需要requests库：
$ curl -OL https://github.com/kennethreitz/requests/zipball/master
$ python setup.py install
'''


import os, re, requests


xmlfile = input('键入一个网址，如kamilet.cn，要求kamilet.cn/sitemap.xml存在:')
print('在本页面上抓取：http://' + xmlfile + '/sitemap.xml')
r = requests.get('http://' + xmlfile + '/sitemap.xml') #正式用
#r = requests.get('http://kamilet.cn/sitemap.xml') #测试用
data = r.text

#查找data内符合条件的内容
#<loc>*</loc>标签为查找目标
link_list =re.findall(r"(?<=<loc>).+?(?=</loc>)" ,data)
#写入url.txt，方式为覆盖，不存在则创建
i = 0
f = open('url.txt','w')	#改为'a'可进行追加，不推荐
for url in link_list:
    f.write('\n'+ url)
    i +=1
f.close()

input('抓取完成，本次抓取数据{}个，按任意键退出'.format(i))