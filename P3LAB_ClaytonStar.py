#Star Clayton
#Oct 19, 2024
#P3LAB3
# The program will exceted users input and will display money in the most efficient


def calculate_coins(amount):
    # Convert the amount to an integer representing cents
    total_cents = int(amount * 100)

 # If the amount is zero, notify the user
    if total_cents == 0:
        print("No change.")
        return
    
    # Calculate the number of each coin
    dollars = total_cents // 100
    total_cents %= 100

    quarters = total_cents // 25
    total_cents %= 25

    dimes = total_cents // 10
    total_cents %= 10

    nickels = total_cents // 5
    total_cents %=5

    pennies = total_cents

    # Display the results
    if dollars > 0:
        print(f"{dollars} dollar{'s' if dollars > 1 else ''}")

    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")

    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")

    if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")

    if pennies > 0:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")


# Main program
def main():
    try:
        amount = float(input("Enter a money value (e.g., 12.34): "))
        if amount < 0:
            print("Please enter a non-negative amount.")
        else:
            calculate_coins(amount)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
