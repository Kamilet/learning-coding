#coding=UTF-8

class SchoolMember:
	'''代表任何学校的成员'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('added SchoolMember: {}'.format(self.name))

	def tell(self):
		'''告诉我细节'''
		print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
	'''代表一个老师'''
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print('added Teacher: {}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
	'''代表一个学生'''
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('added Student: {}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mr. Kamilet', 40, 30000)
s = Student('Grucy', 25, 75)

#打印空白行
print()

members = [t, s]
for member in members:
	#对全体师生工作
	member.tell()