class Employee :
	def __init__(self, name, age) :
		self.name = name
		self.age = age
	def detail(self) -> str :
		print('Name:',self.name, self.age,'years old')
	def getAge(self) :
		print('10')

user1 = Employee('austiniqer',19)
user1.detail()
user1.getAge()
