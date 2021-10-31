class Queue:
	def __init__(self) -> None:
		self.q = []
	def enqueue(self, item):
		self.q.append(item)
	def dequeue(self):
		return self.q.pop(0)
	def __str__(self) -> str:
		return str(self.q)
	def isEmpty(self):
		return len(self.q) == 0

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

	def in_order(self,cur):
		if cur is not None:
			self.in_order(cur.left)
			print(cur.data,end=' ')
			self.in_order(cur.right)
	def pre_order(self,cur):
		if cur is not None:
			print(cur.data,end=' ')
			self.pre_order(cur.left)
			self.pre_order(cur.right)
	def post_order(self,cur):
		if cur is not None:
			self.post_order(cur.left)
			self.post_order(cur.right)
			print(cur.data,end=' ')
	def breadth(self,root):
			q = Queue()	
			q.enqueue(root)
			while not q.isEmpty():
				n = q.dequeue()
				print(n.data,end=' ')
				if n.left:
					q.enqueue(n.left)
				if n.right:
					q.enqueue(n.right)

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node.data)
        printTree90(node.left, level + 1)

data = input('Enter Input : ').split()
tree = BST()
for i in data:
	tree.insert(int(i))
# printTree90(tree.root)
print('Preorder : ',end='')
tree.pre_order(tree.root)
print('\nInorder : ',end='')
tree.in_order(tree.root)
print('\nPostorder : ',end='')
tree.post_order(tree.root)
print('\nBreadth : ',end='')
tree.breadth(tree.root)
