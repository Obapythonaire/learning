
# program to get student name
# and 5 marks in an array and total of the subjects
# and display.
# import array as arr

# name = input("Enter your name: ")
# marks = arr.array('i', [])
# # total = 0
# for score in range(6):
#     marks.append(int(input("Enter a number: ")))
#     # total+= marks
#     total = sum(marks)

# print(f"Hello {name}, your scores are {marks} and the total is {total}")


# program to get student name
# and 5 marks in an array and total of the subjects
# and display.
import array as arr

name = input("Enter your name: ")
marks = arr.array('i', [])
# total = 0
for score in range(6):
    marks.append(int(input("Enter a number: ")))
    # total+= marks
    total = sum(marks)
    average = total / len(marks)

print(f"Hello {name}, your scores are {marks} and the total is {total} with average of {average}")
