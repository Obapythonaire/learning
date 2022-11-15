# from difflib import SequenceMatcher
# from distutils.errors import LinkError
# import numbers


# program to generate 10 numbers,
# find their square and cube and 
# add the squrae and cube with the output Like
# numbers Square cube addition
# 1           1   1   2
# 2           4   8   12
# 3           9   27  36

# num = []
# print(f"Numbers Square Cube Addition")

# for i in range(1, 11):
#     # num.append(int(input(f"Enter number {i}: ")))

    
#     # for k in i:
#     square_n = i**2
#     cube_n = i**3
#     add = square_n + cube_n
    
#     print(f"{i} \t {square_n} \t {cube_n} \t {add}")
    
# ASS
# program to generate 10 numbers,
# find their square and cube and 
# add the squrae and cube with the output Like
# numbers Square cube addition IN DESC ORDER

print(f"Numbers Square Cube Addition")

for i in reversed(range(1, 11, 2)):
    # num.append(int(input(f"Enter number {i}: ")))

    
    # for k in i:
    square_n = i**2
    cube_n = i**3
    add = square_n + cube_n
    
    print(f"{i} \t {square_n} \t {cube_n} \t {add}")