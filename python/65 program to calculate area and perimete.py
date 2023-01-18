# program to calculate area and perimeter of a square

# side = int(input("Enter a side of the square: "))
# area = side*side
# per_sq = side*4

# print(f"A square with side {side} cm has Area of {area} centimeter square and perimeter of {per_sq} centimeter")

# program to calculate area and perimeter of a square, square root the area
# and perimeter and add then print all in a function
import math

def square_prop():
    side = int(input("Enter a side of the square: "))
    area = side*side
    per_sq = side*4

    root_area = math.pow(area, 2)
    root_per = math.pow(per_sq, 2)

    # print(root_area)
    # print(root_per)
    # list_sum = []
    # list_sum+= roo
    sum_both = root_area + root_per


    print(f"A square with side {side} cm has Area of {area} centimeter square and perimeter of {per_sq} centimeter, with square of area as {root_area} with square of perimeter {root_per} and their sum as {sum_both}")

square_prop()