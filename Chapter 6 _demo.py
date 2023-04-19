def main():
    line = ''
    counter = 0

    infile = open('names.txt', 'r')
    line = infile.readline()

    while line != '':
        counter += 1
        line = infile.readline()

    infile.close()
    print(counter, 'names were read from the file.')


main()
