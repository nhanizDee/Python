# Telephone Number, program 5
# Nhan Nguyen
# Apr 17, 2023
def main():
    digit_list = ['2', '3', '4', '5', '6', '7', '8', '9']
    alpha_ph_number = ''
    num_ph_number = ''

    alpha_ph_number = input('Enter the phone number as xxx-xxx-xxxx: ')
    for character in alpha_ph_number:
        if character.isalpha():
            character = character.upper()
            if character == 'A' or character == 'B' or character == 'C':
                index = 0
            elif character == 'D' or character == 'E' or character == 'F':
                index = 1
            elif character == 'G' or character == 'H' or character == 'I':
                index = 2
            elif character == 'J' or character == 'K' or character == 'L':
                index = 3
            elif character == 'M' or character == 'N' or character == 'O':
                index = 4
            elif character == 'P' or character == 'Q' or character == 'R' or character == 'S':
                index = 5
            elif character == 'T' or character == 'U' or character == 'V':
                index = 6
            elif character == 'W' or character == 'x' or character == 'Y' or character == 'Z':
                index = 7

            character = digit_list[index]
        num_ph_number += character
    print('Phone number is', num_ph_number)

if __name__ == '__main__':
    main()
