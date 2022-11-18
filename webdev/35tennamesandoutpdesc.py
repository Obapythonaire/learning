# Program to accept ten names from user
# and output them in descending order



# name = []

# for num in range(1, 11):
#     num = input("Enter a name: ")
#     name.append(num)
#     reversed_name = name[::-1]
    
# print(reversed_name)

# ASS
# Program to accept ten names from user
# and output them in reverse order, then remove 
# the first and the last name

student_name = []

for i in range(1, 11):
    i = (input("Enter name: "))
    student_name.append(i)
    #student_name.append(input("Enter name: "))
    student_name.reverse()
    

    rm_l = student_name.pop()

    #rm_1 = student_name.remove(1)
print(reversed)
print(rm_l)
#
# print(rm_1)