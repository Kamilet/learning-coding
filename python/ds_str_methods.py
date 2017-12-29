#这是一个字符串对象
name = 'Kamilet'

if name.startswith('Kam'):
	print('Yes, the string starts with "Kam"')

if 'a' in name:
	print('Yes, contains "a"')

if name.find('mil') != -1:
	print('Yes, contains "mil"')

delimiter='_*_'
mylist = ['aaa', 'bbb', 'ccc', 'ddd']
print(delimiter.join(mylist))