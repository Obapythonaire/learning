# Program to create a list to pass into function as parameter
# and display the message in reverse order

# my_list = []
# # count = 0

# def list_it():
#     for item in range(5):
#         my_list.append(input("Enter a lenter: "))
#         rev_list = my_list[::-1]

#     print(my_list)
#     print(rev_list)

# list_it()

# Program to display prime numbers of a given number

num = int(input("Enter a number to get it's prime number: "))
prime_nos =[]

for i in range(1, num+1):
    for num in range(2, i):
        if (i%num) == 0:
            break
    else:
        prime_nos.append(i)

        print(f" i ={i} and num = {num}")
print(prime_nos)