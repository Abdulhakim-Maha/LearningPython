# s = 'austsua'
# y = s[::-1]
# print(s)
# print(y)
def isPalindrome(st):
	s = ''
	if len(st) == 0:
		return s
	elif len(st) == 1:
		s += st[-1]
		return s
	else :
		s += st[-1] + isPalindrome(st[:-1])
		return s

inp = input('Enter Input : ')
isPalin = isPalindrome(inp)
if inp == isPalin:
	print('\'{}\' is palindrome'.format(inp,))
else:
	print('\'{}\' is not palindrome'.format(inp,))

