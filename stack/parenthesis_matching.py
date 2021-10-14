class Stack:
	def __init__(self):
		self.stack = []
	def __str__(self) -> str:
		return 'Stack : ' + str(self.stack)
	def push(self, item):
		self.stack.append(item)
	def pop(self):
		if self.isEmpty():
			return None
		return self.stack.pop()
	def isEmpty(self):
		return len(self.stack) == 0 
	def size(self):
		return len(self.stack)

def parent_check(ls):
	match = True
	s = Stack()
	for i in ls:
		# print(i)
		if i in ['(','{','[']:
			s.push(i)
			print(s)
		elif i in [')','}',']']:
			last = s.pop()  
			if i == ')':
				if last != '(':
					match = False
			elif i == '}':
				if last != '{':
					match = False
			elif i == ']':
				if last != '[':
					match = False
			print(s)
	return match


if __name__ == '__main__':
	s = Stack()
	filter_ls = []
	ls = input('Enter input : ')
	for i in ls:
		if i in ['(',')','{','}','[',']']:
			filter_ls.append(i)
	# print(filter_ls)
	match = parent_check(filter_ls)
	if match :
		print('parenthesis is matched!')
	else:
		print('parenthesis unmatch!')



