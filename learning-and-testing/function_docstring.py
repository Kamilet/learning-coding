def print_max(x, y):
	'''Prints the maxium of two numbers.

	The two values must be integers'''
	#第一行以大写字母开始，句号结束。第二行空行，第三行开始说明
	x = int(x)
	y = int(y)

	if x > y:
		print(x, 'is maximum')
	else:
		print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
help(print_max)