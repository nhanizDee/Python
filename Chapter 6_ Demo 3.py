# Demo program 10 in book
# Golf Score
# Part 1
def main():
    # local variables
    num_of_players: int = 0  # type of value is int
    name = ''
    golf_score = 0

    num_of_players = int(input('Enter number of players: '))
    output_file = open('golf.txt', 'w')  # w to write value to a file

    # for loop to working in file
    for count in range(num_of_players):
        name = input('Enter the name of players: ')
        golf_score = int(input('Enter the score of each player: '))

        output_file.write(name + '\n')
        output_file.write(str(golf_score) + '\n')  # convert int to string to add to file

    output_file.close()


main()


# part 2
def main():
    # local variables
    num_of_players: int = 0  # type of value is int
    name = ''
    golf_score = 0
    line = ''

    infile = open('golf.txt', 'r')

    name = infile.readline()

    while name != '':
        golf_score = infile.readline()
        name = name.rstrip('\n')
        print('name:', name)
        print('Golf Score:', golf_score)
        name = infile.readline()
    infile.close()


main()
