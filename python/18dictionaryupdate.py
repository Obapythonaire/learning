#A python program to store name, address and contact in alist and update the contact nbumber
""" name = {A, B, D,U, L, A, H, I}
address = {52, A, W, O, L, O, W, O}
contact = {0, 8,1,5,3,0,0,6,0,0}
contact.clear()
new_contact = {0, 8,0,5,3,4,0,6,3,1}
contact.extend(new_contact) 

user_details = {"name": "Abdulahi", "address": "GRA", "phone_no":8153009123}

#print(f"Hello Mr {name}, you live at {address} and your updated phone number is {contact}")
print(user_details)
user_details.update({"phone_no": 703244312})
print(user_details)
"""
#print(f"Hello Mr {user_details.name}, you live at {user_details.address} and your updated phone number is {user_details.phone_no}

#ASS
#A python program to store name, address and contact in alist and update the contact nbumber AT RUN TIME

name = input("Enter your name")
address = (input("Enter your addrress"))
phone_no = int(input("Enter your phone no"))

print(f'Hello {name}, you live at {address} and your phone number is {phone_no}')

#phone_no_update =phone_no.update()