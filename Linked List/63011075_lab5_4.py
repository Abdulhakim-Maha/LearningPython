from typing import Deque


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

if __name__ == '__main__':
	L = LinkedList()
	inp = input('Enter Input : ').split(',')
	for i in inp:
		if i[0] == 'I':
			L.insert(i[2:])
			print(L)
	# print(L)

