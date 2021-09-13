class LinkedList:
	class Node:
		def __init__(self,data) -> None:
			self.data = data
			self.prev = None
			self.next = None
	def __init__(self) -> None:
		self.dummy = self.Node(None)
	def isEmpty(self):
		return self.dummy.next == None
	def length(self):
		total = 0
		cur = self.dummy
		while cur.next != None:
			total += 1 
			cur = cur.next
		return total
	def append(self,data):
		new_node = self.Node(data)
		cur = self.dummy
		while cur.next != None:
			cur = cur.next
		cur.next = new_node
		new_node.prev = cur
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
	def str_reverse(self) -> str:
		s = ''
		if self.isEmpty():
			return s
		cur = self.dummy.next
		while cur.next != None:
			cur = cur.next
		while cur.prev != None:
			s += str(cur.data) + ' '
			cur = cur.prev
		return s[:-1]


l1,l2 = input('Enter Input (L1,L2) : ').split()
l1 = l1.split('->')
l2 = l2.split('->')

L1 = LinkedList()
L2 = LinkedList()

for i in l1:
	L1.append(i)
for i in l2:
	L2.append(i)
			
print('L1    :',L1)
print('L2    :',L2)
# print('L2 reverse :',L2.str_reverse())			

Merge = LinkedList()
for i in l1:
	Merge.append(i)
for i in L2.str_reverse().split():
	Merge.append(i)
print('Merge :',Merge)

		
	