def quick_sort(ls):
	length = len(ls) 
	if length <= 1:
		return ls
	else:
		pivot = ls.pop()

		greater_ls = []
		lower_ls = []
		
		for item in ls:
			if item > pivot:
				greater_ls.append(item)
			else:
				lower_ls.append(item)

	return quick_sort(lower_ls) + [pivot] + quick_sort(greater_ls)


if __name__ == '__main__':
	inp = [int(i) for i in input('Enter Input : ').split()]
	print(inp)
	print(quick_sort(inp))

