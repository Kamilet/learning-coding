dict = {}
dict['one'] = '1 - Kamilet'
dict[2]		= '2 - grucy'

print(dict['one'])			#输出键值one下的值
print(dict[2])				#输出键为2的值
print(dict.keys())		#输出所有键
print(dict.values())	#输出所有值

tinydict = {'name':'runnoob','code':1,'site':'www.runnoob.com'}

print(tinydict)				#输出字典
print(tinydict.keys())		#输出所有键
print(tinydict.values())	#输出所有值
print(bool(tinydict['code']))

mydict = {'name':['a','b']}
mydict['age'] = ['39','88']
mydict['city'] = ['bj']
print(mydict)
mydict['age'] = ['40','41']
print(mydict)
#字典和列表嵌套

print('所有键值！：',end='')
for i in mydict:
	print('{}'.format(i),end=',')

print('键值对')
for k,v in mydict.items():
	print(k,':',v,end=' ')

# 判断子类对象是否继承于父类
class father(object):
    pass
class son(father):
    pass
if __name__ == '__main__':
    print (type(son())==father)
    print (isinstance(son(),father))
    print (type(son()))
    print (type(son))