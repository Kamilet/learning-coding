while True:
	s = input('Enter something : ')
	if s == 'quit':
		break
	if len(s) < 3:
		print('Too short!')
		continue
	print('I feel comfortable with this length emm..')
	#长度小于3，则上述不执行