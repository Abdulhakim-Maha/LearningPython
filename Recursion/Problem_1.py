'''
Given a string, find the first Capital letter
'''
input_number1 = 'Iloveprogramming'
input_number2 = 'iloveProgramming'
input_number3 = 'iloveprogramming'

#iterative
def find_uppercase_iterative(s):
	for i in range(len(s)):
		if s[i].isupper():
			return s[i]
	return 'No Capital Letter Found'

#Recursive
def find_uppercase_recursive(s, idx = 0):
	if s[idx].isupper():
		return s[idx]
	if idx == len(s) - 1:
		return 'No Capital Letter Found'
	return find_uppercase_recursive(s, idx+ 1)


print(find_uppercase_iterative(input_number1))
print(find_uppercase_iterative(input_number2))
print(find_uppercase_iterative(input_number3))
print()
print(find_uppercase_recursive(input_number1))
print(find_uppercase_recursive(input_number2))
print(find_uppercase_recursive(input_number3))

