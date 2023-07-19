# 69 python program to create file and write into it

# txt_file = open('./python/learn.txt', 'a')
# name = input("What's your name? ")
# age = int(input("How old are you? "))

# txt_file.write(name,)
# txt_file.write(str(f'{ age}' '\n'))

# txt_file.close()

# Ass
# program to read existing file, get two numbers from user and add
# to the file and display

ass_file = open('python/assfile.txt', 'a', encoding='utf-8')
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
ass_file.write(str(num_1,))
ass_file.write(str(f'{  num_2} \n'))

content = ass_file.read()
print(content)

ass_file.close()