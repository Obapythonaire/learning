# Program  to check student eligibility for
# schorlarship and amount to pay

# tuition = 91560
# boarding = 181000
# tot_fee = tuition + boarding

# score = float(input("Enter your total Score: "))

# if score == 1100:
#     print(f"You are granted FREE EDUCATION! This is as a result of your Stellar performance.")
# elif score >= 1000:
#     fee = (20/100)*tuition + boarding
#     print(f"You are to pay {fee} Because you scored {score} in the exam.")

# elif score >= 900:
#     fee = (40/100)*tuition + boarding
#     print(f"You are to pay {fee} Because you scored {score} in the exam.")

# elif score >= 800:
#     fee = (60/100)*tuition + boarding
#     print(f"You are to pay {fee} Because you scored {score} in the exam.")

# elif score >= 700:
#     fee = (70/100)*tuition + boarding
#     print(f"You are to pay {fee} Because you scored {score} in the exam.")

# else:
#     print(f"You are to pay {tot_fee} Because you scored {score} in the exam.")

# Program  to check student eligibility for
# schorlarship and amount to pay using a function

tuition = 91560
boarding = 181000
tot_fee = tuition + boarding



def scholarship():
    
    score = float(input("Enter your total Score: "))
    if score == 1100:
        print(f"You are granted FREE EDUCATION! This is as a result of your Stellar performance.")
    elif score >= 1000:
        fee = (20/100)*tuition + boarding
        print(f"You are to pay {fee} Because you scored {score} in the exam.")

    elif score >= 900:
        fee = (40/100)*tuition + boarding
        print(f"You are to pay {fee} Because you scored {score} in the exam.")

    elif score >= 800:
        fee = (60/100)*tuition + boarding
        print(f"You are to pay {fee} Because you scored {score} in the exam.")

    elif score >= 700:
        fee = (70/100)*tuition + boarding
        print(f"You are to pay {fee} Because you scored {score} in the exam.")

    else:
        print(f"You are to pay {tot_fee} Because you scored {score} in the exam.")

# scholarship(670)
# scholarship(1670)
# scholarship(870)
# scholarship(970)
# scholarship(770)
# scholarship(570)