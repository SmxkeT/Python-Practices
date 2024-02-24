### Fortune teller ###


import time #allowing usage of time

def tellfortune(spouse, children, location, job): #function with 4 arguments to fill and call.
    print("Welcome to fortune teller...")

    time.sleep(2) #sleep command to give pause to commands.
    print("Calculating fortune...")

    time.sleep(5)
    print(f"You will be married to {spouse}, with {children} in {location}, working as a {job}") #displaying the 4 arguments in string.
    

tellfortune("kat", "3 kids", "Japan", "Programmer")     #calling functionsss
tellfortune("Kato", "2 children", "Korea", "Software Dev")
tellfortune("katto", "1 child", "UK", "owl tamer")