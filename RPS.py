import random #allowing use of the random time and OS libraries..
import time
import os

os.system("color a") #If running on console will change text to green(Just prefer how that looks, not necessarry.)

def RPS(): #Function to contain the program.
    PCScore = 0 #Vars to hold the scores of the user and computer. 
    userscore = 0
    NPC = ["R", "P", "S"] #List of choices for the computer to select.

    while(1): #While loop to take user choice, pick random pc choice and check who wins. 
        userchoice = input("Pick Rock Paper or Scissors (R/P/S): ")
        PCchoice = random.choice(NPC) #Pulls a random item from the above list.

        if PCchoice == "R" and userchoice == "R": #Comparing choices to determine winner.
            print("It's a tie, both have chosen rock!")

        elif PCchoice == "R" and userchoice == "P":
            (print("You Win!, Paper beats rock"))
            userscore += 1

        elif PCchoice == "R" and userchoice == "S":
            print("NPC Wins!, Rock beats scissors.")
            PCScore += 1

        if PCchoice == "P" and userchoice == "P":
            print("It's a draw!, Both have chosen paper.")

        elif PCchoice == "P" and userchoice == "R":
            print("NPC Wins!, Paper beats rock.")
            PCScore += 1
        
        elif PCchoice == "P" and userchoice == "S":
            print("You win!, Scissors beat paper")
            userscore += 1
        
        if PCchoice == "S" and userchoice == "S":
            print("It's a tie, both have chosen scissors.")

        elif PCchoice == "S" and userchoice == "R":
            print("You win!, Rock beats scissors")
            userscore += 1

        elif PCchoice == "S" and userchoice == "P":
            print("NPC Wins, Scissors beat paper.")
            PCScore += 1

        re = input("Do you want to play again? Y/N: ") #take input to decide for rematch.
        if re == "N":
            print("|Final Scores Loading...|") #If user says no, total the scores and display the overall winner.
            time.sleep(3)
            print(f"The computer had {PCScore} points")

            time.sleep(2)
            print(f"You had {userscore} points")
            if userscore > PCScore:
                print("YOU WIN!")
            elif userscore < PCScore:
                print("NPC WINS!")
            else:
                print("IT'S A TIE!")

            time.sleep(2) #Added so can see final result in CMD console. Would close too fast otherwise.
            input("Thank you for playing! - Press enter to exit...")
            break
        else:
            pass #If the user has selected Y, the program will pass and repeat again.

RPS() #Calling the function to run the program.