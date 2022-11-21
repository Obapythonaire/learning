# program to get current date upon user request

from datetime import datetime

today = datetime.now()



ques = input("Enter Yes to see date or No: ")

def see_date(ans):
    if (ans=='Yes' or 'yes' or 'YES' or 'YEs'):
        print(f"Today\'s date is {today}")
    elif (ans=='no' or 'No' or 'NO'):
        print('No problem')
    else:
        print("Please enter yes or no")

see_date(ques)

# program to get current date to milliseconds upon user request
