def leftside(inp):
	inp = inp[-2:] + inp[:-2]
	return inp
def rightside(inp):
	inp = inp[3:] + inp[:3]
	return inp

print('*** String Rotation ***')
inp = input('Enter 2 strings : ').split()
count = 0
dotPrint = False
# print(inp[0])
left = leftside(inp[0])
# print(inp[1])
right = rightside(inp[1])
count += 1
print('{} {} {}'.format(count,left,right))

while inp[0] != left or inp[1] != right:
	left = leftside(left)
	right = rightside(right)
	count += 1
	if count <= 5:
		print('{} {} {}'.format(count,left,right))
	elif count > 5 and dotPrint == False:
		print(' . . . . . ') 
		dotPrint = True
	# print('{} {} {}'.format(count,left,right))
if count > 5 :
	print('{} {} {}'.format(count,left,right))
print('Total of  {} rounds.'.format(count))
