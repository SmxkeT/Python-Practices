#Fortune teller

import time #allows usage of time functions.

def tellfortune(spouse, kids, location, job): #function to facilitate 4 arguments.
    print("Welcome to fortune teller!")
    time.sleep(2) #delays next line by 2 seconds.

    print("Calculating your fortune, please wait...")
    time.sleep(5) 
                                        #display the fortune and insert options into the arguments. 
    print(f"You will be married to someone named {spouse} with {kids} kid(s), living in {location} working as a {job}")


tellfortune("Kat", 1, "UK", "Software Dev")
tellfortune("Katto", 2, "Korea", "Programmer")
tellfortune("Kattooo", 3, "Japan", "Tester")    #calling the function 3 times with different options.