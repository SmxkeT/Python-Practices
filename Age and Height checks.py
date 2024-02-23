#Age prompt to determine if mature student. 

#function to call
def mature():
    age = int(input("Enter your age here: ")) #take numbers as whole numbers and output based on input.
    if age >= 21:
        print("You are a mature student.")
    elif age < 21:
        print("You are not a mature student")


        #function to call
def tallcheck():
    height = float(input("Enter your height in metres: ")) #take numbers as floating point numbers and output based on input
    if height >= 1.90:
        print("You are very tall")
    elif height < 1.90:
        print("You are not tall")

tallcheck() #calling function 