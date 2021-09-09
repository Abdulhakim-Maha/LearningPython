class Stack:
	def __init__(self):
		self.stack = []
	def push(self,i):
		self.stack.append(i)
	def pop(self):
		return self.stack.pop()
	def isEmpty(self):
		return True if len(self.stack) == 0 else False
	def turn_around(self):
		lis = []
		for i in self.stack:
			if len(lis) == 0:
				lis.append(i)
			else:
				for j in range(len(lis)):
					if i < lis[-1]:
						lis.append(i)
						break
					elif i > lis[-1]:
						lis.pop()

					if len(lis) == 0:
						lis.append(i)
		print(len(lis))

	def spacial(self):
		lis = []
		for i in self.stack:
			if i % 2 == 0:
				i -= 1
				lis.append(i)
			elif i % 2 == 1:
				i += 2
				lis.append(i)
		self.stack = lis



s = Stack()
inp = input('Enter Input : ').split(',')
for i in inp:
	typ = i.split()[0]
	num = i.split()[-1]
	if typ == 'A':
		s.push(int(num))
	elif typ == 'B':
		s.turn_around()
	elif typ == 'S':
		s.spacial()
		

	