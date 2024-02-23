#Currnecy conversion ex

#variables for the current conversion of 1 Pound.
USD = 1.27
EUR = 1.17

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


##Main Program area##
        #calling function to initiate the program.
cconverter()