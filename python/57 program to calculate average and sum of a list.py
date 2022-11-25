# program to calculate average

# cont = []
# high_num = int(input("Enter the amount of number needed: "))

# for i in range(1, high_num+1):
#     if i == 1:
#         cont.append(int(input(f"Enter the {i}st number: ")))
#     elif i == 2:
#         cont.append(int(input(f"Enter the {i}nd number: ")))
#     elif i == 3:
#         cont.append(int(input(f"Enter the {i}rd number: ")))
#     elif i == 4:
#         cont.append(int(input(f"Enter the {i}th number: ")))
#     elif i == 5:
#         cont.append(int(input(f"Enter the {i}th number: ")))
#     else:
#         cont.append(int(input(f"Enter the {i}th number: ")))

# total = sum(cont)
# avg = total/len(cont)

# print(f" The list is {cont} with sum of {total} and average of {avg}")

# Assignment
# program to convert binary to decimal

binary = (input("Enter a number: "))
base = int(input("Enter the base: "))
conv = int(binary, base)

print(f"{binary} in decimal is {conv}")

# binary = (input("Enter a number: "))
# conv = int(binary, 10)

# print(f"{binary} in decimal is {conv}")