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
		
def letters(input):
    valids = []
    for character in input:
        if character.isalpha():
            valids.append(character)
    return ''.join(valids)

inp = input('Enter Input : ')
x = inp
inp = inp.replace(' ','')
inp = letters(inp)
# print(inp)
isPalin = isPalindrome(inp)
if inp.lower() == isPalin.lower():
	print('\'{}\' is palindrome'.format(x))
else:
	print('\'{}\' is not palindrome'.format(x))