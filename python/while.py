number = 23
running = True
count = 0

while running:
	guess = int(input('Enter an interger : '))

	if guess == number:
		print('you get it')
		#循环终止
		running = False
		count += 1
	elif guess < number:
		print('no, lighter')
		count += 1
	else:
		print('No, lower')
		count +=1
else:
	print('loop over')
	#循环完成，

print('Done, you tried {} times.'.format(count))
