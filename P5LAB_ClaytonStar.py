#Star Clayton
#Nov.17, 2024
#5PLAB
# Create a self-checkout program that will display what you owe and then change you get back


import random

# Function to calculate and display the change in denominations
def dispense_change(change_owed):
    # Convert change owed to cents to avoid floating-point imprecision
    change = round(change_owed * 100)

    # Calculate each denomination
    dollars = change // 100
    change %= 100

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    # Display the change breakdown
    
    print(f"${dollars} dollars")
    print(f"{quarters} quarters")
    print(f"{dimes} dimes")
    print(f"{nickels} nickels")
    print(f"{pennies} pennies")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    # Get valid input for total owed and cash given
    total_owed = get_positive_float("You owe: $")
    cash_given = get_positive_float("How much cash will you put in the self-checkout? $")

    # Calculate the change
    change_owed = cash_given - total_owed

    if change_owed < 0:
        print("Insufficient funds provided.")
    else:
        print(f"Change is: ${change_owed:.2f}")
        dispense_change(change_owed)

# Run the main function
if __name__ == "__main__":
    main()
