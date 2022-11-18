#accepting array input in exercise 21

import array as arr
""" To check if leap year or not """
""" year = int(input("Enter a year: "))

if year%4 == 0:
    print(f'{year} is a leap year')
elif year%100 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year') """

""" Prompt user to enter year 5 times and
check if leap year or not """

#a = []
s=0
year = arr.array('i', [] )
for i in range(1,6):
    year.append(int(input(f"Enter the {i} year: ")))
    s+= year
#print(year)
    if s%4 == 0:
        print(f'{year} is a leap year')
    elif s%100 == 0:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year') 