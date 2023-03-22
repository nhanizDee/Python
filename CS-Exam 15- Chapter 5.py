def main():
    sc1 = float(input("Enter the first test score: "))
    sc2 = float(input("Enter the second test score: "))
    sc3 = float(input("Enter the third test score: "))
    sc4 = float(input("Enter the fourth test score: "))
    sc5 = float(input("Enter the fifth test score: "))
    avg = calc_average(sc1, sc2, sc3, sc4, sc5)
    print("Score\t\tNumeric Grade\t\t\tLetter Grade ")
    print('_______________________________')
    print("score 1:\t\t\t", sc1, "\t\t\t", determine_grade(sc1))
    print("score 2:\t\t\t", sc2, "\t\t\t", determine_grade(sc2))
    print("score 3:\t\t\t", sc3, "\t\t\t", determine_grade(sc3))
    print("score 4:\t\t\t", sc4, "\t\t\t", determine_grade(sc4))
    print("score 5:\t\t\t", sc5, "\t\t\t", determine_grade(sc5))
    print('______________________________________________')
    print("Average Grade:\t\t", avg, "\t\t\t", determine_grade(avg))


def calc_average(s1, s2, s3, s4, s5):
    # each s is score of one test
    return (s1 + s2 + s3 + s4 + s5) / 5.0


def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


main()
