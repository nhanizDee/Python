def main():
    num1 = 0   # local variable
    num2 = 0
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print("The maximum number is", maximum(number1, number2))


def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


main()
