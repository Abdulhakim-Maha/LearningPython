def check_is_int(x):
	isinstance(x, int)

def sum_of_digit(num):
	sum = 0
	while num > 0:
		sum += num % 10
		num //= 10
	# print(sum)
	return sum

def bubble_sort_with_sum(l):
	for last in range(len(l) -1 , -1 ,-1): # from last index to index zero
		# print(last)
		swaped = False
		for i in range(last):
			if sum_of_digit(l[i]) < sum_of_digit(l[i+1]):
				l[i], l[i+1] = l[i+1], l[i]
				swaped = True
		if not swaped:
			break
	return l	

ls = []

num = int(input('How many numbers(n)?: '))
for i in range(num):
	inp = int(input('Number {}: '.format(i+1)))
	ls.append(inp)
for i in ls:
	check_is_int(i)
	
print(ls)
print(bubble_sort_with_sum(ls))