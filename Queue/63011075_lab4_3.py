code,hint = input('Enter code,hint : ').split(',')
q = []
diff = ord(hint) - ord(code[0])
# print(diff)
for i in code:
	q.append(chr(ord(i) + diff))
	print(q)
