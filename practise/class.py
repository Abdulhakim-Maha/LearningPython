class Employee :
	def __init__(self, name, age, salary) :
		self.name = name
		self.age = age
		self.salary = salary

	# def detail(self) -> str :
		# print('Name:',self.name, self.age,'years old')

	# def getAge(self) :
	# 	print('10')

	# def getSalary(self) :
	# 	print('10')
	
	def credential(self) :
		print( 'Name:',self.name,'Age:',self.age,'Salary:',self.salary)
		
	def __str__(self) -> str:
		return self.name + str(self.age) + str(self.salary)

class Programmer(Employee):
	def __init__(self, name, age, salary,skill):
		super().__init__(name, age, salary)
		self.skill = skill

	def showSkill(self):
		print(self.skill)

	def showAll(self):
		print(self.name,self.age,self.salary,self.skill)
	
	def __str__(self) -> str:
		return super().__str__() + self.skill
	
user1 = Programmer('austiniqer',19,14000.99,'C, Java, JavaScript, Python')
# print(user1.credential())
print(user1.__str__())
# user1.showAll()

