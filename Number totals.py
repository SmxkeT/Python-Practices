#Prompt for 10 numbers and total + display them.


def whilecounting(): #function to be called.
    count = 0 #var storage
    numstore = 0
    while count < 10: #while loop to iterate 10 times and add all the numbers. 
        numbers = int(input("Enter a number: ")) #take user inputs.
        count += 1 #add 1 to count per iteration to end loop once count var = 10
        numstore += numbers
    print(f"The total of all numbers entered are: {numstore}") #display results of 10 iterations added. 
        

def counting(): #function to call. 
    numstore = 0 #var storage
    for i in range(10): #for loop to iterate 10 times and add all the numbers. 
        numbers = int(input("Enter a number: ")) #take user inputs.
        numstore += numbers #add users inputs to var.numstore

    print(f"Total of all numbers entered are: {numstore}") #display results. 

whilecounting() #calling function

