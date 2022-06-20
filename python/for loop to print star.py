#use for loop to print
""" *
**
***
****
***** """

""" n = "*"
for i in range(0, 6):
    k= n*i
    print(k, end='\n')
print(' ') """


#ASS
#Align the text to right

from turtle import width

n = "*"
for i in range(0, 6):
    k= n*i
    width = 127
    m = k.rjust(width)
    print(m, end='\n')
print(' ')