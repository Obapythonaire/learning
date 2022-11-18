#To check word % in a document.

""" document = input("Enter the document text: ")
word = input("Enter the word you want to check: ")
doc_upper = document.upper()
word_upper = word.upper()
doc_dict = doc_upper.split()
doc_length = len(doc_dict)
word_count = doc_dict.count(word_upper)
word_percent = float(word_count/doc_length * 100)
word_perc = round(word_percent, 2)
print(f'There are {word_perc}% of "{word}" in the document.') """

# BMI Calculator

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Height = float(input("Enter your height in Meters(m): "))
Weight = float(input("Enter your weight in Kilogrammes: "))

BMI = Weight/(Height*Height)
BMI_app = round(BMI, 2)

#print(BMI_app)
if BMI_app <= 15.9:
    print(f"Hello {Name}, your Body mass Index is {BMI_app} and you are Underweight (Severe Thinness)")
elif BMI_app >=16.0 and BMI_app<= 16.9:
    print(f"Hello {Name}, your Body mass Index is {BMI_app} and you are Underweight (Moderate Thinness)")
elif BMI_app >=17.0 and BMI_app <= 18.4:
    print(f"Hello {Name}, your Body mass Index is {BMI_app} and you are Underweight (Mild Thinness)")
elif BMI_app >=18.5 and BMI_app <= 24.9:
    print(f"Hello {Name}, your Body mass Index is {BMI_app} and you are Normal")
elif BMI_app >=25.0 and BMI_app <= 29.9:
    print(f"Hello {Name}, your Body mass Index is {BMI_app} and you are  Overweight (Pre Obese)")
elif BMI_app >=30.0 and BMI_app <= 34.9:
    print(f"Hello {Name}, your Body mass Index is {BMI_app} and you are Obese (Class I)")
elif BMI_app >=35.0 and BMI_app <= 39.9:
    print(f"Hello {Name}, your Body mass Index is {BMI_app} and you are Obese (Class II)")
elif BMI_app >=40.0:
    print(f"Hello {Name}, your Body mass Index is {BMI_app} and you are Obese (Class III)")