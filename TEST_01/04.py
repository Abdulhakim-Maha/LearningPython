members = {}
inp = int(input('How many contact list (n)?: '))
for i in range(inp):
	x = input('Name and phone number {}: '.format(i+1)).split(' ')
	members[x[0]] = x[-1]
find = input('Find?: ')
if members.get(find) is None:
	print('Not found!')
else:
	print('Phone number of {} is {}'.format(find, members.get(find)))