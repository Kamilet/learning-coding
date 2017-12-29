import sys
print('==import mode==')
print('命令行参数为：')
for i in sys.argv:
	print (i)
print('\npython 路径为', sys.path)