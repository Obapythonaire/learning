# program to count number of 
# character and word in bio of 
# a user AND SPECIFIC WORD.
# bio = input("Enter a brief descripttion of yourself: ")
# xter_count = len(bio)
# bio_split = bio.split()
# word_count = len(bio_split)


# print(f"There are {xter_count} letters and {word_count} words in {bio}.")


# program to count number of 
# character and word in bio of 
# a user.
bio = input("Enter a brief descripttion of yourself: ")
spec_word= input("Enter a brief descripttion of yourself: ")
xter_count = len(bio)
bio_split = bio.split()
spec_word_count = bio.count('you')
word_count = len(bio_split)


print(f"There are {xter_count} letters and {word_count} words in {bio}, and {spec_word} appeared {spec_word_count} times in it.")