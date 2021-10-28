class Queue:
	def __init__(self) -> None:
		self.q = []
	def enqueue(self, item):
		self.q.append(item)
	def dequeue(self):
		return self.q.pop(0)
	def __str__(self) -> str:
		return str(self.q)
	def isEmpty(self):
		return len(self.q) == 0

# if __name__ == '__main__':
# 	inp = input('Enter Queue : ').split(',')
# 	q = Queue()
# 	for i in inp:
# 		typ = i.split()[0]
# 		data = i.split()[-1]
# 		if typ == 'E':
# 			q.enqueue(int(data))
# 			print('Queue   :', q)
# 		elif typ == 'D':
# 			deq = q.dequeue()
# 			print('Dequeue :',deq)
# 			print('Queue   :', q)
		