arr = []
print('*** TorKham HanSaa ***')
express = input('Enter Input : ').split(',')
for i in range(len(express)):
	if express[i].split(' ')[0] == 'P':
		if len(arr) == 0:
			word = express[i].split(' ')[-1]
			arr.append(word)
			print('\'{}\' -> {}'.format(word,arr))	
		else:
			lastList = arr[-1]
			# print(lastList)
			appendList = express[i].split(' ')[-1]
			if lastList[-2:].lower() == appendList[:2].lower():
				arr.append(appendList)
				print('\'{}\' -> {}'.format(appendList,arr))	
			else:
				print('\'{}\' -> game over'.format(appendList))
	elif express[i].split(' ')[0] == 'R':
		pass	
		print('game restarted')
		arr = []
	elif express[i].split(' ')[0] == 'X':
		break
	else:
		print('\'{}\' is Invalid Input !!!'.format(express[i]))
		break