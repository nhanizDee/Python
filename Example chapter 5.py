# test the calculator of e^x and sin x

def main():
    number = float(input("Enter a number: "))
    exp_x = exp(number)
    sin_x = sin(number)
    print('e raise to power ', number, ' is ', format(exp_x, '.6f'), sep='')
    print('sin of ', number, ' is ', format(sin_x, '.6f'), sep='')


def exp(x):
    # x is the number to find
    expx = 1 + x + x ** 2 / 2 + x ** 3 / 6 + x ** 4 / 24 + x ** 5 / 120 + x ** 6 / 720 + x ** 7 / 5040 + x ** 8 / 40320\
           + x ** 9 / 362880
    return expx


def sin(x):
    sinx = x - x ** 3 / 6 + x ** 5 / 120 - x ** 7 / 5040 + x ** 9 / 362880
    return sinx


main()

import math


def main():
    num = float(input('Enter number'))
    exp_x = math.exp(num)
    sin_x = math.sin(num)
    cos_x = math.cos(num)

    print(' e raise ', num, ' is ', format(exp_x, '.6f'), sep='')
    print('sin of ', num, ' is ', format(sin_x, '.6f'), sep='')
    print('cos of ', num, ' is ', format(cos_x, '.6f'), sep='')


main()
# Example 16 in book
# Even Odd number
import random


def main():
    num = 0
    even_counter = 0
    odd_counter = 0
    total_number = 100
    for Counter in range(total_number):
        num = random.randint(1, 100)

        if is_even(num):
            even_counter += 1
        else:
            odd_counter += 1
    print('Out of ', total_number, 'random number', even_counter, ' were even and ', odd_counter, ' were odd')


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


main()
