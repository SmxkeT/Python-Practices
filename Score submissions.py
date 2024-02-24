#Take scores until there are none remaining.

def scoretrack(): #function to be called
    count = 0 #var storage to total
    print("Welcome to score submissions, enter your scores below: ")

    while(1): #while loop to iterate until the user has no more scores to enter
        score = int(input("Enter score out of 100: "))
        count += score                                   #adding userinput to count variable to total.
        ask = input("Do you have another score? Y/N: ")
        if ask == "N":
            print(f"Total of scores is: {count}")
            break
        
        elif ask == "Y":
            pass

        else:
            print("Wrong Input retry!")


scoretrack() #calling function