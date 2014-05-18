# Tuple Program
import random

# Immutable tuple to store words
WORDS = ("python", "easy", "apples", "blueberries", "java", "html", "inventory")

# Chose a random word from the list
word = random.choice(WORDS)

# The correct word
correct = word

# Jumble the word
jumble = ""

while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position + 1):]

print("The word is: ", jumble)
guess = input("Guess: ")
guess = guess.lower()
while (guess != correct) and (guess != ""):
	print("The word is: ", jumble)
	print("Sorry that is not correct")
	guess = input("Guess: ")
	guess = guess.lower()

if guess == correct:
	print("That's it! You win")

