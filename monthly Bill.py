# Prompt user for package type
package = input("Which package have you purchased (A, B, C, D, or E)? ")

while package not in ["A", "B", "C", "D", "E"]:
    package = input("Invalid input. Please choose package A, B, C, D, or E: ")
    
if package == "E":
    monthly_bill = 69.99
    print(f"Your monthly bill is ${monthly_bill:.2f}")
elif package != "E":
    minutes= int(input("Enter how many minutes you use your phone: "))
    while minutes < 0:
        minutes = int(input('Invalid value. Minute must be positive, input new amount of minute: '))
    
    if package == "A":
        monthly_bill = 29.99 + max(0, minutes- 250)*0.27
    elif package == "B":
        monthly_bill = 39.99 + max(0, minutes- 500)*0.23
    elif package == "C":
        monthly_bill = 49.99 + max(0, minutes- 750)*0.21
    else:
        monthly_bill = 59.99 + max(0, minutes- 1000)*0.19
    print(f"Your monthly bill is ${monthly_bill:.2f}")
    




