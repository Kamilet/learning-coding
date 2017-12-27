# coding=UTF-8

class Robot:
	'''表示有一个带名字的机器人'''
	#一个类变量，用来计数机器人数量
	population = 0

	def __init__(self, name):
		'''初始化数据'''
		self.name = name
		print('Initializing {}'.format(self.name))

		#当有人被创建时，机器人的人口会增加
		Robot.population += 1

	def die(self):
		'''我挂了'''
		print('{} is being destoryed !'.format(self.name))

		Robot.population -=1

		if Robot.population == 0:
			print('{} was the last one.'.format(self.name))
		else:
			print('There are still {:d} robots working'.format(Robot.population))

	def say_hi(self):
		'''来自机器人的问候'''

		print('Greetings, my masters call me {}.'.format(self.name))

	@classmethod
	#一个装时期，相当于
	#how_many = classmethod(how_many)
	def how_many(cls):
		'''当前人口'''
		print('We have {} robots.'.format(cls.population))

droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3P0')
droid2.say_hi()
Robot.how_many()

print('\nRobots can do some work here.\n')

print("Robots have finished their work. So let's destory them !")
droid1.die()
droid2.die()

Robot.how_many()
