class Stack:
	def __init__(self) -> None:
		self.stack = []

	def push(self, elm) -> None:
		self.stack.append(elm)
		print('Add =',elm)

	def pop(self) :
		if len(self.stack) == 0:
			print('-1')
		else:
			print('Pop =',self.stack[-1])
			self.stack.pop()

	def isEmpty(self) -> bool:
		return True if len(self.stack) == 0 else False
		
	def size(self) -> str:
		return str(len(self.stack))

	def items(self) -> str:
		return str(self.stack)	

	def delete(self, elm):
		if len(self.stack) == 0:
			print('-1')
		else:
			for i in range(self.stack.count(elm)):
				self.stack.remove(elm)
				print('Delete =',elm) 


	def deleteLD(self, elm):
		if len(self.stack) == 0:
			print('-1')
		else:
			for i in self.stack:
				if i < elm:
					self.stack.remove(i)
					print('Delete =',i,'Because',i,'is less than',elm)

	def deleteMD(self, elm):
		if len(self.stack) == 0:
			print('-1')
		else:
			for i in self.stack:
				if i > elm:
					self.stack.remove(i)
					print('Delete =',i,'Because',i,'is more than',elm)


def ManageStack():
	array = input('Enter Input : ').split(',')
	s = Stack()

	for i in range(len(array)):
		typ = array[i].split(' ')[0]
		num = array[i].split(' ')[-1]
		if typ == 'A':
			s.push(int(num))
		elif typ == 'P':
			s.pop()
		elif typ == 'D':
			s.delete(int(num))
		elif typ == 'LD':
			s.deleteLD(int(num))
		elif typ == 'MD':
			s.deleteMD(int(num))
		
	print('Value in Stack =',s.items())	

ManageStack()

