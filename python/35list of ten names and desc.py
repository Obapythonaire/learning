#35: Get names of ten students in a list
# and output them in descending order

# count = 0
# names = []
# for i in range(3):
#     names.append(input('Enter name {i} '))
#     count += i

# print(names)

# names.reverse()

# rev =names[:-0]
# print(f"These are the names in reversed order {names} or {rev}")

# for j in names:
#     print(j)

#35: Get names of ten students in a list
# and output them in descending order
# with removing first and last name

std_name = []

for k in range(3):
    std_name.append(input("Enter a name: "))

print(std_name)

del std_name[0]
del std_name[1]
# rem_name = std_name.remove(1)


print(f"Popped student names are: {std_name}")