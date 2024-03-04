import time #Importing Libraries.
import os
import random

os.system("color a") #Changes CMD and terminal text to Green.

def numguess(): #Function containing the program
    guess = random.randint(1, 100) #Selects a random int between 1 and 100
    tries = 0 #Var storage to total attempts.

    high = ["That was too high", "Try lower next time", "Small numbers can be good too"] #Lists containing strings to give hints to the users. 
    low = ["That wasn't high enough", "Try aiming higher next time", "Some say bigger is better"]

    print("Welcome to number guessing game!") #Game rules and intro.
    time.sleep(2)
    print("You have a random amount of tries...")
    time.sleep(2)
    print("Good Luck!!")
                                
    for i in range(guess): #loop to iterate by whatever number the computer has chosen for the guess.
        userguess = int(input("Enter a number between 1 - 100!: ")) #Take user attempt.
        tries += 1 #add attempts to tries var 
        if userguess == guess:
            print(f"Correct! You got it right the number was {guess}")
            print(f"It took you {tries} attempts out of {round(guess / 2)}!") #Divide guess by 2 and display if guess correct.
            
            input("Thank you for playing! | Press Enter to exit") #take input to exit program 
            break
        
        elif userguess < guess: 
            print(random.choice(low)) #take a random string from the low var list to give a hint.
            time.sleep(1) #Display if the guess is lower than the number.

        else: #If neither of the above then number must be higher and will display this.
            print(random.choice(high)) #Take a random string from the high var list to give a hint
            time.sleep(1)

        if tries == guess / 2: #Will display if the user has expended their tries.
            print(f"Unlucky! the random number was {guess}!, you have ran out of attempts, better luck next time.")
            input("Thank you for playing! | Press Enter to exit")
            break

#####################
 #Main Program
#####################
            
numguess() #calling function to initiate the program.


