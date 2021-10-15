class LinkedList:
	class Node:
		def __init__(self, value) -> None:
			self.value = value
			self.next = None

	def __init__(self) -> None:
		self.head = None

	def __str__(self) -> str:
		if self.isEmpty():
			return 'Empty'
		cur = self.head		
		s = ''
		while cur.next != None:
			s += str(cur.value) + '->'
			cur = cur.next
		s += str(cur.value)
		return s

	def size(self) -> int:
		total = 0
		if self.isEmpty():
			return total
		cur = self.head
		while cur.next != None:
			cur = cur.next
			total += 1
		return total + 1


	def append(self, item):
		new_node = self.Node(item)
		if self.isEmpty():
			self.head = new_node
		else:
			cur = self.head
			while cur.next != None:
				cur = cur.next
			cur.next = new_node

	def pop(self):
		if self.isEmpty():
			return 'Empty'
		cur = self.head
		length = self.size()
		pop = self.find_with_index(length)
		for i in range(1,length - 1):
			cur = cur.next
		cur.next = None
		return pop

		
	def find_with_index(self, index):
		if self.isEmpty():
			return 'Empty'
		cur = self.head
		for i in range(index - 1):
			cur = cur.next
		return cur.value


	def isEmpty(self):
		return self.head == None

	def search(self, item):
		if self.isEmpty():
			return 'Not Found!'
		cur = self.head		
		while cur.next != None:
			if cur.value == item:
				return 'Found!'
			cur = cur.next
		if cur.value == item:
			return 'Found!'
		else:
			return 'Not Found!'

	def index(self, item):
		if self.isEmpty():
			return 'Empty'
		index = 0
		cur = self.head
		while cur.next != None:
			if item == cur.value:
				return index
			cur = cur.next
			index += 1
		if item == cur.value:
			return index
		else:
			return 'Not Found!'



if __name__ == '__main__':
	L = LinkedList()
	inp = input('Enter Input : ').split(',')
	for i in inp:
		typ = i.split()[0]
		item = i.split()[-1]
		if typ == 'A':
			L.append(int(item))
			print('Append :',item)		
			print('Linked List :',L)
		elif typ == 'P':
			pop = L.pop()
			print('Pop :',pop)
			print('Linked List :',L)
		elif typ == 'S':
			print('Linked List size :',L.size())
		elif typ == 'SE':
			print(f'{L.search(int(item))}')	
		elif typ == 'IN':
			print(f'Index : {L.index(int(item))}')