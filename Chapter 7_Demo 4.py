# program 10
def main():
    team = ''
    count_winner = 0
    try:
        infile = open('WorldSeriesWinners.txt', 'r')
        winners = infile.readlines()
        for j in range(len(winners)):
            winners[j] = winners[j].rstrip('\n')
            team = input("Enter name of a team: ")
            if team not in winners:
                print('The', team, 'has never won the world series!')
            else:
                for i in winners:
                    if i == team:
                        count_winner += 1
                print('The', team, "won the world series", count_winner, 'times!')
    except IOError:
        print("File not found!")
    except IndexError:
        print('Index error!')
    except:
        print('Error!')


main()
