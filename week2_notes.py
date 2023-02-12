#week 2 demos
#week 1 review
greeting = 'Hi' 
name = 'James' 
greeting_name = greeting + ', ' + name
print(greeting + ', ' + name)
print(greeting_name)
print('i\'m great at programming')

#numbers
1
10
3.141
a = 10
b = 20
10 + 10
10 - 5
10 * 3
10/5
print(10/5)  #notice how it gives a floating point number and not an integer
print(1/10)  #hard to represent in binary 
print(1/10 + 1/10 + 1/10)  #limitation of using binary rounding error
greeting = 'hello'
print(type(greeting))
print(type(1/10))
print(type(10/2)) #it gives a float and not an integer

10**2 #exponent

10 % 3 #modulo divides and spits out the remainder
1

3 % 10
3

-3 % 10
7

4 % 2 

4 % -1 #clock work arithmatic 

10 // 3 #floor division value if we truncate the decimal, always rounds down, 
#always leaves an integer
#ex:
print(10/3)
print(10 // 3)

print(10 + 3)
print(10 - 3)
print(10*3)
print(10/3)
print(10 ** 3)
print(10 % 3)
print(10 // 3)


print('now again with variables')
a = 10
b = 3

print(a + b)
print(a - b)
print(a*b)
print(a/b)
print(a ** b)
print(a % b)
print(a // b)

print('now calculate and assign')
c = 10 + 3
d = a + b
print(c)
print(d)

print((a - 3) * (10 + b) / 3)  # notice that the formula obeys order of operation including ()
# and uses the variables 


#strings allow for storage using concationation ex:

greeting = 'hell0'
name = 'james'
message = greeting + ', ' + name
print(message)

print(message + ' ' + message)


# how to update a variable 

a = 10 #assignment

print(a) # notice how it prints out 10, because the program runs sequentailly and doesn't know 
#           that a will be reassigned later 

a = 20 # reassignment

print(a) #notice it prints 20 instead of 10

# debugging tool: the step debugger stops and lets you look around  right click on # next to line to
#set a break point


a = a + 1 # takes the old value of a, adds 1, then updates variable a 
print(a)  # notice how it prints 21 (a + 1)

a = a - 2 
print(a)
a = a * 3
print(a)
a = a/5
print(a)

print('now do the same thing in a different way')
b = 20 
b += 1 #same as b = b+1
print(b)
b -= 2
print(b)
b *= 3
print(b)
b /= 5
print(b)


c = 10 
print(c + 20) # doesn't reassign c
print(c) # thats why this prints 10 not 30

# more complicated math

# have to tell python to include the library for more math

# go to python.com to find what is in each library

import math #should be at the start of the code
import random # need seperate lines for sepearate librarys  
from math import sqrt # may import certain functions from a library
root_2 = math.sqrt(2)
print(root_2)

print(math.pi) #use math. to call from math library
print(abs(-10))



#getting user input

greeting = 'hello'
name = 'jay'
print(greeting + ', ' + name)
name = input('enter your name: ')  # updates the name to the user input
print(greeting + ', ' + name)   # notice how it will print out the name you enter

# print('jay' + 10)  strong language: will not allow mixing of different data types
# except integer and float

print('hello' + str(10)) #type casting converts into a string
#print('1' + 10)

print(int('1') + 10)  # converts into an integer if the string could reasonably be considered an int
print(type('hello' + str(10)))
print(type(print(int('1') + 10)))


name = input('what is your name: ')
print('hello, ' + name)
age = int(input('how old are you?: '))  # stored as a string and coverts to int
next_age = age + 1
print('next year you will be ' + str(next_age) + ' years old!')