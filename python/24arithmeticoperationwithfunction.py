from sqlite3 import OperationalError

""" 
A program to perform arithmetic Operation on
two numbers using a function """
a = float(input("Enter a number: ")) 
b = float(input("Enter a number: "))
op = input("Enter an operator sign e.g (*,+,-,**,%,/,//): ")
def maths(a, b, op):
    if op=="+":
        res = a+b
        print(res)
    elif op=="-":
        res = a-b
        print(res)
    elif op=="*":
        res = a*b
        print(res)
    elif op=="/":
        res = a/b
        print(res)
    elif op=="%":
        res = a%b
        print(res)
    elif op=="//":
        res = a//b
        print(res)
    elif op=="**":
        res = a**b
        print(res)
    else:
        print("Wrong input and not allowed")

maths(a,b, op)








""" 
A program to perform arithmetic Operation on
two numbers using a function and print out error 
message if user enter a digit or wrong character """