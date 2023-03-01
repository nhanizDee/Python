#Nhan Nguyen
#Max Raven
#Cochise Nava
#Date: Feb 27, 2023
#Program 2: Cellphone Bill custom

# Declare package
# Prompt user for package type
package = input("Which package have you purchased (A, B, C, D, or E)? ")

# Validate Package
while package not in ["A", "B", "C", "D", "E"]:
    package = input("Invalid input. Please choose package A, B, C, D, or E: ")

# Pakage E then the monthly bill is just 69.99 for unlimmited    
if package == "E":
    monthly_bill = 69.99
    print(f"Your monthly bill is ${monthly_bill:.2f}")
# if packgae in not E and is one of the other options
elif package != "E":
    # get the total time of user
    minutes= int(input("Enter how many minutes you use your phone: "))
    # Validate time
    while minutes < 0:
        minutes = int(input('Invalid value. Minute must be positive, input new amount of minute: '))
    # counting the bill
    if package == "A":
        monthly_bill = 29.99 + max(0, minutes- 250)*0.27 #The max() function returns the item with the highest value, or the item with the highest value in an iterable.

                                                         #If the values are strings, an alphabetically comparison is done.
    elif package == "B":
        monthly_bill = 39.99 + max(0, minutes- 500)*0.23
    elif package == "C":
        monthly_bill = 49.99 + max(0, minutes- 750)*0.21
    else:
        monthly_bill = 59.99 + max(0, minutes- 1000)*0.19
    print(f"Your monthly bill is ${monthly_bill:.2f}")
