def find_factor(x):
	lis = []
	for i in range(1, x+1):
		if x % i == 0:
			lis.append(i)
	return lis
print(' *** Perfect Number Verification ***')
inp = int(input('Enter number : '))
if inp < 0:
	print('Only positive number !!!')
else:
	factor = find_factor(inp)
	sum = 0
	perfect = []
	for i in range(len(factor)-1):
		perfect.append(factor[i])
		# print(factor[i])
		sum += factor[i]
	if sum == inp:
		print('{} is a PERFECT NUMBER.'.format(inp))
		print('Factors : {}'.format(str(perfect)))
	elif sum != inp:
		print('{} is NOT a perfect number.'.format(inp)) 
		print('Factors : {}'.format(str(perfect)))
