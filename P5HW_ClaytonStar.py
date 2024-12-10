#Star Clayton
# Nov.22, 2024
#P5HW
# Create a Math QUIZ which will add and substract two random numbers and will let the user know if thier answers is correct or incorrect.

import random

# Function to run the addition quiz
def addition_quiz():
    # Generate two random numbers between 1 and 999
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # Display the problem to the user
    print(f"\n{num1}")
    print(f"+ {num2}")

    # Calculate the correct answer
    correct_answer = num1 + num2

    # Variable to track the number of guesses
    guess_count = 0

    while True:
        # Ask the user for their guess
        try:
            user_guess = int(input("What is the sum? "))
            guess_count += 1  # Increment the guess count each time the user makes a guess
            
            if user_guess == correct_answer:
                print(f"Congratulations! You got it right in {guess_count} guesses!")
                break  # Exit the loop if the user guesses correctly
            elif user_guess < correct_answer:
                print("Your guess is too low. Try again.")
            else:
                print("Your guess is too high. Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Function to run the subtraction quiz
def subtraction_quiz():
    # Generate two random numbers between 1 and 999
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)

    # Display the problem to the user
    print(f"\n{num1}")
    print(f"- {num2}")

    # Calculate the correct answer
    correct_answer = num1 - num2

    # Variable to track the number of guesses
    guess_count = 0

    while True:
        # Ask the user for their guess
        try:
            user_guess = int(input("What is the difference? "))
            guess_count += 1  # Increment the guess count each time the user makes a guess
            
            if user_guess == correct_answer:
                print(f"Congratulations! You got it right in {guess_count} guesses!")
                break  # Exit the loop if the user guesses correctly
            elif user_guess < correct_answer:
                print("Your guess is too low. Try again.")
            else:
                print("Your guess is too high. Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Main function to display the menu and run the quiz
def main():
    while True:
        # Display the menu
        print("\nMath Quiz Menu:")
        print("1. Addition Quiz")
        print("2. Subtraction Quiz")
        print("3. Exit the quiz")

        # Ask the user for their choice
        choice = input("Please choose an option (1, 2, or 3): ").strip()

        if choice == "1":
            print("\nStarting Addition Quiz...")
            for i in range(5):  # Ask 5 questions for addition
                print(f"Question {i + 1}:")
                addition_quiz()
        elif choice == "2":
            print("\nStarting Subtraction Quiz...")
            for i in range(5):  # Ask 5 questions for subtraction
                print(f"Question {i + 1}:")
                subtraction_quiz()
        elif choice == "3":
            print("Thank you for playing! Goodbye.")
            break  # Exit the quiz
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main function
if __name__ == "__main__":
    main()

