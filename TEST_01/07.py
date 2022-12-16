def explode(s):
	st = ''
	for i in s:
		st = st[:] + str(i) * int(i)
	return st

print(explode('123'))