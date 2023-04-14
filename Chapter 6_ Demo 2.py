# Chapter 6 demo number 2
# Program 6, 9 on book-related to each other

# program 6
def main():
    counter = 0
    num_in_file = 0.00  # can be float so jus to verify it
    total = 0

    infile = open('numbers.txt', 'r')  # r to read the file after open it
    # for loop to auto read the file
    for line in infile:
        counter += 1
        num_in_file = float(line)
        total += num_in_file
    infile.close()  # close the file

    average = total / counter

    print('Average of file is: ', average)


main()


# program 9 - modified program 6 to catch exception
def main():
    counter = 0
    num_in_file = 0.00  # can be float so jus to verify it
    total = 0

    try:
        infile = open('numbers.txt', 'r')  # r to read the file after open it
        # for loop to auto read the file
        for line in infile:
            counter += 1
            num_in_file = float(line)
            total += num_in_file
        infile.close()  # close the file

        average = total / counter

        print('Average of file is: ', total)
    except IOError:
        print('An error occurred while trying to read the file')
    except ValueError:
        print('Non numeric data occurred.')
    except:
        print('An error occurred')


main()
