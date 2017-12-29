# "ab"是地址(Address)簿(Book)的缩写

ab = {
	'hi': 'hi@kamilet.cn',
	'admin': 'admin@kamilet.cn',
	'grucy': 'grucy@kamilet.cn',
	'kamilet': 'kamilet@kamilet.cn'
}

print("Kamilet's address is", ab['kamilet'])

#删除对
del ab['hi']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
	print('Contact {} at {}'.format(name, address))

#添加对
ab['mkt'] = 'mkt@kamilet.cn'

if 'mkt' in ab:
	print("\nmkt's address is", ab['mkt'])