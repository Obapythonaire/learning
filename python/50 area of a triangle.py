# program to calculate area of a triangle
# base = float(input("Enter the value of base: "))
# height = float(input("Enter the value of height: "))

# Area = base*height/2

# print(f"A triangle with a base of {base} and height of {height} will have an area of {Area}")


# Assignment
# program to calculate area of a triangle, get another number
# from user, square the number, add tio area and display
import math


base = float(input("Enter the value of base: "))
height = float(input("Enter the value of height: "))
Area = base*height/2
num = float(input("Enter a number: "))
sq_num = math.pow(num, 2)
total = Area + sq_num

print(f"A triangle with a base of {base} and height of {height} will have an area of {Area} and the addition of square of {num} is {total}")