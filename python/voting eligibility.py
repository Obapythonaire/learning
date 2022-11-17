#Check voting eligility and if not till when

name = input("What\'s your name?  ")

year_of_birth = int(input("What year were you born? "))

age = 2022 -year_of_birth

# when = 18 - age

if age >= 18:
    print(f' Congratulations {name}, you are eligible to vote because you\'re {age} years old')
else:
    print(f'Sorry {name}, you\'re ineligible to vote because you\'re {age} years old, come back in {when} years time.')