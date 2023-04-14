# Program 3
# Nhan Nguyen
# date: Apr 10, 2023
def main():
    # local variables
    total = 0
    average = 0
    highest = 0
    lowest = 0
    month_lowest = ''
    month_highest = ''

    # create list - monthly quantity of rain and list of month
    month_rain = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    month_of_year = ['jan', 'feb', 'mar', 'apr', 'thang5', 'june', 'july', 'aug', 'sep','oct', 'than11', 'dece']
    # or it can be month by word like January
    # making the loop
    for count in range(12):
        month_rain[count] = float(input("Rain fall amount for" + month_of_year[count]))

    total = sum(month_rain)
    average = total / 12  # can divide by the length of the month rain list

    # find the highest
    highest = max(month_rain)
    month_highest = month_rain.index(highest)

    # find the lowest month
    lowest = min(month_rain)
    month_lowest = month_rain.index(lowest)

    print("Total rainfall: ", format(total, '.2f'))
    print("Average rainfall: ", format(average, '.2f'))
    print("Highest month of the year: ", month_of_year[month_highest])
    print("Lowest month of the year: ", month_of_year[month_lowest])


main()
