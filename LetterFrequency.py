#LetterFrequency.py
#Name:
#Date:
#Assignment:

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def count_letters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    freq = [0] * 26  

    for letter in message:
        if letter in alpha:
            freq[alpha.index(letter)] += 1  
    return freq

def display_frequencies(freq):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        print(f"{alpha[i]}: {freq[i]}")

def main():
    message = input("Enter a message: ")
    frequencies = count_letters(message)
    display_frequencies(frequencies)

if __name__ == "__main__":
    main()
