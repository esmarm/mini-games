name = input("Please enter your name:	")
print("Hello " +name+ " Time to Play Hangman!!!")

secret_word = "i dont know why i am doing this"

guess_global = " "

lives = 10

while lives>0:
	character_left = 0

	for character in secret_word:

		if character in guess_global:
			print(character)
		else:
			print("-")
			character_left += 1
	if character_left == 0:
		print("You won!!!")
		break


	
	guess = input("Guess a word!:	")
	guess_global += guess

	if guess not in secret_word:
		lives -=1
		print("Wrong guess!!!")
		print(f"You have {lives} lives left.")

		if lives == 0:
			print("You died!!!")



