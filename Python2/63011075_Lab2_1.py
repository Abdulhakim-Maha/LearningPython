class Calculator :
	def __init__(self,num) -> None:
		self.num = num 
	def __add__(self, y) :
		return self.num + y.num
	def __sub__(self, y) :
		return self.num - y.num
	def __mul__(self, y) :
		return self.num * y.num
	def __truediv__(self, y):
		return self.num / y.num



x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))
print(x+y,x-y,x*y,x/y,sep = "\n")