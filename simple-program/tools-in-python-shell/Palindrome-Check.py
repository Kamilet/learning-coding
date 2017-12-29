'''判断是否是回文文本

忽略大小写，忽略空格，忽略标点符号
'''
import re

def reverse(text):
	return text[::-1]	#反转文本

def standardization(text):
	#stan_str = text.strip('"').strip("'")	#删除文本中的某些内容
	stan_str = re.sub('[,.?!:; ，。？！：；"]', '', text)
	stan_str = re.sub("[']", "", stan_str)
	return stan_str.lower()	#大写转小写

text = input('本程序可以判断一个文本是不是回文，部分支持中文。\n您可以键入一个文本：')
if standardization(text) == standardization(reverse(text)):
	print('是回文！')
else:
	print('不是回文！')
#print(standardization(text))
#print(standardization(reverse(text)))
input('按任意键退出')