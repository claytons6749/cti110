#Star Clayton
#Oct 27, 2024
#P4LAB2
# Use a while loop and a for loop together
'''

Get integer from user
#Determine if inegter is positive or negative
if number is positive, display multiplication tab;e
if number is negative, tell user program cannot accept if
Ask user to run again
If yes, run program
If no, end program
'''

run_again = 'yes'

while run_again != "no":

    user_num =int(input("Enter an integer"))

    if user_num >= 0:
        #display multiplication for that value and range (1-12)
        for item in range (1, 13):
            print(f"{user_num} * {item} = {user_num * item}")          
    else:
        print("This program doesn't handle negative numbers")

    run_again = input("Would you like to run the program again?")

#Loop is broken. User entered 'no'
print("Program is ending....")

