#Non scientific calculator
import math

n1 = float(input("Enter the first number: "))

n2 = float(input("Enter the second number: "))

op = input("Enter the operator sign e.g(/,+,-,*,**, sqrt, cube: ")

#result = n1 op n2

if(op == '/'):
    res = n1/n2
    print(f' The result of {n1}{op}{n2} is: {res}')

elif(op == '+'):
    res = n1+n2
    print(f' The result of {n1}{op}{n2} is: {res}')

elif(op == '-'):
    res = n1-n2
    print(f' The result of {n1}{op}{n2} is: {res}')

elif(op == '*'):
    res = n1*n2
    print(f' The result of {n1}{op}{n2} is: {res}')

elif(op == '**'):
    res = n1**n2
    print(f' The result of {n1}{op}{n2} is: {res}')

#To calculate square root of a whole number, enter 1 as the second variable
elif(op == 'sqr'):
    res = n1**n2
    sqr = math.sqrt(res) 
    print(f' The result of {n1}{op}{n2} is: {sqr}')

#To calculate square root of a whole number, enter 1 as the second variable
elif(op == 'cube'):
    res = n1**n2
    cube = math.pow(res, 1/3) 
    print(f' The result of {n1}{op}{n2} is: {cube}')


""" 
#To calculate square root of a whole number, enter 1 as the second variable
elif(op == '**1/2'):
    res = (n1**n2)**(1/2)
    print(f' The result of {n1}{op}{n2} is: {res}')

#To calculate cube root of a whole number, enter 1 as the second variable
elif(op == '**1/3'):
    res = (n1**n2)**(1/3)
    print(f' The result of {n1}{op}{n2} is: {res}') 
"""


#To calculate square root of a whole number, enter 1 as the second variable
