#Currnecy conversion ex

#variables for the current conversion of 1 Pound.
USD = 1.27
EUR = 1.17

miles = 1
kilometer = 1.60

def cconverter(): #Function to convert the currency 
    print("Welcome, to convert currency please enter below.")
    useramount = float(input("Enter amount to convert: ")) #Take float value from user.
    ctype = input("What currency would you like to convert to? (EUR OR USD) ") #Find out what var to calculate with

   
    if ctype == "EUR": #Times var by the amount entered by user to get the conversion rate.
        print(f"Your pounds converted to Euros are: {EUR*useramount}")
    elif ctype == "USD":
        print(f"Your pounds converted to dollars are: {USD*useramount}")
    else:
        print("Invalid input, please restart the process.") 


def DistanceCon(): #function to call
    Counter = input("Miles and Kilometers conversion - Select Miles or Kilometers: ")
    if Counter == "Miles":
        miletrav = float(input("Enter the distance to convert to kilometers: "))
        print(f"Miles converted to kilometers successfully! - Distance in Km is: {miletrav*kilometer}") #If input matches do calc and display output
    
    elif Counter == "Kilometers":
        miletrav = float(input("Enter the distance to convert to Miles: "))
        print(f"Kilometers converted to miles successfully! - Distance in Miles is: {miletrav/kilometer}")

    else:
        print("Invalid Input, please restart the process.") #break





##Main Program area##
        #calling function to initiate the program.
#cconverter()
DistanceCon()