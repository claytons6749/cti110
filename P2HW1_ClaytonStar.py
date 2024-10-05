# Star Clayton
# September 19, 2024
# P1HW1
#  Using mathematical equation in code for travel expenses.

# Get Inputs from users
print ("---This program calcutes and display travel expenses---")
print()
bud = float(input("Enter your budget:"))
dest = input("Enter your travel Destination:")
gas = float(input("Enter how much will you spend on gas:"))
acc = float(input("Enter how much will you need for accommodation:"))
food = float(input("Enter how much you will need for food:"))

# Calculate the total planned budget
bud2 = gas + acc + food

# Calculate the remaining balance
bal = bud - gas - acc - food

# Output the balances
print()
print("--------------Travel Expenses----------------")
print(f"Location:                   {dest}")
print(f"Inital Buget:              ${bud:.2f}")
print(f"Fuel:                      ${gas:.2f}")
print(f"Accommodation:             ${acc:.2f}")
print(f"Food:                      ${food:.2f}")
print('---------------------------------------------')
print()
print(f"remaining balance:         ${bal:.2f}")

