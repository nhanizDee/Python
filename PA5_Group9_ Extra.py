# Required: The attached file Random.txt contains a long list of random numbers,
# Write a program that opens the file,
# reads all the numbers from the file, and calculates the following:
# (a) The number of numbers in the file
def main():
    filename = "Random.txt"

    with open(filename, "r") as file:
        count = 0
        for line in file:
            for char in line:
                if char.isdigit():
                    count += 1

    print(f"The number of numbers in the file is {count}")


main()
