# swap upper to lower and vise versa
def swap(string_):
	new = ''
	for i in string_:
		if i == i.upper():
			new = new[:] + i.lower()
		elif i == i.lower():
			new = new[:] + i.upper()
	return new

print(swap('Iqer'))