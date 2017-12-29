x = 50

def fonc(x):
	print('x is', x)
	x = 2
	print('Changed local x to', x)

fonc(x)
print('x is still', x)