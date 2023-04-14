# program 8:
# Nhan Nguyen
def main():
    try:
        boy_input = open('BoyNames.txt', 'r')
        # making list
        popular_boys = boy_input.readlines()

        for i in range(len(popular_boys)):
            popular_boys[i] = popular_boys[i].rstrip('\n')
        # do the same for girl
        girl_input = open('GirlNames.txt', 'r')
        popular_girls = girl_input.readlines()

        for i in range(len(popular_boys)):
            popular_girls[i] = popular_girls[i].rstrip('\n')

        boy = input("Enter a boy name's name or N if you do not wish to enter: ")
        girl = input("Enter a girl name's name or N if you do not wish to enter: ")

        if boy == "N":
            print('You choose to not enter boy name')
        elif boy in popular_boys:
            print(boy, 'is the most popular boy name.')
        else:
            print(boy, 'is not the most popular boy name.')

        if girl == "N":
            print('You choose to not enter girl name')
        elif girl in popular_girls:
            print(girl, 'is the most popular girl name.')
        else:
            print(girl, 'is not the most popular girl name.')

    except IOError:
        print('File can not be found!')
    except IndexError:
        print('Index error!')
    except:
        print('Error!')


main()
