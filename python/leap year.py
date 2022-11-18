"""" EXERCISE 1
Code to check if a year is leap or not. 
NB: A leap year is divisible by 4, 400 
and 100 while a non leap year is not."""
"""while True:
    try:
        year = int(input("Please enter the year  "))
        if (year % 100 == 0) and (year % 400 == 0) and (year % 4 == 0):
            print(f" The year{year} is a leap year")
        else:
            print(f" The year {year} is not a leap year")
    except StopIteration:
        raise (' Enter a proper value')
    except ValueError:
        print (' Enter a proper value') """

""""  EXERCISE 2
Code to find the highest of three numbers"""
""" num_1 = float(input("Enter the first Number "))
num_2 = float(input("Enter the second Number "))
num_3 = float(input("Enter the third Number "))
highest_no = max(num_1, num_2, num_3)
print(f"The highest number between {num_1}, {num_2}, {num_3} is {highest_no}") """

"""" EXERCISE 3
Code to check if a number is Prime No or not.
A prime number has two factors; one and itself. """

""" while True:
    try:
        num = float(input("Enter a number to check if prime: "))
        if (num % num == 0) and (num % 2 != 0) and (num % 3 != 0)and (num % 4 != 0)and (num % 5 != 0):
            print(f" {num} is a Prime Number")
        else:
            print(f" {num} is not a Prime Number")
    except ValueError:
        print("Please enter a valid number") """

"""OR
from programiz but faulty as it doesn't capture all prime numbers"""
"""num = int(input("Enter a number to check if prime: "))
check = False
if num >1:
    for i in range(2, num):
        if (num % i == 0):
            check= True
            break
if check:
    print(" it is a prime no")
else:
    print("it is not a prime number")
"""

"""" EXERCISE 1
CODE TO PRINT OUT PRIME NUMBERS WITHIN A RANGE
"""
""" num = int(input("Enter a number to check if prime: "))
last_num = 0
for i in range (0, num):
    try:
        if (num % num == 0) and (num % 2 != 0) and (num % 3 != 0)and (num % 4 != 0)and (num % 5 != 0):
            print(f" [list{num}] is a Prime Number")
            if last_num == num:
                num -= 1
                print(f" [list{num}] is a Prime Number")
            else:
                print(f" {num} is not a Prime Number")
    except ValueError:
        print("Please enter a valid number") """

"""useful modules 1
"""
""" from collections import Counter, defaultdict, OrderedDict
from operator import countOf """

""" li = [1,2,3,4,5,6,6,7,6,6]
sentence = " I love Python very much"
print(Counter(li))
print(Counter(sentence)) """

""" dictionary = defaultdict(lambda: 5,{"a": 1, "b":2})
print(dictionary["z", "w"]) """

""" d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d) """

''' Useful modules one ends'''
''' Prime nos within a range of numbers'''
lower_num = 0
upper_num = int(input("Enter the number you want to find Prime Nos below"))
print(f" The Prime Nos between {lower_num} and {upper_num} are: ")
for num in range (lower_num, upper_num+1):
    if num > 1:
        for i in range(2, num):
            if (num %i == 0):
            #if (num % 2 == 0) or num % 3 == 0 or num % 4 == 0:
                break
            else:
                print(num)