print('*** Reading E-Book ***')
text,highlight = [i for i in input('Text , Highlight : ').split(',')]
show_text = ''
for i in range(len(text)):
	if text[i] == highlight:
		show_text += '[' + text[i]  +']'
	else:
		show_text += text[i]
print(show_text)
