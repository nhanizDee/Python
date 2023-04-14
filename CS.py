def main():
    file = open('Random.txt', 'r')
    num1 = 0   # local variable
    num2 = 0
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print("The maximum number is", maximum(number1, number2))


    # Initialize a counter for the number of lines
    num_lines = 0

    # Iterate through each character in the file
    for char in file.read():
        # If the character is a newline character, increment the counter
        if char == '\n':
            num_lines += 1

    # If the file doesn't end with a newline character, increment the counter one last time
    if len(file.read()) > 0:
        num_lines += 1

    # Close the file
    file.close()

    # Print the number of lines in the file
    print(f"The file contains {num_lines} lines.")


def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


main()
