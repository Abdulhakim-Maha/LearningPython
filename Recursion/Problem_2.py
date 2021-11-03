'''
Given a string, find a length of a string
'''
input_number1 = 'Iloveprogramming'
input_number2 = 'austiniqer'
input_number3 = 'Valorant'

#iterative
def find_with_iterative(s):
	count = 0
	while s != '':
		s = s[1:]
		count += 1
	return count

#recursive
def find_with_recursive(s):
	if s == '':
		return 0
	else:
		return 1 + find_with_iterative(s[1:]) 

print(find_with_iterative(input_number1))
print(find_with_iterative(input_number2))
print(find_with_iterative(input_number3))
print()
print(find_with_recursive(input_number1))
print(find_with_recursive(input_number2))
print(find_with_recursive(input_number3))