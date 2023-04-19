#  Program 9, counting vowels and consonants
# Nhan Nguyen
def main():
    vowel = 0
    consonant = 0
    your_string = input('Enter a string: ')
    vowel = vowel_count(your_string)
    consonant = consonant_count(your_string)
    print(' Your string contains', vowel, 'vowels and', consonant, 'consonants.')


def vowel_count(string):
    counter = 0
    vowels = 'aeiou'

    for character in string:
        if vowels.find(character) <= 0:
            counter += 1
    return counter


def consonant_count(string):
    counter = 0
    consonant = 'qwrtypsdfghjklzxcvbnm'

    for character in string:
        if consonant.find(character) <= 0:
            counter += 1
    return counter


if __name__ == '__main__':
    main()
