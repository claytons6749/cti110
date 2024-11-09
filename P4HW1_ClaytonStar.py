def get_letter_grade(average):
    # Assigning letter grade based on the average score
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Ask user for the number of scores
    while True:
        try:
            modules_scores = int(input("Enter the number of scores you would like to enter: "))
            if modules_scores < 1:
                print("Please enter a positive number for the number of scores.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    scores = []
    
    # Collecting valid scores using a loop
    for i in range(modules_scores):
        while True:
            try:
                score = float(input(f"Enter score {i + 1} (between 0 and 100): "))
                # Validate score range
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Invalid score. Please enter a score between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number for the score.")

    # Dropping the lowest score
    scores.sort()  # Sort the scores in ascending order
    scores.pop(0)  # Remove the lowest score

    # Calculating the average after dropping the lowest score
    average = sum(scores) / len(scores)
    
    # Display the average
    print(f"\nAverage score (after dropping the lowest): {average:.2f}")
    
    # Determine the letter grade
    grade = get_letter_grade(average)
    print(f"Letter grade: {grade}")

# Run the program
main()


