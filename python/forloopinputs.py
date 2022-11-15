""" Program to prompt user for input 
n times using for loop
and getting the sum """
a = 0

for i in range(1, 6):
    i= int(input(f"Enter number {i}: "))
    a+=i

print(a)