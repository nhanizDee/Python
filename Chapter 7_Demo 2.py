# Program 6
def main():
    num = int(input('Enter a num: '))
    num_list = [35, 71, 68, 76, 80, 45, 77, 91, 15]
    print('Num: ', num)
    print('List of num: \n', num_list, sep = '')
    print('List of num greater than ', num, ':', sep='')
    display_greater_than_n_list(num, num_list)


def display_greater_than_n_list(n, n_list):
    greater_than_n_list = []
    for val in n_list:
        if val > n:
            greater_than_n_list.append(val)

    print(greater_than_n_list)


main()
