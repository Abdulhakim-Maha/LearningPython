def merge_sort(l, left, right):
	center = (left + right) // 2 
	if left < right:
		merge_sort(l, left, center)
		merge_sort(l ,center + 1, right)
		merge(l, left, center + 1)

def merge():
	pass


if __name__ == '__main__':
	inp = [int(i) for i in input('Enter Input : ').split()]
	print(inp)
	merge_sort(inp,0, len(inp) -1)
	print(inp)