class Queue:
	def __init__(self) -> None:
		self.q = []
	def enqueue(self,data):
		self.q.append(data)
	def dequeue(self):
		return self.q.pop(0)
	def isEmpty(self):
		return len(self.q) == 0
class Node:
	def __init__(self, data) -> None:
		self.data = data
		self.right = None
		self.left = None
	def __str__(self) -> str:
		return str(self.data)
class BST:
	def __init__(self,data = None) -> None:
		if data:
			self.root = Node(data)
		else:
			self.root = None
	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			cur = self.root
			while True:
				if data >= cur.data:
					if cur.right is None:
						cur.right = Node(data)
						break
					else:
						cur = cur.right
				elif data < cur.data:
					if cur.left is None:
						cur.left = Node(data)
						break
					else:
						cur = cur.left
				else:
					break
	def traversal(self, type):
		if type == 'pre order':
			return self.__pre_order(self.root,'')
		elif type == 'in order':
			return self.__in_order(self.root,'')
		elif type == 'post order':
			return self.__post_order(self.root,'')
		elif type == 'level order':
			return self.__level_order()
		elif type == 'reverse level order':
			return self.__reverse_level_order()
		else:
			return f'not allow traversal {type}'

	def __pre_order(self,node,s):
		if node:
			s += str(node) + ' '
			s = self.__pre_order(node.left,s)
			s = self.__pre_order(node.right,s)
		return s

	def __in_order(self,node,s):
		if node:
			s = self.__in_order(node.left,s)
			s += str(node) + ' '
			s = self.__in_order(node.right,s)
		return s

	def __post_order(self,node,s):
		if node:
			s = self.__post_order(node.left,s)
			s = self.__post_order(node.right,s)
			s += str(node) + ' '
		return s
	def __level_order(self):
		if self.root is None:
			return ''	
		q = Queue()
		q.enqueue(self.root)
		s = ''
		while not q.isEmpty():
			p = q.dequeue()
			s += str(p) + ' '
			if p.left:
				q.enqueue(p.left)
			if p.right:
				q.enqueue(p.right)
		return s

T = BST()
print(' *** Binary Search Tree ***')
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
     T.insert(i)
print('\n --- Tree traversal ---')
print('Level order :',T.traversal('level order'))
print('Preorder :',T.traversal('pre order'))
print('Inorder :',T.traversal('in order'))
print('Postorder :',T.traversal('post order'))