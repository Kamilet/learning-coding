number = 23
guess = int(input('Enter an interger : '))

if guess == number:
	# 新块开始
	print('Congratulations, you guessed it.')
	print('but you don not win any prizes')
	# End
elif (guess < number) and ((number - guess)**2 < 5):
	# 新块开始
	print('close in 5.')
	# End
else:
	# Start
	print('long way from.')
	# End
print('done')
#在if执行后执行