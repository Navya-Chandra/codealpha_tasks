import random

words = ["python", "computer", "program", "application", "coding"]
word = random.choice(words)
guessed_letters = []
max_attempts = 6
wrong_guesses = 0

print(" ")
print("          HANGMAN GAME")
print(" ")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_attempts:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations!")
        print("You guessed the word:", word)
        break
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses:", wrong_guesses)
        print("Attempts remaining:", max_attempts - wrong_guesses)

if wrong_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", word)
print("\nThank you for playing!")