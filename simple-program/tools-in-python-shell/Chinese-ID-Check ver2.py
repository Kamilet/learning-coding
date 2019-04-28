# -*- coding:utf-8 -*-
'''检查身份证号是否合法，版本2

身份证号码每行一条储存在myid.txt内，和本py文件同目录
检查位数/内容/生日/校验码，另存为新文档myid-checked.csv
新文档内每行格式为：
序号,身份证号,检验结果（正确/错误）,性别,如错误原因

错误原因包括（按照检查顺序）：
①包含非法字符（最后一位不是数字或X，其他位数有不是数字的）
②位数错误（非15位/18位）
③旧版身份证号（15位）
④区号不存在（1-2位：01-82，3-4位：01-70）
⑤出生日期错误（和当前差距超过150年，或月日无效）
⑥校验码错误
'''

__author__ = 'Kamilet (kamilet.cn)'
__version__ = '1.0'  # lastchanged: 2019-04-28

import time, os

#错误代码翻译器
error_code_cn = {1:'包含非法字符',2:'位数错误',3:'旧版身份证号',4:'区号不存在',5:'出生日期错误',6:'校验码错误'}
error_code_en = {1:'Illegal ID Num',2:'Wrong Length',3:'Old ID Version',4:'Wrong Area Code',5:'Wrong Birth Date',6:'Check Failed'}
sex_code_cn = {1:'男',0:'女'}
sex_code_en = {1:'Male',0:'Female'}
#初始化数组
def readFile():
        if os.path.exists('myid.txt'):
                id_list = []
                for line in open('myid.txt'):
                        line = line.strip('\n')
                        id_list.append(line)
                return id_list
        else:
                input('错误，文件myid.txt不存在')

#检查并返回错误码
def checkId(cid, thisYear):
	#非法字符检查
	for i in range(0,16):
		if not(cid[i].isdigit()):
			return 1
	if cid[17] != 'X' and not(cid[17].isdigit()):
		return 1
	#位数检查
	if len(cid) != 18:
		if len(cid) == 15:
			return 3
		else:
			return 2
	#区号检查
	if int(cid[0:2]) > 82 or int(cid[2:4]) >70:
		return 4
	#生日检查
	idYear = int(cid[6:10])
	idMonth = int(cid[10:12])
	idDay = int(cid[12:14])
	if idYear < thisYear - 150 or idYear > thisYear:
		return 5
	if idMonth == 0 or idMonth > 12 or idDay == 0:
		return 5
	else:
		if idMonth in [1,3,5,7,8,11,12] and idDay > 31:
			return 5
		elif idMonth in [4,6,9,10] and idDay > 30:
			return 5
		else:
			if idMonth == 2 and idDay >29:
				return 5
			elif idMonth == 2 and idDay == 29:
				if idYear%4 != 0 or idYear%100 == 0:
					return 5
	#校验码检查
	if cid[17] == 'X':
		str18 = 10
	else:
		str18 = int(cid[17])
	checkNum = int(cid[0])*7 + int(cid[1])*9 + int(cid[2])*10 + int(cid[3])*5 +\
	int(cid[4])*8 + int(cid[5])*4 + int(cid[6])*2 + int(cid[7]) + int(cid[8])*6 +\
	int(cid[9])*3 + int(cid[10])*7 + int(cid[11])*9 + int(cid[12])*10 + int(cid[13])*5 +\
	int(cid[14])*8 + int(cid[15])*4 + int(cid[16])*2
	if checkNum%11 + str18 != 12:
		return 6
	return 0
	
def checkMain(lang = "cn"):
	input('请将身份证号1行1个存为myid.txt并放在本脚本同一目录下，按下回车键开始')
	id_list = readFile()
	thisYear = int(time.strftime("%Y"))
	count = 0
	writeFile = open('myid-checked.csv','w')
	newLine = 'idChecking'
	for cid in id_list:
		count += 1
		checkCode = checkId(cid, thisYear)
		if checkCode == 0:
			if lang == "cn":
				newLine = '{},{},正确,{},/'.format(count,cid,sex_code_cn[int(cid[16])%2])
			else:
				newLine = '{},{},Right,{},/'.format(count,cid,sex_code_en[int(cid[16])%2])
		else:
			if lang == "cn":
				newLine = '{},{},错误,/,{}'.format(count,cid,error_code_cn[checkCode])
			else:
				newLine = '{},{},Wrong,/,{}'.format(count,cid,error_code_cn[checkCode])
		writeFile.write(newLine+'\n')
	writeFile.close()
	input('检查完成，共检查了{}个身份证号，请用Excel或文本编辑器打开myid-checked.csv'.format(count))
	
checkMain("cn")
