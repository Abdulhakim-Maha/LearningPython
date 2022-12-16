print(' *** 3-digit odd even ***')
inp = input('Enter 3-digit number : ')
li = []
for i in inp:
	if (int(i) % 2 == 0):
		li.append('even')
	elif(int(i) % 2 != 0):
		li.append('odd')
print('{} => {} {} {}'.format(inp,li[0],li[1],li[2]))
