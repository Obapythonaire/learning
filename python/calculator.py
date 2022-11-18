#calculator by the latest Pythonaire

def calculator (num1, op, num2):
    num1 = float(input("Enter a number"))
    op = input("Enter the sign")
    num2 = float(input("Enter another number"))
    if op == "+" :
        print (num1 + num2)
    elif op == "-" :
        print (num1 - num2)
    elif op == "/" :
        print (num1 / num2)
    elif op == "*" :
        print (num1 * num2)
    elif op == "**" :
        print (num1 ** num2)
    elif op == "%" :
        print (num1 % num2)
    else:
        print("Enter a valid operator")
calculator("num1", "op", "num2")	