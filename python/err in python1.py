""" while True:
    try:
        age = int(input('Whats your age?'))
        print(age)
    except:
        print('please enter a number')
    else:
        print('Thanks you')
        break """

def sum(num1, num2):
  try:
    return num1 + num2
  except:
    return ('something is wrong')
print(sum(1, 2))
