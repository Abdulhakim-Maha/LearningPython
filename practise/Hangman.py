import random
run = True

def gameplay():
	vocabulary = ['book','pen','pencil','phone']
	random_word = vocabulary[random.randrange(0,len(vocabulary))]
	word_to_show = '_' * len(random_word) 
	count = 0
	corrected = 0
	gamerun = True
	while gamerun:
		print('Guess the word below:'+'\t\t\t\t\tround:',count+1)
		print(word_to_show)
		ch = input('->: ')
		for i in range(len(random_word)):
			if random_word[i] == ch:
				word_to_show = word_to_show[:i] + ch + word_to_show[i+1:]
				corrected+=1
		if corrected == len(random_word):
			print('Congratulation you win the game!!!\n')
			gamerun = False
		if count == 9:
			print('Unfortunately please try again\n')
			gamerun = False
		count+=1


while run:
	print('Welcome to the Hangman game!')
	print('press 1 to play game or press 0 to exit game:')
	num = int(input('->: '))
	if num == 1:
		gameplay()
	else:
		print('Bye bye!!!\n')
		run = False