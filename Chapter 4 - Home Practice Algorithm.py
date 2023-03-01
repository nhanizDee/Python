# Algorithm Workbench
# Nhan Nguyen
# Chapter 4


# work 1
# loop enter a number, number *10,
# then assign to variable "product" , iterate as long as product <100

product = 0
while product < 100:
    num = int(input('Enter an number: '))
    product = 10*num
    print(product)

# work 2
# loop ask user to enter two number
# add the two number and the sum displayed
# ask user if they want to do it again, if Y then repeat, otherwise break
while True:
    num1 = int(input('Enter num 1: '))
    num2 = int(input("Enter num 2: "))
    sum_of_numbers = num1 + num2
    print(sum_of_numbers)
    decide = input('Do you want to keep going(Y/N): ')
    if decide == 'Y' or decide == 'y':
        continue
    else:
        break
# work 3
# write a loop print set 0,10,20,30,40,...1000
for i in range(0, 1001, 10):  # take i in a set from 0 to 1001,
    # each number on set away from each other by 10
    print(i)

# work 4
# write a loop that ask user to enter a number. The loop should iterate
# 10 times and keep a running total of the number entered.
total = 0
for i in range(10):
    num_in = int(input('Enter a number: '))
    total += num_in
print(total)

# work 5
# write a loop that calculates the total of the following series
# 1/30 + 2/29 + 3/28 + ... + 30/1

sum_fraction = 0.0
for i in range(1, 31):  # taking number in a range of 1 to n+1
    # to have last number end of n.
    sum_fraction += i/(31 - i)
print(sum_fraction)

# work 6
# augmented assignment operator
# x = x + 1
# x = x * 2
# x = x/10
# x = x -100
for x in range(100):
    x += 1
    x *= 2
    x /= 10
    x -= 100

# work 7
