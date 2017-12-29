def print_max(a, b):
	if a > b :
		return a
	elif a == b :
		return 0
	else :
		return b

x = 5
y = 6 # I CAN USE a AND b AGAIN HERE.
z = print_max(a, b)
if z == 0 :
	print('they are the same !')
else:
	print(z,' is bigger !')