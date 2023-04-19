# Nhan Nguyen
# Apr 19, 2023
# Program 1: write a dictionary that have course number, name , and some more information
def main():
    rooms = {'CS101': 3004, 'CS103': 4501, 'CS103': 6755, 'NT110': 1244, 'CN241': 1411}
    instructors = {'CS101': 'Nhan', 'CS103': 'Nguyen', 'CS103': 'Map', 'NT110': 'Dit', 'CN241': 'Thoi'}
    time_at_school = {'CS101': '8 am', 'CS103': '9 am', 'CS103': '10 am', 'NT110': '1 pm', 'CN241': '3pm'}
    course = input('Enter a course number: ')

    if course not in rooms:
        print('Course is not available or invalid course number!')
    else:
        print('The following are the detail for', course)
        print('Room:', rooms[course])  # take the room by course given
        print('Professor: ', instructors[course])
        print('Meeting time: ', time_at_school[course])


main()
