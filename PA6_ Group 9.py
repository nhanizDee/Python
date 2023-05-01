# Nhan Nguyen
# Cochise Nava
# Max Raven
# Programing assignment 7 - chapter 9 on Pearson
# Date: Apr 24, 2023

#     """Reads the World Series winners file and returns two dictionaries: one mapping team names to number of wins,
#     and another mapping years to winning team names."""
#    Using the file that found on Pearson website instead of the file provided by professor Kulwant

def read_winners_file(filename):
    team_wins = {}  # create list for team who win
    year_winners = {}  # create list for year that a team win on that year
    with open(filename) as f:
        year = 1903  # start the first line as winner at year 1903
        for line in f:
            if line.strip() == "":
                continue
            if line.startswith('World Series not played in'):
                year += 1
                continue
            team = line.strip()
            if year == 1904 or year == 1994:  # condition to denied value of 1904 and 1944
                year += 1
                continue
            if team in team_wins:
                team_wins[team] += 1
            else:
                team_wins[team] = 1
            team_year = f"{team}"
            year_winners[year] = team_year
            year += 1
    return team_wins, year_winners
    # code above adding value of the year from 1903 to 2009 to the file
    # the year value was add to the end of each line so now value look like
    # team name     year win


def main():
    try:
        team_wins, year_winners = read_winners_file("WorldSeriesWinners.txt")
    except FileNotFoundError:
        print("Error: input file not found.")
        return
    while True:
        year = int(input("Enter a year between 1903 and 2009: "))
        if year not in year_winners:
            print(f"No World Series winner found for {year}.")
        else:
            winner = year_winners[year]
            team_name = winner.split(" (")[0]
            # find total win by key is the team name
            total_wins = sum(v for k, v in team_wins.items() if k.startswith(team_name))
            print(f"The {winner} won the World Series in {year}.")
            print(f"The {team_name} has won {total_wins} times from 1903 to 2009.")

        # re call the loop to make new search before user want to end the program
        user_input = input("Would you like to check another year? (y/n): ")
        if user_input.lower() != 'y':
            break


main()
