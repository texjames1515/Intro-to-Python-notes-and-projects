#week 4 class notes
# import.math          #import comes before a function
days_in_a_week = 7   #constant (doesn't change) comes before a function

g = 4                #global variables are outside a function, minimize using them. 
                     #don't use them in this course.



def main():
    a = 10   #local variables are in a function
    b = 20
    do_things(a,b)
    True    
    False    #boolean value 
    lights_are_on = True
    object_is_recyclable = False     #boolean value can be stored in a variable 
    10 > 20     #returns boolean value False
    10 < 20     #returns boolean value True
    2 == 1      #checks for equality this returns False
    2 >= 1      #greather than or equal to returns True
    2 <= 1      #less than or equal to returns False
    2 != 1      #checks for inequality returns True
    print(a != b) #returns boolean value
    


    




def do_things(a,b):
    print(a + b)


main()

