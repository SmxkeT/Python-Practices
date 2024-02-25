#expenses calculator


def monthlycost():
    total = []
    many = int(input("How many expenses will you enter?: "))
    
    for i in range(many):
        xpense = float(input("Enter an expense: "))
        total.append(xpense)
    return total
    
def calculation(math):
    monthly = 0
    for i in range(len(math)):
        monthly += math[i]
    return monthly
    
completecost = monthlycost()

print(f"The total monthly costs added are: ${calculation(completecost)} for this month")
    
