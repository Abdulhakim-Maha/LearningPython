from collections import deque
class Queue:
	def __init__(self, ls = None) -> None:
		if ls != None:
			self.q = deque(ls,len(ls)) 
		else:
			self.q = deque()
	def enqueue(self,i):
		# self.q.append(i)
		if self.isEmpty() :
			self.q.append(i)
		else:
			for j in range(len(self.q)) :
				if self.q[j] // 100 == i // 100:
					self.q.insert(j + 1, i)
					break;
				else:
					self.q.append(i)
					break;
				
	def dequeue(self):
		return self.q.popleft() if not self.isEmpty() else 'Empty'
	def items(self):
		return self.q
	def size(self):
		return len(self.q)
	def isEmpty(self):
		return len(self.q) == 0

elm,queue = input('Enter Input : ').split('/')
queue = queue.split(',')
q = Queue()
for i in queue:
	typ = i.split()[0]
	num = i.split()[-1]
	if typ == 'E':
		q.enqueue(int(num))
	elif typ == 'D':
		print(q.dequeue())
# print(queue)