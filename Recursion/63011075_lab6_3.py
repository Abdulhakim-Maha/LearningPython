def gcd(num,divisor):
	Gcd = 1
	num1 = int(num.split()[0])
	num2 = int(num.split()[-1])
	if num1 == 0 and num2 == 0:
		return -1 	
	elif divisor <= abs(num1) and divisor <= abs(num2):
		if num1 % divisor == 0 and num2 % divisor == 0:
			num1 //= divisor 
			num2 //= divisor
			s = str(num1) +' '+ str(num2)
			Gcd *= divisor * gcd(s,divisor)
			return Gcd
		else:
			Gcd *= gcd(num,divisor+1)
			return Gcd
	else:
		return 1	

inp = input('Enter Input : ')
num1 = inp.split()[0]
num2 = inp.split()[-1]
gcd = gcd(inp,2)
if gcd != -1:
	print('The gcd of {} and {} is : {}'.format(num1,num2,gcd))
else:
	print('Error! must be not all zero.')