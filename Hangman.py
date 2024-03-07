import time
import os
import random #adding libraries. 

words = ["stonks", "daverino", "peetah", "test", "cat", "dog", "chungus", "apple"]

def welcome(): #function to introduce user to the game.
    print("Welcome to hangman.")
    time.sleep(1) #wait for 1 second.
    print("A random word will be chosen and you must figure out the word letter by letter.")
    time.sleep(1)
    print("If you can't do it fast enough, you will lose, good luck!")
    print("Game Loading....")
    time.sleep(5)

def hangman(word, letters): #function to take 2 arguments and join and display text as _____ 
    guess = "".join([(x if word in x else "_")for x in word])
    return guess
