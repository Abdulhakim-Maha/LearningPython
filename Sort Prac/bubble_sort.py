def bubble(l):
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

if __name__ == '__main__':
	inp = [int(i) for i in input('Enter Input : ').split()]
	print(inp)
	print(bubble(inp))
	