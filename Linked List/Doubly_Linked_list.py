class DoudlyLinkedList:
	class Node:
		def __init__(self, value) -> None:
			self.value = value
			self.next = None
			self.prev = None

	def __init__(self) -> None:
		self.dummy = self.Node(None)
	def append(self, value):
		new_node = self.Node(value)
		cur = self.dummy
		if self.isEmpty():
			cur.next = new_node
			new_node.prev = cur
		else:
			while cur.next != None:
				cur = cur.next
			cur.next = new_node
			new_node.prev = cur

	def __str__(self) -> str:
		if self.isEmpty() : return 'Empty'
		else:
			s = ''
			cur = self.dummy.next
			while cur.next != None:
				s += str(cur.value) + '->'
				cur = cur.next
			s += str(cur.value) 
			return s

	def isEmpty(self):
		return  self.dummy.next == None
	def __len__(self):
		if self.isEmpty(): return 0
		cur = self.dummy.next
		l = 1
		while cur.next != None:
			l += 1
			cur = cur.next
		return l
	def remove(self,data):
		if self.isEmpty():  return 'Empty'
		else:
			cur = self.dummy.next
			while cur.next != None:
				if cur.value == data:
					p = cur.next
					q = cur.prev
					q.next = p
					p.prev = q
				cur = cur.next
			if cur.value == data:
				q = cur.prev
				q.next = None
	def insert(self, data, index):
		if self.isEmpty(): return 'Empty'
		if index > len(self):
			self.append(data)
		else:
			p = self.find_with_index(index)
			q = p.prev
			new_node = self.Node(data)
			q.next = new_node
			new_node.next = p
			p.prev = new_node
			new_node.prev = q

	def find_with_index(self,index):
		if self.isEmpty(): return 'Empty'
		if index > len(self): return 'Index out of bound'
		else:
			cur = self.dummy.next
			for i in range(index):
				cur = cur.next
			return cur

if __name__ == '__main__':
	L = DoudlyLinkedList()
	inp = input('Enter Input : ').split(',')
	for i in inp:
		typ = i.split()[0]
		item = i.split()[-1]
		if typ == 'A':
			L.append(int(item))
			print('\tAppend :',item)		
			print('Linked List :',L)
		elif typ == 'R':
			L.remove(int(item))
			print('\tRemove :',item)		
			print('Linked List :',L)
		elif typ == 'F':
			print('\tData index of :',item,'is :',(L.find_with_index(int(item))).value)		
		elif typ == 'I':
			data = item.split(':')[0]
			index = item.split(':')[-1]
			L.insert(int(data), int(index))
			print('\tInsert :',item,'at index :',index)		
			print('Linked List :',L)
			
		# # elif typ == 'INS':
		# 	result = L.insert(item.split(':')[0],int(item.split(':')[1]))
		# 	print('\tInsert :',item.split(':')[0],'Index :',item.split(':')[1])
		# 	if result != 0:
		# 		print(result)
		# 	print('Linked List :',L)