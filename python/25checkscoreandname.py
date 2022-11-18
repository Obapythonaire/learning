""" A program to accept only student with
score greater than 40 admission and name must not be xyz """

score = float(input('Enter your score: '))
name = input('Enter your name: ')

if name !='xyz' and score>= 40:
    print(f'Hello {name}, congrats you scored {score} and promoted to next class')
elif name=='xyz':
    print("Report to the Principal's office immediately")
elif score<40:
    print(f'Hello {name}, you scored {score} and you are not promoted to next class. Study hard next time.')