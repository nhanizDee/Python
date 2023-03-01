# Nhan Nguyen
# Max Raven
# Cochise Nava
# Date: Feb 27, 2023
# Program 3: Tax Payroll
# Required

# 1- ask the user for the employee number, gross pay, state tax, federal tax,
# and FICA with-holdings.
# 2-  The loop will terminate when 0 is entered for the employee number
# 3- Display total value after entered

# no negative allow, sum of state, fed, and FICA can not over net pay

# Declare total need to report
total_gross = 0.0
total_stateT = 0.0
total_fedT = 0.0
total_FICA_wth = 0.0
total_net = 0.0

# making the loop

while True:
    # Asking for employee number
    em_num = int(input(
        'Enter employee number(enter 0 to quit): '))  # Em number will be any that > 0,
    # if 0 appear then it end of the loop.

    # Validate employee number

    if em_num < 0:
        em_num = int(input('Error: Employee number can not be negatve, re-enter it: '))
    elif em_num == 0:
        break

    # Get the information from user

    gross_p = float(input(f"Enter gross pay for employee {em_num}: "))  # Gross pay
    while gross_p <= 0:
        gross_p = float(input(f"Gross pay can not be negative, re-enter gross pay for employee {em_num}: "))

    state_tax = float(input('Enter the state tax: '))  # State tax
    while state_tax <= 0 or state_tax > gross_p:
        state_tax = float(input('State tax can not be negative or greater than gross pay re-enter state tax: '))

    fed_tax = float(input('Enter the federal tax: '))  # Federal tax
    while fed_tax <= 0 or fed_tax > gross_p:
        fed_tax = float(input('Federal tax can not be negative or greater than gross pay, re-enter federal tax: '))

    fica_wth = float(input('Enter the FICA withholding: '))  # FICA withholding
    while fica_wth <= 0 or fica_wth > gross_p:
        fica_wth = float(input('Withholding can not be negative or greater than gross pay, re-enter withholding: '))

    # Calculating net pay
    net_pay = gross_p - state_tax - fed_tax - fica_wth
    if net_pay <= 0:  # if not having <=, you can input -0 as a value, and it still counts as 0.
        print("Error: The net pay can not be negative, please check and re-enter the value!")
        continue  # restart loop for this employee

    # Update total of each value
    total_gross += gross_p  # sum all gross pay of all employee

    total_stateT += state_tax  # sum all state tax of all employee

    total_fedT += fed_tax  # sum all fed tax of all employee

    total_FICA_wth += fica_wth  # sum all withholding of all employee

    total_net += net_pay  # sum all net pay of all employee

# print totals
print("Payroll report:")
print(f"Total gross pay: ${total_gross:.2f}")
print(f"Total state tax: ${total_stateT:.2f}")
print(f"Total federal tax: ${total_fedT:.2f}")
print(f"Total FICA withholding: ${total_FICA_wth:.2f}")
print(f"Total net pay: ${total_net:.2f}")
