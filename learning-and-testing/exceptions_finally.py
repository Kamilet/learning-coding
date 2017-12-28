import sys, time

f = None
try:
	f = open('poem.txt')
	#文件阅读风格
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print(line, end='')
		sys.stdout.flush()	#把对象立刻打印在屏幕上
		print('Press ctrl+c now')
		#确保它能运行一段时间
		time.sleep(2)
except IOError:
	print('Cant find the file poem.txt')
except KeyboardInterrupt:
	print('!! You cancelled the reading from poem.txt')
finally:
	if f:
		f.close()
	print("(Cleaning up: Closed the file")