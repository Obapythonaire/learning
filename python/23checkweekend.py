""" A program to check if a day is weekday or
weekend """
""" day = input('Enter a day: ')

if day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday':
    print(f'It\'s a weekday {day}')
elif day=='saturday' or day=='sunday':
    print(f'It\'s a weekend {day}')
else:
    print('Enter a valid day') """




""" ASS
Attemping to solve the problem of capital or small letters
in the above exercise """

day = input('Enter a day: ')
weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
weekend = ['saturday', 'sunday']
space = ' '
nwkday = space.join(weekday)
nwkday_upp = nwkday.upper()
nweekend = space.join(weekend)
nweekend_upp = nweekend.upper()
""" wkdays =''
for day in weekday:
    wkdays+= day
print(wkdays) """

for a in weekday or nwkday_upp:
    if a == day:
        print(f'Today {day} is a weekday. Get up and work.')
    else:
        #for b in weekend or nweekend_upp:
        print(f'{day}is a weekend, enjoy')

"""
if day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday':
    print(f'It\'s a weekday {day}')
elif day=='saturday' or day=='sunday':
    print(f'It\'s a weekend {day}')
else:
    print('Enter a valid day') """