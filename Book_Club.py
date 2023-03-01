#book club point
# write program ask user insert number of book buy in one month and give the point
#asking for insert number of book
#give the point by : number of book * point
number =0
points = 0


number= int(input('Enter the number of book purhase:'))

if number == 2:
    points = 5
elif number ==4:
    points = 15
elif number == 6:
    points = 30
elif number >= 8:
    points = 60
else: point =0
                
print("You have purchased", number, "book.")
print("You earned", points, "points")
