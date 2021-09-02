from collections import deque
class Queue:
	def __init__(self, ls = None):
		self.first = False
		if ls != None:
			self.q = deque(ls,len(ls))
		else:
			self.q = deque()
	def enqueue(self,i):
		self.q.append(i)
	def s_enqueue(self,i):
		if self.first == False:
			self.q.insert(0,i)
			self.first = True
		else:
			self.q.insert(1,i)
	def dequeue(self):
		return self.q.popleft() if len(self.q) != 0 else 'Empty'
	def isEmpty(self):
		return len(self.q) == 0
	def size(self):
		return len(self.q)

inp = input('Enter Input : ').split(',')
q = Queue()
for i in inp:
	typ = i.split()[0]
	num = i.split()[-1]
	if typ == 'EN':
		q.enqueue(num) 
	elif typ == 'ES':
		q.s_enqueue(num)	
	elif typ == 'D':
		print(str(q.dequeue()))