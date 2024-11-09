#Star Clayton
#Nov. 8, 2024
#P4HW2_Salary
#Calculate salary

#Program will take input and calculate and display nicely. 


# Initialize variables for totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
total_employees = 0
overtime_hours = 0
# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
total_employees = 0

# Main loop to input employee data
while True:
    employee_name = input("Enter employee's name: 'none' to exit.")
    
    if employee_name.lower() == 'none':
        break
    
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    # Calculate pay
    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        regular_pay = hours_worked * pay_rate
        overtime_hours = 0
        overtime_pay = 0
    gross_pay = regular_pay + overtime_pay
    
    # Update totals
    total_employees += 1
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    print('- ' * 30)
    # Display employee details
    print(f"Employee name: {employee_name}")
    print('-' * 25)
    # Print the header with properly aligned columns
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime pay':<15}{'Reg/HourPay':<15}{'Gross Pay':<15}")

    # Print the data row with values properly aligned in the columns
    print(f"{hours_worked:<15.1f}{pay_rate:<15.2f}{overtime_hours:<15.1f}{overtime_pay:>10.2f}{regular_pay:>14.2f}{gross_pay:>15.2f}")
    print('-' * 75)

    # Display totals
    print(f"Total number of employees entered: {total_employees}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
    print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
