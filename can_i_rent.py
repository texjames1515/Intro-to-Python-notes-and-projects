def main():
    print('enter your age and I will tell you if you can rent a car.')
    age = int(input('enter your age: '))
    print('you can rent: ' + str(age >= 25))
    a = 25
    if age >= 25 : # if the boolean value is True then the if statement will run if False it will skip
        print('You can rent a car.')
    elif a == 25 :    # you can use elif to make a other branching paths in a code 
        print('test')
    else :  # if any of the if or elif statements aren't returned true the else will run
        print('you are not old enough to rent a car.') 
    
    print('Thanks for visting Python rental agency')



main()