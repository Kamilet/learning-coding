'''文件处理

输入0压缩一个叫做'test.py'的文件，输入1删除原文件，输入2解压缩，输入3删除压缩包
'''
import os, zipfile

#名称和列表
file_needZip = 'G:\\Documents\\Python\\test.py'	#需要压缩的文件
file_needExtract = file_needZip + '.zip'		#需要解压缩的文件
switch = '0'

#主函数
def file_main(swi):
	if switch == 'exit':
		print('结束')
		return
	elif switch == '0':
		if os.path.exists(file_needZip) == False:
			print('错误，文件不存在')
			return
		zipit(file_needZip)
	elif switch == '1':
		if os.path.exists(file_needZip) == False:
			print('错误，文件不存在')
			return
		os.remove(file_needZip)
	elif switch == '2':
		if os.path.exists(file_needExtract) == False:
			print('错误，文件不存在')
			return
		zipit(file_needExtract)
	elif switch == '3':
		if os.path.exists(file_needExtract) == False:
			print('错误，文件不存在')
			return
		os.remove(file_needExtract)
	else:
		print('无效指令')
		return

def zipit(zi):
	if 'zip' in zi:
		#Go Ext
		z = zipfile.ZipFile(file_needExtract, 'r')  
		print z.read(z.namelist()[0])
	else:
		#Go Zip
		z = zipfile.ZipFile(file_needExtract, 'w') 
		z.write(file_needZip+os.sep+d)
		z.close

#主程序
while switch != 'exit':
	switch = str(input('输入0压缩，输入1删除，输入2解压缩，输入3删除压缩包，输入exit推出'))
	file_main(switch)


'''上述无法工作，参考：
<span style="font-size:18px;"># coding:UTF-8  
import zipfile,os  
  
#把整个文件夹内的文件打包  
path = 'G:\\BaiduMusic\\Images\\'  
zipName = path + 'BaiduMusic_Image.zip'  
  
f = zipfile.ZipFile( zipName, 'w', zipfile.ZIP_DEFLATED )  
for dirpath, dirnames, filenames in os.walk( path ):  
    for filename in filenames:  
        print filename  
        f.write(os.path.join(dirpath,filename))  
f.close()  
  
#将打包的文件解压  
f = zipfile.ZipFile(zipName, 'r')  
for file in f.namelist():  
    f.extract(file, path)</span> 
 '''
