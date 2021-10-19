def happynumber(n):
	sum = 0
	while n > 0 :
		sum += (n % 10) ** 2
		n //= 10
	if sum >= 0 and sum <= 9:
		return True if sum == 1 else False
	else:
		return happynumber(sum)


inp = int(input('Enter numter : '))
print(happynumber(inp))
