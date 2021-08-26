def weirdSubtract(n,k):
	if k == 0:
		return n
	checkZero =	n % 10 
	if checkZero == 0:
		n = n // 10
	else:
		n -= 1
	k -= 1
	b = weirdSubtract(n,k)
	return b
	
n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))