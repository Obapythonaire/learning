# Program to accept and display student name, first name, admission no,
# age, and phone no.

# name = input("Enter your name: ")
# sur_name = input("Enter your surname: ")
# admission_no = str(input("Enter your admission no: "))
# age = int(input("How old are you?: "))
# phone_no = int(input("Enter your phone no: "))

# print(f"Name: \t\t {name}")
# print(f"Surname: \t\t {sur_name}")
# print(f"Admission No: \t\t {admission_no}")
# print(f"Age: \t\t {name} years")
# print(f"Phone No: \t\t {phone_no}")

# Assignment
# Program to accept and display student name, first name, admission no,
# age, and phone no., then update admission number, age, and phone no
name = input("Enter your name: ")
sur_name = input("Enter your surname: ")
admission_no =[str(input("Enter your admission no: "))]
# admission_no = str(input("Enter your admission no: "))
age = [int(input("How old are you?: "))]
phone_no = [int(input("Enter your phone no: "))]

print(f"Name: \t\t {name}")
print(f"Surname: \t\t {sur_name}")
print(f"Admission No: \t\t {admission_no}")
print(f"Age: \t\t {age} years")
print(f"Phone No: \t\t {phone_no}")

print("Clearing the files")
admission_no.clear()
age.clear()
phone_no.clear()
print("updating the files")

admission_no.append(str(input("Enter new admission no: ")))
age.append(int(input("Enter a new age: ")))
phone_no.append(int(input("Enter a new phone no: ")))

print(f"Name: \t\t {name}")
print(f"Surname: \t\t {sur_name}")
print(f"Admission No: \t\t {admission_no}[updated]")
print(f"Age: \t\t {age} years [updated]")
print(f"Phone No: \t\t {phone_no}[updated]")