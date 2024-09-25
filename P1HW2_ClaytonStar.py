# Star Clayton
# September 19, 2024
# P1HW2
#  Using mathematical equation in code for travel expenses.

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
