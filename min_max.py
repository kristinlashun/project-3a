print("How many integers would you like to enter?")
num = int(input())

highest = None
lowest = None

print("Please enter", num, "integers.")
while num > 0: 
    user_input = int(input())

    if highest is None or user_input > highest:
        highest = user_input  
    if lowest is None or user_input < lowest:
        lowest = user_input

    num = num - 1

print("min:", lowest)
print("max:", highest)