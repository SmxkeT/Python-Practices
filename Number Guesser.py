import time #Importing Libraries.
import os
import random

os.system("color a") #Changes CMD and terminal text to Green.

def numguess(): #Function containing the program
    guess = random.randint(1, 100) #Selects a random int between 1 and 100
    tries = 0 #Var storage to total attempts.

    print("Welcome to number guessing game!") # Display Game rules and intro.
    time.sleep(2)
    print("You have limited tries, but you won't know how many tries you have!")
    time.sleep(2)
    print("Good Luck!!")
                                
    for i in range(guess): #loop to iterate by num in guess var
        userguess = int(input("Enter a number between 1 - 100!: ")) #Take user attempt.
        tries += 1 #add attempts to tries var 
        if userguess == guess:
            print(f"Correct! You got it right the number was {guess}")
            print(f"It took you {tries} attempts out of {(round(guess / 2))}!") #Display winner message and tries used/had if guess is correct.
            
            input("Thank you for playing! | Press Enter to exit") #take input to exit program 
            break
        
        elif userguess < guess: 
            print("Not quite right, aim a bit higher..")
            time.sleep(1) #Display if the guess is lower than the number.

        else: #If neither of the above then number must be higher and will display this.
            print("Getting warmer, aim a little lower..")
            time.sleep(1)

        if tries == guess / 2: #Will display if the user has expended their tries. | /2 to give half the random number as the amount of tries.
            print(f"Unlucky the answer was {guess}! Better luck next time.")
            input("Thank you for playing! ||| Press Enter to exit")
            break

#####################
 #Main Program
#####################
            
numguess() #calling function to initiate the program.


