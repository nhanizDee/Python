# Nhan Nguyen\
# Programing 6
# Apr 19, 2023
def main():
    input_name = input('Enter name of the first file: ')
    file1 = open(input_name, 'r')
    text1 = file1.read()
    file1.close()
    world1 = text1.split()
    set1 = set(world1)

    input_name = input('Enter name of the second file: ')
    file2 = open(input_name, 'r')
    text2 = file2.read()
    file2.close()
    world2 = text2.split()
    set2 = set(world2)

    union = set1.union(set2)
    print('there are word union in both file: ')

    for item in union:
        print(item)
    print()

    intersection = set1.intersection(set2)
    print('there are word appear in both file: ')

    for item in intersection:
        print(item)
    print()

    difference1 = set1.difference(set2)
    print('there are word in set 1 that not in set 2: ')

    for item in difference1:
        print(item)
    print()

    difference2 = set2.difference(set1)
    print('there are word appear in only set 2: ')

    for item in difference2:
        print(item)
    print()

    sym_diff = set1.symmetric_difference(set2)  # item appear in either set but not both
    print('there are word union in only 1 file: ')

    for item in sym_diff:
        print(item)
    print()


main()
