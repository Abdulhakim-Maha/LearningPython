class Node:
	def __init__(self,value) -> None:
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self) -> None:
		self.head = None

	def __str__(self) -> str:
		if self.isEmpty():
			return 'Empty'
		cur, s = self.head, str(self.head.value) + ' '
		while cur.next != None:
			s += str(cur.next.value) + ' '
			cur = cur.next
		return s	

	def isEmpty(self):
		return self.head == None

	def append(self,item):
		new_node = Node(item)
		if self.isEmpty():
			self.head = new_node 
		else:
			cur = self.head
			while cur.next != None:
				cur = cur.next 
			cur.next = new_node

	def addHead(self,item):
		if self.isEmpty():
			self.head = Node(item)
		else:
			new_node = Node(item)
			new_node.next = self.head
			self.head = new_node

	def search(self,item):
		if self.isEmpty():
			return 'Not Found'
		cur = self.head
		while cur.next != None:
			if item == cur.value:
				return 'Found'
			cur = cur.next
		return 'Found' if cur.value == item else 'Not Found'

	def size(self):
		if self.isEmpty():
			return 0
		cur = self.head
		total = 1
		while cur.next != None:
			total += 1
			cur = cur.next
		return total

	def index(self,item):
		if self.isEmpty():
			return -1
		p = self.head
		for i in range(self.size()):
			if p.value == item:
				return i
			p = p.next
		return -1

	def pop(self,pos):
		if self.isEmpty():
			return 'Out of Range'
		cur = self.head
		if pos == 0:
			self.head = self.head.next
			return 'Success'
		for i in range(self.size())	:
			if i == (pos - 1):
				cur.next = cur.next.next
				return 'Success'
			cur = cur.next
		return 'Out of Range'


			

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
	if i[:2] == "AP":
		L.append(i[3:])
	elif i[:2] == "AH":
		L.addHead(i[3:])
	elif i[:2] == "SE":
		print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
	elif i[:2] == "SI":
		print("Linked List size = {0} : {1}".format(L.size(), L))
	elif i[:2] == "ID":
		print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
	elif i[:2] == "PO":
		before = "{}".format(L)
		k = L.pop(int(i[3:]))
		print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
