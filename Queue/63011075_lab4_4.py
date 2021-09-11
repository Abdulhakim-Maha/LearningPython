from collections import deque
class Queue:
	def __init__(self) -> None:
		self.q = deque()
		self.dpm = deque()
	def enqueue(self,i):
		dpm = i // 100
		# if i in self.q:
		# 	return
		if len(self.q) == 0:
			self.q.append(i)	
			self.dpm.append(dpm)
		else:
			if dpm not in self.dpm:
				self.q.append(i)
				self.dpm.append(dpm)
			else:
				# insert last index
				find = deque(self.dpm)
				find.reverse()
				index = find.index(dpm)
				last_index = (len(find)-index-1)
				# print('last index :',last_index)
				self.q.insert(last_index + 1,i)
				self.dpm.insert(last_index + 1,dpm)

			
	def dequeue(self) -> str:
		if len(self.q) == 0:
			return 'Empty'
		else:
			self.dpm.popleft()
			return self.q.popleft()

if __name__ == '__main__':
	inp =input('Enter Input : ').split('/')[-1].split(',')
	q = Queue()
	for i in inp:
		if i[0] == 'E':
			q.enqueue(int(i[2:]))
		elif i[0] == 'D':
			print(f'{q.dequeue()}')

