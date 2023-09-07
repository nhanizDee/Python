# pennies to pay
# Nhan Nguyen
# Date: feb 22, 2023
# variable
name = str(input("nhapten"))
# the function to count money S(n) = 2^n-1, when n is the number of day
# declare variable

day_penny = 1
number_of_day = 0
total = 0.00

number_of_day = int(input('Enter the num ber of day: '))
# making a table using \t to separate the line

print('Day\tPennies')
print('--------------------')

for day in range(1, number_of_day+1):
    print(day, '\tS', float(day_penny/100))
    total += day_penny
    day_penny *= 2


print(' Total amount for: ', number_of_day, 'day is $', float(total/100))
    

