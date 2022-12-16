inp = [i for i in input('Enter number: ').split(' ')]
inp.sort()
# print(inp)
temp = ''
for i in range(len(inp)):
	temp += inp.pop(0)
	print(temp)