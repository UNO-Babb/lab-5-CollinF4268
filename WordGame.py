#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Check if letter is anywhere in the word."""
    return letter in word

def inSpot(letter, word, spot):
    """Check if letter is in the correct spot."""
    return word[spot] == letter

def rateGuess(myGuess, word):
    """Provide feedback on the guess."""
    feedback = ""
    for i in range(len(myGuess)):
        if inSpot(myGuess[i], word, i):
            feedback += myGuess[i].upper()  
        elif inWord(myGuess[i], word):
            feedback += myGuess[i].lower()  
        else:
            feedback += "-"  
    return feedback

def main():
    with open("words.txt", "r") as wordfile:
        wordlist = wordfile.read().splitlines()

    todayWord = random.choice(wordlist)
    print("Word selected. Start guessing!")

    attempts = 6
    while attempts > 0:
        guess = input("Enter a 5-letter word: ").lower()
        if len(guess) != 5:
            print("Invalid word length. Try again.")
            continue

        feedback = rateGuess(guess, todayWord)
        print("Feedback:", feedback)

        if feedback == todayWord.upper():
            print("Congratulations! You guessed the word.")
            break

        attempts -= 1

    if attempts == 0:
        print("Game over! The word was:", todayWord)

if __name__ == "__main__":
    main()

