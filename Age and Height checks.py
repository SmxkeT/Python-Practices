#Age prompt to determine if mature student. 

def mature():
    age = int(input("Enter your age here: "))
    if age >= 21:
        print("You are a mature student.")
    elif age < 21:
        print("You are not a mature student")

def tallcheck():
    height = float(input("Enter your height in metres: "))
    if height >= 1.90:
        print("You are very tall")
    elif height < 1.90:
        print("You are not tall")

tallcheck()