'''检查身份证号是否合法/Check if ID is legal

检查位数/内容/生日/校验码
'''


def checkId(cid):
	#位数检查
	if len(cid) != 18:
		return 'wrong length'
	#逐个检查是否数字
	for i in range(0,16):
		if not(cid[i].isdigit()):
			return 'wrong'
	if cid[17] != 'X' and not(cid[17].isdigit()):
		return 'wrong'
	#X赋值
	if cid[17] == 'X':
		str18 = 10
	else:
		str18 = int(cid[17])
	#区号检查（粗略）
	#如果希望的话，加入一个字典来检查，后续如有闲心更新会加入
	if int(cid[0:6]) < 100000 or int(cid[0:6]) > 700000:	#[]是一个前闭后开区间
		return 'wrong area'
	#生日检查（粗略）
	if int(cid[6:14]) < 19000101 or int(cid[6:14]) > 20171231:
		return 'wrong birthday'
	#校验码检查
	#如果可以的话，import time来进行检查
	a = int(cid[0])*7 + int(cid[1])*9 + int(cid[2])*10 + int(cid[3])*5 +\
	int(cid[4])*8 + int(cid[5])*4 + int(cid[6])*2 + int(cid[7]) + int(cid[8])*6 +\
	int(cid[9])*3 + int(cid[10])*7 + int(cid[11])*9 + int(cid[12])*10 + int(cid[13])*5 +\
	int(cid[14])*8 + int(cid[15])*4 + int(cid[16])*2
	a%=11
	if a + str18 != 12:
		return 'wrong safe number'
	return 'may right ID'

for line in open('myid.txt'):
	line=line.strip('\n')
	print('The number:[',line,']',checkId(str(line)))