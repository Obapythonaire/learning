""" 
Check alpha character then 
check wether vowel or consonant """

""" xter = input("Enter a character: ")

if xter =="a" or xter =="e" or xter =="i" or xter =="o" or xter =="u":
    print(f' The character {xter} is a vowel')
else:
    print(f' The character {xter} is a Consonant') """

""" ASS
Check alpha character then 
check wether vowel or consonant 
and also display it's a number if user input a number"""

xter = input("Enter a character: ")

if xter.isalpha():
    if xter =="a" or xter =="e" or xter =="i" or xter =="o" or xter =="u":
        print(f' The character {xter} is a vowel')
    else:
        print(f' The character {xter} is a Consonant')
else:
    print(f'You have entered a number: {xter}')