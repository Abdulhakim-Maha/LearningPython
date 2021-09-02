class Queue:
	def __init__(self) -> None:
		self.q = []
		self.d = []
	def enqueue(self,i):
		self.q.append(i)
		print(self.items())
	def items(self):
		if len(self.q) == 0:
			return 'Empty'
		else:
			return str(self.q)[1:-1]
	def dequeue(self):
		if len(self.q) == 0:
			print('Empty')
		else:
			d = self.q.pop(0)
			print(f'{d} <- {self.items()}')
			self.d.append(d)
	def dItems(self):
		return str(self.d)[1:-1] 

inp = input('Enter Input : ').split(',')
q = Queue()
for i in inp:
	typ = i.split()[0]
	val = i.split()[-1]
	if typ == 'E':
		q.enqueue(int(val))
	elif typ == 'D':
		q.dequeue()
print(q.dItems(),':',q.items())