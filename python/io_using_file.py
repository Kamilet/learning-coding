poem ='''\
Programing is fun
When the dork is done
if you wanna make your work also fun:
	use Python!
'''

#打开文件编辑
f = open('poem.txt', 'w')
#中文内容需要以下参数：
#f = open('poem.txt', 'w', encoding='uft-8')
#写入文本
f.write(poem)
#关闭文件
f.close()

#在没有指定的情况下，开启只读模式'r'
f = open('poem.txt')
while True:
	line = f.readline()
	#零长度就EOF
	if len(line) == 0:
		break
	#每行line的末尾都自带换行符，因为读取自文件
	print(line, end='')
#关闭文件
f.close()