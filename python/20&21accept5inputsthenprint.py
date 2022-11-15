""" accept five variables as inputs, 
store them and 
add them up. """
""" import array as arr


no = arr.array('i', [])

sum = 0
for i in range(5):
    no.append(int(input('Enter a number: ')))
    sum += i
print(no)
print(f' The sum of the {no} is: {sum}') """

""" ASS
Get five numbers fro the user,
store them and 
find the max and minimum number in them """

import array as fig

nums = fig.array('i', [])

for i in range(5):
    nums.append(int(input("Enter a number: ")))
    max_no = max(nums)
    min_no = min(nums)

print(f'The maximum number is: {max_no} and the minimum number is: {min_no}')
