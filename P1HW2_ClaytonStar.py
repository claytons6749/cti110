# Star Clayton
# September 19, 2024
# P1HW2
#  Using mathematical equation in code for travel expenses.

# Get input from users
print ("---This program calcutes and display travel expenses---")
print()
bud = float(input("Enter your budget:"))
dest = input("Enter Destination:")
gas = float(input("Enter what you will spend on gas:"))
acc = float(input("Enter what you think you will spend on accommodation:"))
food = float(input("Enter what you spend on food:"))

# Calculate planned budget
bud2 = gas + acc + food

# Calculate remaining budget
bal = bud - gas - acc - food

#output values
print()
print("------Travel Expenses-------")
print()
print(f"Location: {dest}")
print(f"Inital Buget: {bud}")
print()
print(f"Fuel: {gas}")
print(f"Accommodation: {acc}")
print(f"Food: {food}")
print()
bal = bud - gas - acc - food
print(f"Remaining Balance: {bal}")
