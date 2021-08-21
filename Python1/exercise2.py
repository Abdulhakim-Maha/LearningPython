print('*** multiplication or sum ***')
x,y = [int(i) for i in input('Enter num1 num2 : ').split()]
if x * y > 1000:
	print('The result is', x + y)
else:
	print('The result is',x * y)