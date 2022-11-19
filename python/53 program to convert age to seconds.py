# program to convert age to seconds

# age = int(input("How old are you?: "))
# age_in_seconds = age*365*24*60*60

# print(f"You are {age_in_seconds} seconds Old.")


# program to get age in Year from user
# convert age to seconds, minutes and hours
from datetime import date

year_of_birth = int(input("What year were you born?: "))
age = date.today().year - year_of_birth
age_in_seconds = age*365*24*60*60
age_in_minutes = age*365*24*60
age_in_hours = age*365*24

print(f"You are {age} years, {age_in_seconds} seconds, {age_in_hours} hours and {age_in_minutes} minutes Old.")