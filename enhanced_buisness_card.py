def user_imput () :
    '''gets user first and last name and email address'''
    first_name = input('enter your first name: ')
    last_name = input('enter your last name: ')
    email_address = input('enter your email address: ')
    print_buisness_card(first_name,last_name,email_address)



def print_buisness_card(first_name,last_name,email_address) :
    name = first_name + ' ' + last_name
    print(name)
    print(email_address)
    print(university)
    print(serc)
    print(address)
    print(city_state_zip)

university = 'Temple University'
serc = 'SERC Building'
address = '1925 North 12th Street'
city_state_zip = 'Philadelphia PA 19122'



user_imput()

