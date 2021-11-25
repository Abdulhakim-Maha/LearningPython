# insertion sort implemented

def shell(l, dIncrements):
	for inc in dIncrements:
		for i in range(inc, len(l)):
			iEle = l[i]
			for j in range(i, -1, -inc):
				if iEle < l[j - inc] and j >= inc:
					l[j] = l[j - inc]
				else:
					l[j] = iEle
					break
	return l


if __name__ == '__main__':
	inp = [int(i) for i in input('Enter Input : ').split()]
	print(inp)
	dIncrements = [5,3,1]
	print(shell(inp,dIncrements))