class LinkedList:
	class Node:
		def __init__(self,data) -> None:
			self.data = data
			self.prev = None
			self.next = None
	def __init__(self) -> None:
		self.dummy = self.Node(None)
		self.cursor = self.Node('|')
		self.dummy.next = self.cursor
		self.cursor.prev = self.dummy
	def length(self):
		total = 0
		cur = self.dummy
		while cur.next != None:
			total += 1
			cur = cur.next
		return total
	def isEmpty(self):
		return self.dummy.next == None
	def insert(self,item):
		new_node = self.Node(item)
		cur = self.cursor
		prev = cur.prev

		new_node.next = cur
		new_node.prev = prev
		prev.next = new_node
		cur.prev = new_node
	def __str__(self) -> str:
		s = ''
		if self.isEmpty():
			return s
		cur = self.dummy.next
		while cur.next != None:
			s += str(cur.data) + ' '
			cur = cur.next
		s += str(cur.data) 
		return s
	def left(self):
		if self.cursor.prev == self.dummy:
			return
		cur = self.cursor
		front = cur.prev.prev
		middle = cur.prev
		last = cur.next

		front.next = cur
		middle.prev = cur
		middle.next = cur.next
		cur.prev = front
		cur.next = middle
		if last != None:
			last.prev = middle
		
		
	def right(self):
		if self.cursor.next == None:
			return
		cur = self.cursor
		first = cur.prev
		middle = cur.next
		last = cur.next.next

		first.next = middle
		middle.prev = first
		middle.next = cur
		if last != None:
			last.prev = cur
		cur.next = last
		cur.prev = middle

	def backspace(self):
		cur = self.cursor
		if cur.prev == self.dummy:
			return
		cur.prev.prev.next = cur
		cur.prev = cur.prev.prev
	def delete(self):
		cur = self.cursor
		if cur.next == None:
			return
		if cur.next.next != None:	
			cur.next.next.prev = cur
		cur.next = cur.next.next

if __name__ == '__main__':
	L = LinkedList()
	inp = input('Enter Input : ').split(',')
	for i in inp:
		if i[0] == 'I':
			L.insert(i[2:])
			# print(L)
		elif i[0] == 'L':
			L.left()
			# print(L)
		elif i[0] == 'R':
			L.right()
			# print(L)
		elif i[0] == 'D':
			L.delete()
			# print(L)
		elif i[0] == 'B':
			L.backspace()
			# print(L)
	print(L)

