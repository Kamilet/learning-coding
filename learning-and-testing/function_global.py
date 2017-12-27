x = 50

def func():
	global x

	print('x is', x) # A space here?
	x = 2
	print('x is changed to ', x)

func()
print('value of x is',x)