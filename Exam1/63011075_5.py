class Rational:
	def __init__(self, num = 1,deno = 1) -> None:
		self.num = num
		self.deno = deno
	def __str__(self) -> str:
		if self.num == 1 and self.deno == 1:
			return str(1) 
		return str(self.num) + '/' + str(self.deno)
	def __lt__(self,other):
		return 'TRUE' if self.num/self.deno < other.num/other.deno else 'FALSE'
	def __gt__(self,other):
		return 'TRUE' if self.num/self.deno > other.num/other.deno else 'FALSE'
	def __le__(self,other):
		return 'TRUE' if self.num/self.deno <= other.num/other.deno else 'FALSE'
	def __ge__(self,other):
		return 'TRUE' if self.num/self.deno >= other.num/other.deno else 'FALSE'
	def __eq__(self,other):
		return 'TRUE' if self.num/self.deno == other.num/other.deno else 'FALSE'
	def __ne__(self,other):
		return 'TRUE' if self.num/self.deno != other.num/other.deno else 'FALSE'
	def __add__(self,other):
		newdeno = self.deno * other.deno
		A_num = self.num * other.deno
		B_num = other.num * self.deno
		result = A_num + B_num
		# print(result)
		# print(newdeno)
		return self.smallestForm(result,newdeno) 
	def __sub__(self,other):
		newdeno = self.deno * other.deno
		A_num = self.num * other.deno
		B_num = other.num * self.deno
		result = A_num - B_num
		# print(result)
		# print(newdeno)
		return self.smallestForm(result,newdeno) 
	def __mul__(self, other):
		newnum = self.num * other.num
		newdeno = self.deno * other.deno
		return self.smallestForm(newnum,newdeno) 
	def __truediv__(self,other):
		newnum = self.num * other.deno
		newdeno = self.deno * other.num
		return self.smallestForm(newnum,newdeno)
	def __floordiv__(self,other):
		newnum = self.num * other.deno
		newdeno = self.deno * other.num
		# print(newnum,newdeno)
		if newnum == 0 or newdeno == 0:
			return 0
		else:
			result = newnum // newdeno
			return str(result)
		# print(result)
	def smallestForm(self,num,deno):
		for i in range(1,100):
			if num % i == 0 and deno % i == 0:
				num = num // i
				deno = deno // i
		return str(num) + '/' + str(deno)

print(" *** Rational Calculator ***")
print(" *        A = n1/d1        *")
print(" *        B = n2/d2        *")
print(" ***************************\n")
str_input = input("Enter n1 d1 n2 d2 : ")
n1, d1, n2, d2 = [int(e) for e in str_input.split()]
A = Rational(n1,d1)     # A = n1/d1
B = Rational(n2,d2)     # B = n2/d2
C = Rational()          # C = 1/1      
print("A = ",A,"\tB= ",B,'\tC = ',C)        # method __str__
print("A < B ==> ",A<B)     # method __lt__
print("A > B ==> ",A>B)     # method __gt__
print("A <= B ==> ",A<=B)   # method __ge__
print("A >= B ==> ",A>=B)   # method __ge__
print("A == B ==> ",A==B)   # method __eq__
print("A != B ==> ",A!=B)   # method __ne__
print("A + B ==> ",A+B)     # method __add__
print("A - B ==> ",A-B)     # method __sub__
print("A * B ==> ",A*B)     # method __mul__
print("A / B ==> ",A/B)     # method __truediv__
print("A // B ==> ",A//B)     # method __floordiv__
print("A + C ==> ",A+C)        