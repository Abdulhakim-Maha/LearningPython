def selection(l):
	for last in range(len(l) -1, -1, -1):
		biggest = l[0]
		biggest_i = 0
		for i in range(1, last + 1):
			if l[i] > biggest:
				biggest = l[i]
				biggest_i  = i
		l[last], l[biggest_i] = l[biggest_i], l[last]
	return l

def selection_2(list_a):
	for i in range(0, len(list_a) -1 ):
		min_value = i
		for j in range(i+1, len(list_a)):
			if list_a[j] < list_a[min_value]:
				min_value = j
		if min_value != i:
			list_a[min_value],list_a[i] = list_a[i],list_a[min_value	]
	return list_a


if __name__ == '__main__':
	inp = [int(i) for i in input('Enter Input : ').split()]
	print(inp)
	# print(selection(inp))
	print(selection_2(inp))