#A program to accept six numbers and display them in a list
""" nos = [1,2,3,4,5,6]
z = sum(nos)
print(z) """
""" list=[]
#list = [3, 4, 4, 5, 6, 7]
for i in range(6):
    list.append(int(input("Enter 6 numbers: ")))

print(f"This is the list: {list}") """

#A program to accept six numbers, display them in a list and sum them up.
list=[]
#list = [3, 4, 4, 5, 6, 7]
for i in range(6):
    list.append(int(input("Enter 6 numbers: ")))
    y = sum(list)
print(f"This is the list: {list} and its sum is: {y}")
#print(f"This is the list: {list}")

'''
#add = 0
for i in nos:
    add+= i 
print(add) 
'''

""" i = 0
while i<6:
    i = float(input("Enter six numbers you want to add: "))
    i+= 0
    print(i)
     """