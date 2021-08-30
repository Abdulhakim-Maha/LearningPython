import random
fruits = ["grape","banana","apple","orange","mango","strawberry","mangosteen","guava","cherry","kiwi"]

menu = "1"
while menu == "1": 
  word = str(random.choice(fruits))
  allowed_errors = 10
  guesses = []
  done = False
  print("menu \n1.play game\n2.end game")
  menu = input()
  if menu == '2':
	  done = True
	  break
  print("start game\n'fruits'")

  while not done:
    for letter in word:
     if letter.lower() in guesses:
        print(letter, end=" ")
     else:
        print("", end=" ")
       #print("")

    guess = input(f"\nAllowed Errors left {allowed_errors}, guess! : ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
     allowed_errors -= 1
    if allowed_errors == 0:
     break

    done = True
    for letter in word:
      if letter.lower() not in guesses:
       done = False

  if done:
     print(f"You got it! It was {word}. ")
  else:
     print(f"Game over, The word is {word}! ")

  print("Do you want to play again?")