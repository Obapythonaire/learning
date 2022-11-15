""" accept number from user and 
find the square and cube """

import math

no = int(input("Enter a number: "))

square = math.pow(no, 2)
cube_no = math.pow(no, 3)

print(f"The square of {no} is {square} and it\'s cube is {cube_no}")
