def odd_list(al):
	oddlist = [i for i in al if i % 2 != 0]
	return oddlist

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
