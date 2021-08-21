x,y = input('Enter num1 num2: ').split()
if int(x) * int(y) > 1000:
	print('The result is',int(x)+int(y))
elif int(x) * int(y) >= 0:
	print('The result is',int(x)*int(y))