def bubble_sort(l):
	for last in range(len(l) -1 , -1 ,-1): # from last index to index zero
		# print(last)
		swaped = False
		for i in range(last):
			if l[i] > l[i+1]:
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

print(bubble_sort(ls))