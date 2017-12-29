student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)	#自动去除重复元素Tom

#成员测试
if 'Rose' in student:
	print('Rose在')
else:
	print('Rose不在')

#set集合运算
a = set('abbbateajio')
b = set('jiawaozq')
print('集合a为: {}'.format(a))
print('集合b为:',b)

print('a和b的差集:',a-b)
print('a和b的并集:',a|b)	#不允许集合相加
print('a和b的交集:',a&b)
print('a和b中不同时存在的元素',a^b)