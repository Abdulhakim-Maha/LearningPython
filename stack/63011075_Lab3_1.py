class Stack:
	def __init__(self) -> None:
		self.stack = []

	def push(self, elm) -> None:
		self.stack.append(elm)

	def pop(self) :
		return self.stack.pop()

	def isEmpty(self) -> bool:
		return True if len(self.stack) == 0 else False
		
	def size(self) -> str:
		return str(len(self.stack))

	def items(self) -> str:
		return str(self.stack)	

print(' *** Stack implement by Python list***')
ls = [e for e in input('Enter data to stack : ').split()]
s = Stack()
for e in ls:
	s.push(e)
print(s.size(),'Data in stack : ',s.items())
while not s.isEmpty():
	s.pop()
print(s.size(),'Data in stack : ',s.items())
