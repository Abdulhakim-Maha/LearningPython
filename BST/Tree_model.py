class Queue:
	def __init__(self) -> None:
		self.q = []
	def enqueue(self,data):
		self.q.append(data)
	def dequeue(self):
		return self.q.pop(0)
	def isEmpty(self):
		return len(self.q) == 0
class Stack:
	def __init__(self) -> None:
		self.s = []
	def push(self, data):
		self.s.append(data)
	def pop(self):
		return self.s.pop()
	def isEmpty(self):
		return len(self.s) == 0
	def peek(self):
		return self.s[-1]
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
				if data > cur.data:
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
	def __reverse_level_order(self):
		if self.root is None:
			return ''
		q = Queue()
		s = Stack()
		q.enqueue(self.root)
		traversal =''
		while not q.isEmpty():
			node = q.dequeue()
			s.push(node)
			if node.right:
				q.enqueue(node.right)
			if node.left:
				q.enqueue(node.left)
		while not s.isEmpty():
			traversal += str(s.pop()) + ' '
		return traversal
	def height(self,node):
		if node is None:
			return -1
		left_height = self.height(node.left)
		right_height = self.height(node.right)
		return 1 + max(left_height, right_height)
	def printTree(self, node, level = 0):
		if node != None:
			self.printTree(node.right, level + 1)
			print('     ' * level, node)
			self.printTree(node.left, level + 1)
	def size(self, node):
		if node is None:
			return 0
		return 1 + self.size(node.left) + self.size(node.right)	
	def size_with_queue(self):
		if self.root is None:
			return 0
		size = 1
		q = Queue()
		q.enqueue(self.root)
		while not q.isEmpty():
			p = q.dequeue()
			if p.left:
				q.enqueue(p.left)
				size += 1
			if p.right:
				q.enqueue(p.right)
				size += 1
		return size
	def father(self,data):
		cur = self.root
		if  cur.data == data:
			return f'None Because {data} is root node'
		while cur.left or cur.right:
			if cur.right and cur.right.data == data:
				return cur.data
			elif cur.left and cur.left.data == data:
				return cur.data
			if data > cur.data:
				cur = cur.right
			elif data < cur.data:
				cur = cur.left
		return 'Not Found'
	def son(self,data):
		pass
	def find(self,node,data):
		if data > node.data and node.right:
			return self.find(node.right, data)
		elif data < node.data and node.left:
			return self.find(node.left, data)
		if data == node.data:
			return True

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
     T.insert(i)
T.printTree(T.root)
print('Pre order :',T.traversal('pre order'))
print('In order :',T.traversal('in order'))
print('Post order :',T.traversal('post order'))
print('Level order :',T.traversal('level order'))
print('Reverse level order :',T.traversal('reverse level order'))
print('Height :',T.height(T.root))		
print('Size :',T.size(T.root))
print('Find 5 :',T.find(T.root,5))
print('Father of {} is {}'.format(5,T.father(5)))
# print('Size :',T.size_with_queue())
