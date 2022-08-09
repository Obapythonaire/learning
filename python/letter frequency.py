#Code to print the % of a letter in another text
n = input('Enter text: ')
l = input('Enter a letter: ')
z = len(n)
#print(z)
count =0
for j in n:
    if j ==l:
        count +=1
        tot = int((count/z) * 100)
print(tot)