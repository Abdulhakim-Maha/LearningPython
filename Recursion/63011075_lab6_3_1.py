def gcd(a,b):
	if(b==0):
		if a>=0:
			return a
		else:
			return -a
	else:
		return gcd(b,a%b)

num1,num2 = input('Enter Input : ').split()
if num1 == num2:
	print('Error! must be not all zero.')
elif num1 > num2:
	print('The gcd of {} and {} is : {}'.format(int(num1),int(num2),gcd(int(num2),int(num1))))
elif num1 < num2:
	print('The gcd of {} and {} is : {}'.format(int(num2),int(num1),gcd(int(num1),int(num2))))