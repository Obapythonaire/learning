""" Code testing for generator 1
def make_list (num):
    result = [ ]
    for i in range (num):
        result.append(i)
    return result
my_list = make_list(1000000)
print(my_list)
#print(list(range(1000000))) """

""" Miscellaneous Code testing for generator 1 """
""" for i in range(100):
    print(i) """

""" Code testing for generator 1 ex 2 """
""" def generator_function(num1):
    for i in range(num1):
        yield i
for item in generator_function(991):
    print(item) """

""" Code testing for generator 1 ex3 """
""" def generator_function(num):
    for i in range(num):
        yield i * 2
g = generator_function(50)
next(g)
#next(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g)) """

"""GENERATOR PERFORMANCE """
""" from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print (f'took {t2-t1}s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(1000):
        i*5
@performance
def long_time2():
    print('2')
    for i in list(range(100)):
        i * 5

long_time()
long_time2() """

''''Generator Performance exc 2'''

""" def gen_func(num):
    for i in range(num):
        yield i

for item in gen_func(50):
    print(item) """

"""     UNDER THE HOOD OF GENERATORS """
""" giving errors """
""" def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator*2))
        except: StopIteration:
            break

special_for([1,2,3]) """

"""     UNDER THE HOOD OF GENERATORS   EXC 2 """
""" class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __iter__(self):
        return self
    def __next__ (self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(0, 100)
for i in gen:
    print(i) """

""" EXERCISE ON FIBONACCI NUMBERS """
def fib (number):
    a = 0
    b = 1
    for i in range(number):
        yield b
        temp = a
        a = b
        b = temp + a
for x in fib(21):
        print(x)
