'''__init__方法会在类的对象被实例化时允许，可以对目标进行初始化操作'''

class Person:
	def __init__(self, name):
		self.namE = name #大写了一个E以示区别

	def say_hi(self):
		print('Hello, my name is', self.namE)

p = Person('Swaroop')
p.say_hi()