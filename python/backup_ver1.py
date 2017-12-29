import os
import time

#需要备份的文件和睦路被指定在列表中
#如Os下， source = ['/Users/swa/notes']
#win下：
source = ['"c:\\My Documents"', 'C:\\Code']
#包含空格，使用双引号

#本份文件在某牡鹿里，Os下，target_dir = '/Users/swa/backup'
#win下：
target_dir = 'E:\\Backup'

#用当前日期和时间构成zip文件名
target = target_dir + os.sep + \
		 time.strftime('%Y%m%d%H%M%S') + '.zip'

#目标目录不存在时创建
if not os.path.exists(target_die):
	os.mkdir(target_dir)

#打包
zip_command = 'zip -r {0) {1}'.format(target,
									  ' ',join(source))

#运行备份
print('Zip command is:')
print('Running:')
is os.system(zip_command) == 0:
	print('Successful backup to', target)
else
	print('Backup FAILED')