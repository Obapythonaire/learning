# program to get high and low numbers
# and display the numbers from highest to
# lowest.

# high_num = int(input("Enter a number: "))
# low_num =  int(input(f"Enter a number lower than {high_num}: "))

# for num in reversed(range(low_num, high_num+1)):
#     print(num, end=', ')
# print()

#ASS
# program to get high and low numbers
# and display the numbers from highest to
# lowest.
print("Program to display numbers in a range and their sum")
high_num = int(input("Enter the biggest number: "))
low_num =  int(input(f"Enter a number lower than {high_num}: "))
add=0
for num in reversed(range(low_num, high_num+1)):
    add= add + num
    print(num, end=', ') 
print()
print(f'The sum of the numbers is: {add}')