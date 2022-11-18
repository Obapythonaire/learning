"""
Finding factorial of a number
n = int(input("Please enter a number"))
factorial = 1
if n ==1:
    print("The factorial of 1 is 1")
elif n<=0:
    print("You can only find factorial of positive integers greater than 1")
else:
    for fact in range(1, n+1):
        factorial = factorial * fact
    print(f"The factorial of {n} is {factorial}")
"""
""""
#to build a multiplication table
num = int(input("Please enter the range of number from 1 to?"))
for i in range(1, num+1):
    for j in range(1, num+1):
        k = i*j
        print(k, end = " ")
    print()
"""
#Fibonacci Sequence
nth_term = int(input("Enter the number of terms you want: "))
count = 0
n1 = 0
n2 = 1
while count<(nth_term):
    print(n1)
    nth = n1 + n2
    n1 =n2
    n2 = nth
    count += 1
    