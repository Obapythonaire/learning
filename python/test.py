#Code to print the % of a string in another text
""" n = input('Enter text: ')
l = input('Enter a letter: ')
z = len(n)
#print(z)
count =0
for j in n:
    if j ==l:
        count +=1
        tot = int((count/z) * 100)
print(tot) """

""" doc = input("Enter the document: ")
word = input("Enter the word you want to check: ")

word_count = 0 """

""" data = [
    'name': phillip,
    'age': 15, 
    'nationality': Nigerian, 
    'religion': Christianity,
    ]
for values in data:
    print(values) """
sentence = 'abracadabra'
count = 0
vowels = 'a e i o u'
for char in sentence:
    for vowels in char:
        count+=1
    print(count, end =' ')