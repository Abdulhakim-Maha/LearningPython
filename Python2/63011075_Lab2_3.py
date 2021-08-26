def listHandler(listParam, eOv):
	reList = []
	if eOv == 'Even':
		for i in range(len(listParam)):
			if (i+1) % 2 == 0:
				reList.append(listParam[i])
	elif eOv == 'Odd':
		for i in range(len(listParam)):
			if (i+1) % 2 != 0:
				reList.append(listParam[i])
	return reList

def stringhandler(strParam, eOv):
	reStr = ''
	if eOv == 'Even':
		for i in range(len(strParam)):
			if (i+1) % 2 == 0:
				reStr += strParam[i]
	elif eOv == 'Odd':
		for i in range(len(strParam)):
			if (i+1) % 2 != 0:
				reStr += strParam[i]
	return reStr
	
print('*** Odd Even ***')
typ, data, eOv = input('Enter Input : ').split(',')
if typ == 'S' :
	arr = stringhandler(data, eOv)
elif typ == 'L' :
	arr = listHandler(data.split(), eOv) 


print(arr)