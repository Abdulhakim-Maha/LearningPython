import random
def random_three_dice() :
	return random.randint(1,6)+random.randint(1,6)+ random.randint(1,6)
time = 1;
score = 0;
print("Hi, welcome to our game!")
print("can u guess what's the sum of random three dice:")
print("if the sum is between 11 - 19 press the h button")
print("and if the sum is between 1 - 10 press the i button")
while(time <= 10):
	guess = input("press h or i: ")
	randoms = random_three_dice()
	if guess != 'i' and guess != 'h':
		print('please enter a letter i or h')
		time -= 1
	if randoms >= 11 and guess == 'h':
		score += 1
	elif randoms <= 10 and guess == 'i':
		score += 1
	time += 1
print('Congratualtion!, your score is',score)