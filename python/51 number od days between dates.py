# program to find number od days between two dates
# from datetime import datetime

# date_1 = (input("Enter the first date in this format(dd/mm/YY): "))
# date_2 = (input("Enter the second date in this format(dd/mm/YY): "))

# d1= datetime.strptime(date_1, "%d/%m/%Y")
# d2= datetime.strptime(date_2, "%d/%m/%Y")

# diff = d2 - d1

# print(f"There are {diff.days} days between {d1} and {d2}.")


# Assignment
# program to find number of hourss between two dates
from datetime import datetime

date_1 = (input("Enter the first date in this format(dd/mm/YY): "))
date_2 = (input("Enter the second date in this format(dd/mm/YY): "))

d1= datetime.strptime(date_1, "%d/%m/%Y")
d2= datetime.strptime(date_2, "%d/%m/%Y")

diff = (d2 - d1).days
hours = (diff)*24

print(f"There are {hours} hours between {d1} and {d2}.")