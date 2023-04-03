# Nhan Nguyen
# Max Raven
# Cochise Nava
# Date: Mar 29, 2023
# Program 4: Prime Number
# Required

# A prime number is a number that is only evenly divisible by itself and 1.
# Write a Boolean function named is_prime which takes an integer as an argument and returns true if
# the argument is a prime number, or false otherwise.
# Use the function is_prime and a loop to display all the prime numbers from 1 to 100.
def is_prime(prime_num):
    if prime_num <= 1:
        return False
    for i in range(2, int(prime_num ** 0.5) + 1):
        if prime_num % i == 0:
            return False
    return True


for prime_num in range(1, 101):
    if is_prime(prime_num):
        print(prime_num, end=" ")



