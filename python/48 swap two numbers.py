# program to get two numbers from user,
# swap and display the new result

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# x_bs = x
# y_bs = y
# temp = x
# x=y
# y = temp
# print(f"The values are {x_bs} and {y_bs} before swapping and {x} and {y} after swapping ")


# ASSIGNMENT
# program to get two numbers from user,
# swap and display the new result without creating
# the temp variable

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
x_bs = x
y_bs = y
x, y = y,x
print(f"The values are {x_bs} and {y_bs} before swapping and {x} and {y} after swapping ")