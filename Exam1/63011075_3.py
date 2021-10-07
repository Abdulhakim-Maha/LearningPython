inp = input('Enter number end with (-1) : ').split()
if not '-1' in inp:
	print('Invalid INPUT !!!')	
else:
	length = inp.index('-1') 
	# print(length)
	new_lis = []	
	for i in range(length):
		# print(inp[i])
		new_lis.append(int(inp[i]))
	print(new_lis)
	