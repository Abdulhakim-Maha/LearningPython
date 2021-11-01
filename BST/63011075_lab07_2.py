class Node:
	def __init__(self, data) -> None:
		self.data = data
		self.right = None
		self.left = None

class BST:
	def __init__(self) -> None:
		self.root = None

	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self.__insert(self.root, data)
		return self.root
	
	def __insert(self, cur_node, data):
		if data > cur_node.data: 
			if cur_node.right is None: cur_node.right = Node(data) 
			else: self.__insert(cur_node.right, data)
		else:
			if cur_node.left is None: cur_node.left = Node(data) 
			else: self.__insert(cur_node.left, data)


	def search_min(self, x):
		s = ''
		if self.root is None:
			s = ' Not have'
		else:
			# s = self.__search_min(self.root,x)
			x = self.in_order(self.root,x, '')
			# print(s)
			# print(x)
			# print(len(s))
			# print(len(x))
			if len(x) == 0:
				s = ' Not have'
				# print(True)
			# print(s.count(' '))
			# if len(s) == s.count(' '):
			# 	s = ' Not have'
			# pr
			# if ord(s[0]) == 32:
				# s = ' Not have'
		return x

	def in_order(self, cur_node, x ,traversal):
		if cur_node:
			traversal = self.in_order(cur_node.left,x, traversal)
			if cur_node.data < x: 
				traversal += str(cur_node.data) + ' '
			traversal = self.in_order(cur_node.right,x, traversal)
		return traversal

	def __search_min(self, cur_node, x):
		s = ''
		if cur_node is not None:
			s += self.__search_min(cur_node.left,x) + ' '
			if cur_node.data < x :
				s += str(cur_node.data)
			s += self.__search_min(cur_node.right,x) 
		return s   

	def printTree(self, node, level = 0):
		if node != None:
			self.printTree(node.right, level + 1)
			print('     ' * level, node.data)
			self.printTree(node.left, level + 1)
	
T = BST()
inp0 = input('Enter Input : ').split('|') 
inp = [int(i) for i in inp0[0].split()] 
m = int(inp0[-1])
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print(f'Below {m} :{T.search_min(m)}')
# print(T.search_min(m))
