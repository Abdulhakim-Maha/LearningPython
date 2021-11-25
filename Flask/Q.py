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
	
	