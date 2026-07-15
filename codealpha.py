print("Welcome to Hangman Game!")
import random

words = ["apple", "tiger", "house", "plant", "chair"]

secret_word = random.choice(words)

print("Welcome to Hangman Game!")
print("Selected word:", secret_word)   # Remove this later
import random

words = ["apple", "tiger", "house", "plant", "chair"]
secret_word = random.choice(words)

guessed_letters = []

guess = input("Enter a letter: ").lower()

guessed_letters.append(guess)

display_word = ""

for letter in secret_word:
    if letter in guessed_letters:
        display_word += letter + " "
    else:
        display_word += "_ "

print(display_word)
import random

words = ["apple", "tiger", "house", "plant", "chair"]
secret_word = random.choice(words)

guessed_letters = []

while True:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    if "_" not in display_word:
        print("You Win!")
        break

    guess = input("Enter a letter: ").lower()

    guessed_letters.append(guess)