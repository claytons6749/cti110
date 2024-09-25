# Star Clayton
# September 19, 2024
# P1HW1
#  Using mathematical equation in code for travel expenses.
# this program allows the user select a Destination and set a budget
# example 
# The user enters a budget amount.
# The user enters their Destination.
# The user enter what they will spend on gas.
# The user enters what they will spend on accommodation.
# The user enters what they will spend obn food.
# The program will then  print out location and budget
# followed by a list of the enter budget items and amount
# The program will then subtract the gas, accommodation, & food from the budget and print the results.

print ("---This program calcutes and display travel expenses---")
print()
bud = int(input("Enter your budget:"))
dest = input("Enter Destination:")
gas = int(input("Enter what you will spend on gas:"))
acc = int(input("Enter what you think you will spend on accommodation:"))
food = int(input("Enter what you spend on food:"))
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
