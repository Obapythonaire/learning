""" A program to get the five numbers in an array and add """
import array as arr
a = arr.array('i', [])
s= 0

for i in range(0, 5):
    a.append(int(input("Enter the numbers of the array: ")))
    s+=a[i]
print(f' The sum of the {a} is: {s}')

#Algorithm 