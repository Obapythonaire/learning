# program to find sum of two numbers, the nubers must
# be positive and less than 50

# num_1 = float(input("Enter a number: "))
# num_2 = float(input("Enter another number: "))

# if (num_1>= 1) and (num_2>=1) and (num_1<50) and (num_2<1):
#     result = num_1 + num_2
    
#     print(f"The sum of {num_1} and {num_2} is {result}")
# else:
#     print(f"One or both of the numbers is/are less than 1 or greater than 50")


# program to find sum of two numbers, 1st number positive, 2nd negative
# and less than 50 and greater than 20

num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))

if (num_1>= 1) and (num_2<1) and (num_1 and num_2<50) and (num_1 and num_2>20):
    result = num_1 + num_2
    
    print(f"The sum of {num_1} and {num_2} is {result}")
else:
    print(f"One or both of the numbers didn't meet the requirements")