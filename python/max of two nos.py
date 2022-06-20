#Get two numbers from user and determine max
#method 1
""" n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = max(n1, n2)
print(n3) """

#method 2
""" n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
 
if n1>n2:
    print(n1)
else:
    print(n2)  """

#Assignment
#Get three numbers from user and determine max
#method 1
""" n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
n4 = max(n1, n2, n3)
print(n4) """

#method 2

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

if n1>(n2 and n3):
    print(n1)
elif n2>(n1 and n3):
    print(n2)
else:
    print(n3)
