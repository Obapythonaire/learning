""" Program to check if a number is positive
negative or zero """

no = float(input("Enter a number: "))

if no>0:
    print(f"{no} is a postive integer")
elif no<0:
    print(f"{no} is a negative integer")
elif no==0:
    print(f"{no} is zero")