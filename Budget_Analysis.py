# budget analysis
# Nhan Nguyen
# Date: Feb 22, 2023

# Declare the variables
budget = 0.00
difference = 0.00
total = 0.00
spent = 1.0


budget = float(input(" enter your budget: "))
while spent !=0:
    spent = float(input(" enter amount spent(0 to quit): "))
    total += spent
  

print(" Budget amount: $", format(budget, '.2f'))
print(" Amount spent: $", format(total, '.2f'))
    
if budget> total:
    difference = budget - total
    print("You are $", format(difference, '.2f'), ' under the budget.')
elif budget< total:
    difference= total - budget
    print(' You are $', format(difference, '.2f'), ' over the budget.')
else:
    print(' Good planing!')
