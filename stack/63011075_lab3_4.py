class Stack:
	def __init__(self):
		self.stack = []
		# self.seen_tree = 0

	def push(self,i):
		# if len(self.stack) == 0:
		# 	self.stack.append(i)
		# 	self.seen_tree += 1
		# else:
		# 	if i < self.stack[-1]:
		# 		self.stack.append(i)
		# 		self.seen_tree += 1
		# 	else:
		# 		self.stack.append(i)
		# 		self.seen_tree = 1
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


		
s = Stack()
inp = input('Enter Input : ').split(',')
for i in inp:
	typ = i.split()[0]
	num = i.split()[-1]
	if typ == 'A':
		s.push(int(num))
	elif typ == 'B':
		s.turn_around()
		

	