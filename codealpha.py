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
    import random

words = ["apple", "tiger", "house", "plant", "chair"]
secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

while incorrect_guesses < max_attempts:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed.")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Remaining attempts:", max_attempts - incorrect_guesses)

if incorrect_guesses == max_attempts:
    print("Game Over!")
    print("The word was:", secret_word)