# Team Member:
# Cochise Nava
# Max Raven
# Nhan Nguyen
#  Date: Apr 5, 2023
# Program 5: Reading and working on file

# Required: The attached file Random.txt contains a long list of random numbers,
# Write a program that opens the file,
# reads all the numbers from the file, and calculates the following:
# (a) The number of numbers in the file
# (b) The largest and the smallest number
# (c) The sum of all the numbers in the file
# (d) The average of all the numbers in
# the file Write Functions and Lists for parts (a) through (d). Do not use the built-in functions in Python.
def main():
    # Open the file for reading
    file = open("Random.txt", "r")

    # Read the contents of the file into a string
    contents = file.read()

    # Split the string by whitespace to obtain a list of numbers
    numbers_as_strings = []
    current_number = ""
    for char in contents:
        if char == " " or char == "\n":
            if current_number != "":
                numbers_as_strings.append(current_number)
                current_number = ""
        else:
            current_number += char
    if current_number != "":
        numbers_as_strings.append(current_number)

    # Convert the list of strings to a list of integers
    numbers = []
    for number_as_string in numbers_as_strings:
        number = int(number_as_string)
        numbers.append(number)

    # count the numbers of element in a list
    def count_numbers(num_list):
        count = 0  # count total of number in file
        for _ in num_list:
            count += 1
        return count

    # find the largest element in a list
    def get_largest(num_list):
        largest = num_list[0]
        for n in num_list:  # n is a temporary number to use to make condition
            if n > largest:
                largest = n
        return largest

    # find the smallest element in a list
    def get_smallest(num_list):
        smallest = num_list[0]
        for n in num_list:
            if n < smallest:
                smallest = n
        return smallest

    # find the average of element in a list
    def get_average(num_list):
        sum_of_num = 0
        count = 0
        for n in num_list:
            sum_of_num += n
            count += 1
        return sum_of_num / count

    # Close the file
    file.close()

    # Print the list of numbers
    print(numbers)
    # printing the total numbers in a list
    print("The total numbers in the file: " + str(count_numbers(numbers)))
    # printing the largest element of a list
    print("The largest number from the file: " + str(get_largest(numbers)))
    # printing the smallest element of given list
    print("The smallest number from the file: " + str(get_smallest(numbers)))
    # printing the average of given list
    print("The average of all numbers in the file: " + str(get_average(numbers)))


main()
