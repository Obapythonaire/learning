# program to get username from user
# should contain alphanumeric,
# pass username to function as parameter to display the username
# name = input("Enter a username:")
# def check_name_alnum():
#     # check = name.isalnum()
        
#     if (name.isalnum()):
#         print(f"{name} is Alphanumeric")
#     else:
#         print(f"{name} is not Alphanumeric")
# # print(f"{check}")

# check_name_alnum()

# ASSIGNMENT
# program to get username from user
# should contain alphanumeric, and 
# not less than or equal to 8

name = input("Enter your username: ")

if (name.isalnum()) and (len(name)>=8):
    print(f"{name} is Alphanumeric and long enough")
else:
    print(f"{name} is not Alphanumeric and not long enough")