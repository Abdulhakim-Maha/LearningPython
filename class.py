class Employee :
	def __init__(self, name, age, salary) :
		self.name = name
		self.age = age
		self.salary = salary

	def detail(self) -> str :
		print('Name:',self.name, self.age,'years old')

	def getAge(self) :
		print('10')

	def getSalary(self) :
		print('10')
	
	def credential(self) -> str:
		return 'Name:',self.name,'Age:',self.age,'Salary:',self.salary

class Programmer(Employee):
	def __init__(self, name, age, salary,skill):
		super().__init__(name, age, salary)
		self.skill = skill

	def showSkill(self):
		print(self.skill)
	
user1 = Programmer('austiniqer',19,14000.99,'C, Java, JavaScript, Python')
print(user1.credential())

