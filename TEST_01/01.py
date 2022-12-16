str1 = input('String 1: ')
str2 = input('String 2: ')

def swap(str1, str2):
	str1, str2 = str2, str1
	return (str1, str2)

str1, str2 = swap(str1, str2)

print('First string is ' + str1 + ' and second string is ' +str2)