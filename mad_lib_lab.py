import math
print('play this game of madlibs with me')   #introduction
animal = input('give me an animal: ')                
adjective = input('give me an adjective: ')
print('It took the ' + adjective + ' ' + animal)
place = input("give me a place(don't put 'the' in front): ")  #double quotes used because of the single quotes in 'don't' and around 'the'
first_number = float(input('give me a number: '))
second_number = float(input('give me another number: '))
third_number = float(input('give me your final number: '))


time = str(math.sqrt(first_number + second_number) + (third_number))
#based on the chicken crossing the road joke
final = 'It took the {1} {0} {2} seconds to cross the road to get to the {3}.'.format(animal,adjective,time,place)
print(final)