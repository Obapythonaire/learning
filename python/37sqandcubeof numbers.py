# Program to find the cube of a number

# Ass
# Get six number from user, find square of first three
# and cube of last three

# num = int(input("Enter a number: "))
# cube = num**3
# print(f"The cube of the number is: {cube}")


# Ass
num = []

sq_out=[]
cb_out=[]

for i in range(1,7):
    num.append(int(input(f"Enter number {i}: ")))
print(f'The numbers are {num}')
first_three = num[0:3]
last_three = num[3:6]

for j in first_three:
    sq = j**2
    sq_out.append(sq)
    # print(f"The square of {j} is: {sq}")
print(f'The square of the first three are: {sq_out}')
for k in last_three:
    cube = k**3
    cb_out.append(cube)
    # print(f"The cube of {k} is: {cube}")
print(f'The cube of the last three are: {cb_out}')



