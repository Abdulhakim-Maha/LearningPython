from collections import deque
class Queue:
	def __init__(self) :
		self.q = deque()
		self.p = deque()
	def enqueue(self,i):
		if i in self.q:
			return 
		else:
			self.q.append(i)
			self.p.append(0)
			# print('Queue :',self.items())


	def enqueue_s(self,i):
		if i in self.q:
			return 
		if len(self.q) == 0:
			self.q.append(i)
			self.p.append(1)
		else:
			if self.p[0] == 0:
				self.q.insert(0,i)
				self.p.insert(0,1)
			else:
				self.q.insert(1,i)
				self.p.insert(1,1)
		# print('Queue :',self.items())

	def dequeue(self):
		if len(self.q) == 0:
			print('Empty')
			return
		else:
			self.p.popleft()
			print(self.q.popleft())
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

inp = input('Enter Input : ').split(',')
q = Queue()
for i in inp:
	if i[:2] == 'EN':
		q.enqueue(int(i[3:]))
	elif i[:2] == 'ES':
		q.enqueue_s(int(i[3:]))
	elif i[0] == 'D':
		q.dequeue()