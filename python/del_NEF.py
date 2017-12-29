'''删除没有对应JPG的NEF

我们筛选照片的时候，经常看JPG来筛选，然后删掉对应NEF，这样不需要开启占内存的Lightroom等即可筛选。
这个程序即遍历当前目录下的文件，如果一个NEF没有对应名称的JPG，那么删除它。
'''

import os, sys, shutil

def delNef(file_dir):
	fjpg = 0
	fnef = 0
	countremain = 0
	countdelete = 0
	cnef = []
	cjpg = []

	#存入filename
	for root, dirs, files in os.walk(file_dir):
		for i in files:
			if '.NEF' in i:
				if os.path.exists(i[0:-3]+'JPG') == False:
					#os.remove(i)	#执行删除操作，但有风险
					if os.path.exists('Deleted') == False:
						os.mkdir('Deleted')
					shutil.move(i, 'Deleted//')		#替换为移动到Deleted文件夹
					print('the file {} has been removed!'.format(i))
					countdelete +=1
				else:
					countremain +=1
	print('{} files checked, {} files deleted'.format(countdelete + countremain, countdelete))

delNef(sys.path[0])