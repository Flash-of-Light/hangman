#!/usr/bin/env python3

import random

def createWord():
    createWord.word = random.choice(["paladin", "warlock", "shaman", "mage", "warrior", "priest", "rogue", "raganaros"]).upper()
    # print(createWord.word)
    # print(len(createWord.word))

def check(guess, guesses, word):
    displayWord = ''
    i = 0
    matches = 0
    for letter in createWord.word:
        if letter in guesses:
            displayWord += letter
            matches += 1
        else:
            displayWord += "@"
    print(displayWord.upper())
    if guess in createWord.word:
        print("yes good guess")
    elif guess not in createWord.word:
        print("no bad guess")
    if matches == len(word):
        print("that's it you won! Time for a new game!")
        playGame()
        
def playGame():
    createWord()
    guesses = []
    solved = False
    print("The secret word has " + str(len(createWord.word)) + " letters.")
    while not solved:        
        guess = input("Guess a letter!").upper()
        if len(guess) != 1:
            print("guess one at a time scrub")
        elif guess in guesses:
            print("you already guessed that dumdum! here are your guesses to remind you.")
            print(guesses)
        elif not str.isalpha(guess):
            print("guess a letter ya turd")
        else:
            guesses.append(guess)
            check(guess, guesses, createWord.word)
            
playGame()
