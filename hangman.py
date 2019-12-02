#!/usr/bin/env python3

import random

word = random.choice(["paladin", "warlock", "shaman", "mage", "warrior", "priest"])
print(word)
print(len(word))

def check(guess, guesses, word):
    displayWord = ''
    i = 0
    matches = 0
    for letter in word:
        if letter in guesses:
            displayWord += letter
            matches += 1
        else:
            displayWord += "@"
    print(displayWord)

guesses = []

def playGame():
    solved = False
    while not solved:
        print("The word has " + str(len(word)) + " letters")
        guess = input("Guess a letter!")
        if len(guess) != 1:
            print("guess one letter at a time scrub")
            playGame()
        elif guess in guesses:
            print("you already guessed that dumdum")
            playGame()
        else:
            guesses.append(guess)
            result = check(guess, guesses, word)
            print(result)
        # print(guess)
        # print(guesses)

playGame()
