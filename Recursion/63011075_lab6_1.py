def print1ToN(n):
	if n == 1 or n <= 0:
		print(1,end=' ')
		return
	else:
		print1ToN(n-1)
		print(n,end=' ')
		return 

def printNto1(n):
	if n == 1 or n <= 0:
		print(1,end='')
		return
	else:
		print(n,end=' ')
		printNto1(n-1)
		return

n = int(input('Enter Input : '))
print1ToN(n)
printNto1(n)

