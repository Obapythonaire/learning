#Program to accept six numbers in a list, display all numbers, clear the list and then display

""" 
Algorithms
1. declare a variable with an empty list
2. use a for loop with an append method to accept input and parse into the empty list
3. Display the updated list
4. use clear method to clear the list
6. display the cleared list
"""

lisst = []
for i in range(5):
    lisst.append(int(input("Enter a number and press enter for 5 times: ")))
x = lisst    
print(x)

lisst.clear()
y = lisst
print(y)
