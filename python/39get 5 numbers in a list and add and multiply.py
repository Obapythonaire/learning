# program to get 5 numbers in a list
# in a function, write a function to 
# add and multiply all of the numbers in the 
# list and display the results

# num =[]

# def add_mul():
#     for i in range(1,6):
#         num.append(int(input(f"Enter number {i}: ")))

#         add = 0
#         for k in num:
#             add+= k
        
#         mul = 1

#         for j in num:
#             mul*= j

#     print(f"The sum of the list is: {add}")
#     print(f"The multiple of the list is: {mul}")

# add_mul()

# program to get 5 numbers in a tuple
# in a function, write a function to 
# add and multiply all of the numbers in the 
# tuple and display the results

num = ()
lis_num = list(num)

def add_mul():
    for i in range(1,6):
        lis_num.append(int(input(f"Enter number {i}: ")))

        add = 0
        for k in lis_num:
            add+= k
        
        mul = 1

        for j in lis_num:
            mul*= j

    print(f"The sum of the list is: {add}")
    print(f"The multiple of the list is: {mul}")

add_mul()
