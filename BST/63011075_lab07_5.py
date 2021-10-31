class Node:
	def __init__(self, data) -> None:
		self.data = data
		self.right = None
		self.left = None
	def __str__(self) -> str:
		return str(self.data)

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node.data)
        printTree90(node.left, level + 1)

def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))
 
def getInfix(exp) :
    s = []
    for i in exp:    
        if (isOperand(i)) :        
            s.insert(0, i)
        else:
            op1 = s[0]
            s.pop(0)
            op2 = s[0]
            s.pop(0)
            s.insert(0, "(" + op2 + i +
                             op1 + ")")
    return s[0]

def postToPre(post_exp):
    s = []
    length = len(post_exp)
    for i in range(length):
        if post_exp[i] in '+-*/': #(isOperator(post_exp[i]))
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])
    ans = ""
    for i in s:
        ans += i
    return ans

inp = input('Enter Postfix : ')
print('Tree :')
s = []
for i in inp:
	if i not in '+-*/':
		s.append(Node(i))
	elif i in '+-*/':
		x = Node(i)
		op2 = s.pop()
		op1 = s.pop()
		x.right = op2
		x.left = op1
		s.append(x)

printTree90(s[0])
print('--------------------------------------------------')
print('Infix :',getInfix(inp))
print('Prefix :',postToPre(inp))	
