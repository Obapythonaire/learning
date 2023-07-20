# Program to get students identities and check duplications and remove
# if any

# std_id = []
# no_of_stds = int(input("Enter the number of students id you need: "))

# new_std_id =[]

# for i in range(no_of_stds):
#     id = int(input("Enter the Student ID: "))
#     std_id.append(id)

# for j in std_id:
#     # print(new_std_id)
#     if j not in new_std_id:
#         new_std_id.append(j)
#         # print(new_std_id)
#     # else:
#     #     continue    

# print(f" The student id with duplicates is {std_id} and with the duplicates removed is: {new_std_id}")


# ASS
# Program to get students identities and check duplications and remove
# if any with system helping to prevent adding duplicate item

std_id = []
no_of_stds = int(input("Enter the number of students id you need: "))

new_std_id =[]

for i in range(no_of_stds):
    id = int(input("Enter the Student ID: "))
    std_id.append(id)
    for j in std_id:
        # print(new_std_id)
        if j not in std_id:
            pass
            # new_std_id.append(j)
            # print(new_std_id)
        else:
            print(f"There's a student with {id} ID, Please enter a new ID.")    

print(f" The student IDs are: {std_id}")