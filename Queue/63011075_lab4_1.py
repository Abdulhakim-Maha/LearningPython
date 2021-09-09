from collections import deque
class Queue:
	def __init__(self):
		self.q = deque()
		self.d = deque()

	def enqueue(self,i):
		self.q.append(i)
		print(self.items())

	def dequeue(self):
		if len(self.q) == 0:
			print('Empty')
			return 
		else:
			d = self.q.popleft()
			self.d.append(d)
			print(d,'<-',self.items())

	def items(self):
		s = ''
		if len(self.q) == 0:
			s = 'Empty'
		for i in range(len(self.q)):
			if i != len(self.q)-1:
				s += str(self.q[i]) +', '
			else:
				s += str(self.q[i])
		return s
		
	def items_d(self):
		s = ''
		if len(self.d) == 0:
			s = 'Empty'
		for i in range(len(self.d)):
			if i != len(self.d)-1:
				s += str(self.d[i]) +', '
			else:
				s += str(self.d[i])
		return s

inp = input('Enter Input : ').split(',')
q = Queue()
for i in inp:
	if i[0] == 'E':
		q.enqueue(i[2:])
	elif i[0] == 'D':
		q.dequeue()
print(q.items_d(),':',q.items())

