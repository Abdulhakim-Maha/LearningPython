def dec_to_bin(dec):
	s = ''
	if dec == 0:
		return 0
	else:
		while dec > 0:
			s = str(dec % 2) + s
			dec = dec // 2
		return s

def dec_to_bin_no_return(dec):
	s = ''
	if dec == 0:
		print(s)
	else:
		while dec > 0:
			s = str(dec % 2) + s
			dec = dec // 2
		print(s)

naofal = input('Enter number : ')
print(dec_to_bin(int(naofal)))
# x = dec_to_bin(10)
# print(dec_to_bin(10))
# #def name()	:
# 	statement
# def sum(number1, number2):
# 	result = number1 + number2
# 	return result
# # name = 'naofal'	

# #return value
# def substract(number1, number2):
# 	result = number1 - number2
# 	return result

# def divide(number1, number2):
# 	result = number1 // number2
# 	print(result)

# print(sum(5,10))
# substract(10,6)
# # print(divide(100,10)) #print(None)
# divide(100,9)

# x = 5 
 
# def power(nubmer):
# 	return nubmer ** 2

# y = power(x)
# print(y)
