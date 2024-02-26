
            #function
def expenses():
    ls = [] #Ask for amount of integers that will be entered. 
    many = int(input("How many expenses do you want to enter?: "))

    for i in range(many):   #Loop to iterate x amount based on many var.
        xpense = float(input("Enter the expense amount: "))
        ls.append(xpense) #add the userinp to the empty list.
    return ls

#function
def xpcalculator(math):
    final = 0

    for i in range(len(math)):  #Loop to iterate the length of the list passed into the function
        final += math[i] #add the total to the final var.
    return final

expensecalculator = expenses() #Turning expenses function into var to pass into xpcalculator function.

#### calling the xpcalc function with the list of expenses as the argument to be looped through and displayed.
print(f"The total amount of monthly expenses are: {xpcalculator(expensecalculator)}")