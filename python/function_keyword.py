def func(a, b=5, c=10):
	print('a is', a, 'b is', b, 'c is', c)

x=3
y=2
func(3, 7, x+y)
func(25, c=24)
func(c=50, a=100)