""" strange_no = 1998
guess = "  "
guess_count = 0
guess_limit = 2
out_of_guess = False
while guess != strange_no and not out_of_guess:
    if guess_count < guess_limit:
        guess = int(input("Please Make Your Guess       "))
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("OOPS!!! you are out of luck")
else:
    print(f"You won, you guessed right, the secret number is {strange_no} ")"""

""" num1 = 8.2
num2  = 15
print(num1 + num2) """
""" num1 = float(input("Please enter a number  "))
num2 = float(input("Please enter a number  "))
sum = num1 + num2
print(f" The sum of the two digits is: {sum} ") """

""" num  = float(input("Please enter a number"))
square_root = num ** (1/2)
print (f" The square root of {num} is: {square_root}") """


""" import cmath

#num = 1 + 2k
num1  = eval(input("Please enter a number"))
num_sqrt = cmath.sqrt(num1)
print(num_sqrt)
 """

""" Understanding Iterators """
""" my_list = [1,2,3,4]
iterator = iter(my_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) """


"""
A code to convert temperature from Celsius to Fahrenheit
Given that, 1C = 33.8 Fahrenheit
"""
""" while True:
    degrees_celsius = float(input("Enter the temp. in (C) "))
    fahrenheit = ((degrees_celsius /5)*(9)) + 32
    print (f" {degrees_celsius}C is {fahrenheit}F") """

"""
Code to check if a number is positive, negative or zero
"""
""" count = 0
while True:
    num = int(input("Please enter a number!"))
    count+= 1
    if num > 0:
        print(f"The number {num} is greater than 0")
    elif num < 0:
        print(f"The number {num} is less than 0")
    elif num == 0:
        print(f"The number {num} is equal t0 0")
    elif count == 3:
        break """
""""
Code tp determine if a number is an odd or even number
"""
num = float(input("Please enter a number"))
if num % 2 == 0:
    print(f'{num} is an even No')
else:
    print(f'{num} is an odd No')