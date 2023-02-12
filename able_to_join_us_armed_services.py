#not flips the bool value

MIN_AGE = 17        #constant is denoted in all caps, not a hard rule but a format preferance
MAX_AGE = 35

def main():
    print('enter your age to see if you are able to join the armed services')
    age = int(input('enter your age: '))
    under_age = age >= MIN_AGE   #if false they are under age
    old = age <= MAX_AGE         #if false they are too old
    if under_age and old :
        print('you are in the age range to join the armed services')
        proper_age = True
    elif under_age == False and age > 0:
        year = MIN_AGE - age
        print('you are too young to join the armed services')
        if year != 1:
            print('wait ' + str(year) + ' years till you can join.')
        else:
            print('you can join next year')
        proper_age = False
    elif old == False :
        year = age - MAX_AGE
        print('you are too old to join the armed services')
        if year == 1:
            print('you should have joined last year')
        else:
            print('you should have joined ' + str(year) + ' years ago')
        proper_age = False
    else:
        print('invalid age')
        proper_age = False
    
#       medical_condition = bool(input('if you have a prior medical condition enter False if not enter True: '))
#        if medical_condition :
#            print('you have no medical blocks')
#        elif medical_wavier :
#            print('you have no medical blocks')
#        
#        else:
#            print('you have a medical block you need to get a waiver if you want to join')
#    elif not proper_age:
#        print()



main()