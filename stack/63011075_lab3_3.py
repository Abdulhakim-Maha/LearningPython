class Stack:
	def __init__(self, ls = None):
		self.stack = []
	def push(self,i):
		self.stack.append(i)	
	def pop(self):
		return self.stack.pop()
	def isEmpty(self):
		return True if len(self.stack) == 0 else False
	def size(self):
		return len(self.stack)

def postFixeval(st):
	s = Stack()
	for i in st:
		if  i ==  '*' or i == '/' or i == '+' or i == '-':
			if i == '+':
				value1 = s.pop()
				value2 = s.pop()
				result = value2 + value1
				s.push(result)
			elif i == '-':
				value1 = s.pop()
				value2 = s.pop()
				result = value2 - value1
				s.push(result)
			elif i == '*':
				value1 = s.pop()
				value2 = s.pop()
				result = value2 * value1
				s.push(result)
			elif i == '/':
				value1 = s.pop()
				value2 = s.pop()
				result = value2 / value1
				s.push(result)
		else:
			s.push(int(i))
	return s.pop()

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())
# print(token)



print("Answer : ",'{:.2f}'.format(postFixeval(token)))