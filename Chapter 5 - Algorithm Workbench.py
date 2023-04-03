# Chapter 5
# algorthm workbench
# 1.
def times_ten(num):
    products = num * 10
    print(" Product is: ", products)


# 2.
def show_value(quantity):
    show_value(12)


# 3.
def my_function(a, b, c):
    my_function(3, 2, 1)


# so: a==3, b==2 and c==1

# 4.
def main():
    x = 1
    y = 3.4
    print(x, y)
    change_us(x, y)
    print(x, y)


def change_us(a, b):
    a = 0
    b = 0
    print(a, b)


main()


# 1 3.4
# 00
# 1 3.4

# 5.
def my_function(a, b, c):
    d = (a + c) / b
    print(d)


# a. my_function(a=2,b=4,c=6)
# b. with a=2 b=4 c=6 > d =2


# 6.
import random

rand = random.randint(1, 100)


# 7.

def half(value):
    return value / 2.0


# result= half(number)

# 8. result= cube(4)

# 9.

def times_ten(num):
    return num * 10


# 10.

def get_first_name():
    name = input("Enter first name: ")
    return name
