def main():
    print('enter a numeric day of the week 1-7')
    day = float(input('enter the day of the week: '))
    day = day // 1
    if day == 1:
        print('sun')
    elif day == 2:
        print('mon')
    elif day == 3:
        print('tue')
    elif day == 4:
        print('wed')
    elif day == 5:
        print('thurs')
    elif day == 6:
        print('fri')
    elif day == 7:
        print('sat')
    else:
        print('there are only 7 days in a week, please reload the program and enter a number between 1 - 7')

    print('Thanks for playing')


main()