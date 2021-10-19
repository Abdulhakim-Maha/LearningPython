class LinkedList:
	class Node:
		def __init__(self, data) -> None:
			self.data = data
			self.next = None
	def __init__(self) -> None:
		self.dummy = self.Node(None)
	def __str__(self) -> str:
		s = ''
		cur = self.dummy.next
		while cur.next != None:
			s += str(cur.data) + '->'
			cur = cur.next 
		s += str(cur.data)
		return s
	def append(self, data):
		new_node = self.Node(data)
		if self.isEmpty():
			self.dummy.next = new_node
		else:
			cur = self.dummy.next
			while cur.next != None:
				cur = cur.next
			cur.next = new_node
	def isEmpty(self):
		return self.dummy.next == None
	def __len__(self):
		if self.isEmpty():
			return 0
		else:
			cur = self.dummy.next	
			l = 1
			while cur.next != None:
				cur = cur.next
				l += 1
			return l
	def insert(self, data, index):
		new_node = self.Node(data)
		if self.isEmpty():
			self.dummy.next = new_node
		if index > len(self):
			return 'Index Out Of Bounds'
		elif index == 0:
			p = self.dummy.next
			self.dummy.next = new_node
			new_node.next = p
			return 0
		else:
			p = self.find_with_index(index - 1)
			new_node.next = p.next
			p.next = new_node
			return 0

	def remove(self, data):
		pass
	def find_with_index(self,index):
		if self.isEmpty():
			return 'Empty'
		else:
			cur = self.dummy.next
			for i in range(index):
				cur = cur.next
			return cur

if __name__ == '__main__':
	L = LinkedList()
	inp = input('Enter Input : ').split(',')
	for i in inp:
		typ = i.split()[0]
		item = i.split()[-1]
		if typ == 'A':
			L.append(int(item))
			print('\tAppend :',item)		
			print('Linked List :',L)
		elif typ == 'INS':
			result = L.insert(item.split(':')[0],int(item.split(':')[1]))
			print('\tInsert :',item.split(':')[0],'Index :',item.split(':')[1])
			if result != 0:
				print(result)
			print('Linked List :',L)
			