def maximum(x, y):
	if x>y:
		return x
	elif x<y:
		return y
	else:
		return "The same !"

def something():
	pass	#不做任何执行，不Return

print(maximum(2, 5))
something()
print(max(2,5))	#这是内置函数