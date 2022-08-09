#prompt a user to enter password and check if password is alphanumeric
"""
name = input("What is your name? ")
password = (input("Enter your password: "))
pass_length = len(password)
#print(pass_length)

#pass_alph =  password.isalnum()

if pass_length >=8 and password.isalnum ()== True:
    password_secure = "*" * pass_length
    print(f'Hello {name}, your password is: {password_secure} and it is {pass_length} characters long and secure ')
else:
    print("Check your password and ensure it contains a letter, number and up to 8 characters")

#print(pass_alph)

"""
""" def pass_check():
    name = input("What is your name? ")
    password = (input("Enter your password: "))
    pass_length = len(password)

    pass_alph =  password.isalnum()

    if pass_length >=8 and (password.isalnum() == True):
        password_secure = "*" * pass_length
        print(f'Hello {name}, your password is: {password_secure} and it is {pass_length} characters long and secure ')
    else:
        print("Check your password and ensure it contains a character, number and up to 8 characters")

pass_check()
pass_check()
pass_check() """

#Third case, password must contain special character (@#*_-\/!'"$~)

name = input("What is your name? ")
password = (input("Enter your password: "))
pass_length = len(password)
spec_char = "(@#*_-\/!'\"$~)"
val = True
#[ "@", "#", "*", "_", "-", "\", "/", "!", "'", "\", "\"", "$", "~", ")", "]" ]
#for i in spec_char and password:
    #for spec_char in password:
    #print(i)
#break
#print(pass_length)

#pass_alph =  password.isalnum()

    
if (char in spec_char for char in password == True) and pass_length >=8 and password.isalnum ()== True:
    password_secure = "*" * pass_length
    print(f'Hello {name}, your password is: {password_secure} and it is {pass_length} characters long and secure ')
else:
    print("Check your password and ensure it contains a letter, number and up to 8 characters")