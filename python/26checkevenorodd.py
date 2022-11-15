""" code to check if a 
number is even or odd """
"""
def check_even_odd(n):
    #n = float(input("Enter a number: "))
    if n%2 == 0:
        print(f'{n} is even')
    else:
        print(f'{n} is odd')
for i in range(1, 100+1):
    print(f"{check_even_odd(i)}")

check_even_odd(1)
check_even_odd(2)
check_even_odd(3)
check_even_odd(4)
check_even_odd(5) """

""" ASS
code to check if a 
number is even or odd and provide the square of the number """

def check_even_odd():
    n = int(input("Enter a number: "))
    for i in range(1, n+1):
        square = i*i
    #print(f"{(i)} and is square {square}")
        if i%2 == 0:
            print(f'{i} is even and is square {square}')
        else:
            print(f'{i} is odd and is square {square}')



check_even_odd()
""" check_even_odd(1)
check_even_odd(2)
check_even_odd(3)
check_even_odd(4)
check_even_odd(5)
square = n*n
if n%2 == 0:
    print(f'{n} is even and is square {square}')
else:
    print(f'{n} is odd and is square {square}')

for i in range(1, 100+1):
    print(f"{check_even_odd(i)} and is square {square}") """