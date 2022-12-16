def to_jaden_case(string):
	ls = string.split(' ')
	newStr = []
	for i in ls:
		newStr.append (i[0].upper() + i[1:]) 
	newStr = ' '.join(newStr)
	return newStr

def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())
	
if __name__ == '__main__':
	quote = "How can mirrors be real if our eyes aren't real"
	print(to_jaden_case(quote))