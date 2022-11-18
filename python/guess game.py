"""guess game constructor"""
#guess = int(input("Enter a number"))
secret_number = 142
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False
        
while guess != secret_number and not (out_of_guesses):
    if guess_count < guess_limit:
        guess_count += 1
        guess = int(input("Enter a number"))
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Try again, you lose")
else:
    print("Well done, You won!!!")


