# Program to accept six students ID no
# and display in ascending order
# std_id = []
# for i in range(0,6):
#     id_num = int(input("Enter the student ID: "))
#     std_id.append(id_num)

#     std_id_sorted = sorted(std_id, reverse=True)

# print(f"The student id's are: {std_id} while in descending order are {std_id_sorted}")

# ASSIGNMENT
# Program to accept six students ID no
# and clear the list and use tghe empty method to check if its truely empty.

std_id = []
num = int(input("Enter the number of students data you need: "))
for i in range(0, num+1):
    id_num = int(input("Enter the student ID: "))
    std_id.append(id_num)

for j in range(num+1):
    std_id.pop()
    print(std_id)

if len(std_id) == 0:
    print(f"The list {std_id} is empty ")
else:
    print(f"The list {std_id} is not empty ")