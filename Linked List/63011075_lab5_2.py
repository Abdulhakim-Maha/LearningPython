class Node:
	def __init__(self, data) -> None:
		self.data = data
		self.next = None
		self.prev = None
class LinkedList:
	def __init__(self) -> None:
		self.dummy = Node(None)
	def lenght(self):
		total = 0
		cur = self.dummy
		while cur.next != None:
			cur = cur.next
			total += 1
		return total
	def __str__(self) -> str:
		s = ''
		if self.lenght() == 0:
			return s
		cur = self.dummy.next 
		while cur.next != None:
			s += str(cur.data) + '->'
			cur = cur.next
		s += str(cur.data)
		return s
	def str_reverse(self):
		s = ''
		if self.lenght() == 0:
			return s
		cur = self.dummy.next
		while cur.next != None:
			cur = cur.next
		while cur.prev != None:
			s += str(cur.data) + '->'
			cur = cur.prev
		return s[:-2]
	def isEmpty(self):
		return self.dummy.next == None
	def append(self,item):
		new_node = Node(item)
		cur = self.dummy
		while cur.next != None:
			cur = cur.next
		cur.next = new_node
		new_node.prev = cur
		new_node.next = None
	def add_before(self,data):
		if self.lenght() == 0:
			self.append(data)
		else:
			new_node = Node(data)
			cur = self.dummy
			p = cur.next
			p.prev = new_node
			new_node.next = cur.next
			new_node.prev = cur
			cur.next = new_node
	def insert(self,index,data):
		if index < 0 or index > self.lenght():
			print('Data cannot be added')
			return False
		if self.lenght() == 0 and index == 0:
			self.append(data)
			return True
		if self.lenght() == index :
			self.append(data)		
			return True
		cur = self.dummy.next
		new_node = Node(data)
		for i in range(index+1):
			if i == index:
				p = cur.prev	
				p.next = new_node
				new_node.prev = p
				new_node.next = cur
				cur.prev = new_node
			cur = cur.next
		return True

	def remove(self,data):
		cur = self.dummy
		index = -1
		while cur.next != None:
			if cur.data == data:
				p = cur.prev
				p.next = cur.next
				q = cur.next
				q.prev = cur.prev
				return cur.data,index
			cur = cur.next
			index += 1
		if cur.data == data:
			p = cur.prev
			p.next = None
			return cur.data,index
		return 'Not Found!',None

l = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
	i = i.strip()
	if i[:2] == 'Ab':
		l.add_before(int(i[2:]))
		print('linked list :',l)
		print('reverse :',l.str_reverse())
	elif i[0] == 'A':
		l.append(int(i[2:]))
		print('linked list :',l)
		print('reverse :',l.str_reverse())
	elif i[0] == 'R':
		data,index = l.remove(int(i[2:]))	
		if data == 'Not Found!':
			print(data)
		else:
			print('removed : {} from index : {}'.format(data,index))
		print('linked list :',l)
		print('reverse :',l.str_reverse())
	elif i[0] == 'I':
		index, data = i[2:].split(':')
		x = l.insert(int(index),int(data))
		if x :
			print('index = {} and data = {}'.format(index,data))
		print('linked list :',l)
		print('reverse :',l.str_reverse())