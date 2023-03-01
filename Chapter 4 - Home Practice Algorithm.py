# Algorithm Workbench
# Nhan Nguyen
# Chapter 4

# work 1
# loop enter a number, number *10,
# then assign to variable "product" , iterate as long as product <100

product = 0
while product < 100:
    num = int(input('Enter a number: '))
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

# another way for 2
again = "Y"
while again == "Y":
    number1 = float(input('Enter 1: '))
    number2 = float(input('Enter 2: '))
    sum_two_no = number1 + number2
    print(f"The sum of two number is {sum_two_no}")
    again = input("Want to keep going(Y/N): ")

# work 3
# write a loop print set 0,10,20,30,40,...1000
for i in range(0, 1001, 10):  # take i in a set from 0 to 1001,
    # each number on set away from each other by 10
    print(i)

# work 4
# write a loop that ask user to enter a number. The loop should iterate
# 10 times and keep a running total of the number entered.
total = 0  # should let it be using data type 'float' rather than just 'int'.
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

# another way for 5
denominator = 30
total = 0
for number in range(1, 31):
    val = number/denominator
    total += val
    denominator -= 1
print(total)

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
# write a nested loop that print 10 row, each row have 15 character '#'.
for i in range(10):
    for j in range(15):
        print('#', end="")
    print()
# work 8
# write a program that prompts user to enter a number that positive and nonzero. Validate it.
while True:
    num_nonzero = int(input('Enter a nonzero positive number: '))  # should use float for more option
    # of a nonzero positive number
    if num_nonzero > 0:
        break
    else:
        print('Can not be negative or equal 0.Input another number.')
print(num_nonzero)

# work 9
#
num = int(input("Enter number between 1 and 100: "))
while num < 1 or num > 100:
    print("Invalid value, enter another number!")
    num = int(input("Enter number between 1 and 100: "))
print(num)
