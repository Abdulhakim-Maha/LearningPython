def count_datatype(inp): # ['a', 132 , 'b', 5]
	numeric_data = 0;
	non_numeric_data = 0;
	for i in inp:
		if i.isdecimal():
			numeric_data += 1
		else:
			non_numeric_data += 1
	return numeric_data, non_numeric_data

num = input('Enter many numbers (n): ')
inp = [i for i in input('Enter member in list: ').split(' ')] # list comprehensive
numeric, non = count_datatype(inp)
print('The number of numeric data is', str(numeric)+ '.')
print('The number of non-numeric data is', str(non) + '.')