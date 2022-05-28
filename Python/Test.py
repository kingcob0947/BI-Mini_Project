

# print('i \'am pravin singh')  # this is single escape \'.
# print("hello \"mr\" pravin singh")  # this is double escape".

# print('this python\nthis is python tutorial')  # this is new line escape \n.

# print('New \ttab')  # this is tab escape \t.

# print('this is backslash\\')  # this is backslash escape \\.
# print("this is double backslash\\\\")  # this is the double backslash escape\\\\.

# print("hell\blo")
# print('hello woo\brld')  # this is the backspace escape \b.

# print('hello \'mr pravin singh\'')  # this is single escape \'.

# print('\\\" \\\'')  # this is comment.

# print("this is \\\\ double backslash")  # This is escape sequence.

# print("these are /\\ /\\ /\\ /\\ mountains")  # this is Comment.

# print("he is\tawesome")  # Escape sequence.

# print("\\\" \\n \\t \\\'")  # escape sequence and escape sequence as normal text.

# print("this is \\\\ double backslash")
# print("these are /\\ /\\ /\\ /\\ mountain")
# print("\\\" \\n \\t \\\' ")
# name = "pravin singh"
# print(name[3:-3])

# a=int(input("Enter your marks"))
# b=int(input("Enter your marks"))
# c=int(input("Enter your marks"))
# d=int(input("Enter your marks"))
# e=int(input("Enter your marks"))
# total=a+b+c+d+e
# percent=(total/500)*100
# print(f"Total marks = {total}, percentage = {percent}")
# if percent>=80:
#     print('you have grade A')
# elif percent >= 60:
#     print("you have grade B")
# elif percent >= 40:
#     print("you have grade C")
# else:
#     print("you have grade D")

#  WAP print 10 to 1.
# n=10
# while (n>=1):
#     print(n)
#     n=n-1
# n=int(input("enter the value"))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+(i*i)
#     i=i+1
#     print("sum of even number is=", sum)

# total=0
# for i in range(1, 11):
#     total=total+i
#     print(total)

############
# user_input=int(input("Enter your number"))
# sum=0
# for i in range(1, user_input+1):
#     sum=sum+i
#     print(sum)

###################
#

# import random
# winning_number= random.randint(1, 50)
# guess = 0
# numbers=int(input("guess a number between 1 to 100:"))
# game_over = False
# while not game_over:
#     if numbers == winning_number:
#         print(f"you win and you guessed in {guess} times")
#         game_over=True
#     else:
#         if numbers < winning_number:
#             print("Too Low")
#         else:
#             print("Too High")
#         guess=guess+1
#         numbers=int(input("Try Again"))

# def my_function():
#     print("heloo from a function")
#
#     my_function()

###Calling a function
# def my_function():
#   print("Hello from a function")
#
# my_function()

## Argument in function###
# def my_function(fname):
#   print(fname + " Refsnes")
#
# my_function("Emil \nTobias \nLinus")

# def my_function(A, b):
#    return A*b
#
# print(my_function(5,8))

# def my_function(first_name, last_name):
#  print(f" {first_name} {last_name}")
#
# my_function("Pravin", "Singh")

# def my_function(a,b):
#  return a+b
# print(my_function(7,8))

# def my_function(food):
#  for x in food:
#   print(x)
#
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)

# def tri_recursion(k):
#  if (k > 0):
#   result = k + tri_recursion(k - 1)
#   print(result)
#  else:
#   result = 0
#  return result
#
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# print(list1, list2, list3)

# fruits = ["Apple"]
# fruits.append("orange")
# fruits.insert(0, "mango")
# print(fruits)

# f1=["apple","mango"]
# f2=["cherry","grapes"]
# print(f1+f2)

# f1=["apple","mango"]
# f2=["cherry","grapes"]
# f1.append(f2)
# print(f1)
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)
#number = [1, 2, 3, 4, 5, 6, 7]
# number=(1,2,3,4,5)
# for i in number:
#     print(i)

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[0:6])
# print(thistuple)

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple present in this tuple")
# else:
#     print("Apple is not present in this tuple")

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# (green, *yellow, red, pink) = fruits
#
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#
# (green, *tropic, red) = fruits
#
# print(green)
# print(tropic)
# print(red)

# fruits = ("apple", "banana", "cherry")
#
# (green, yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])

# A=int(input("Enter your number"))
# if A%2 == 0:
#     print("This number is even")
# else:
#     print("this is odd number")

# def my_function(k):
#     square = []
#     for i in k:
#         square.append(i**2)
#     return square
# number = list(range(1,6))
# print(my_function(number))

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["year"])


# child1 = {
#     "name" : "Emil",
#     "year" : 2004
#   }
# child2 = {
#     "name" : "Tobias",
#     "year" : 2007
#   }
# child3 = {
#     "name" : "Linus",
#     "year" : 2011
#   }
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily)
#
# thisset = {"apple", "banana", "cherry", "apple"}
#
# print(thisset)
#
# i = [1,5,8,6,9,3,6,4,0,9,5]
# s = set(i)
# i = list(s)
# print(i)

# def my_func(n):
#   cube = {}
#   for i in range(1, n+1):
#     cube[i] = i**3
#   return cube
# print(my_func(10))

# name = ["pravin","mohit","shobhit"]
# new_name = [names[0] for names in name]
# print(new_name)

# def my_function(s):
#     reversed = []
#     for i in s:
#         reversed.append(i[::-1])
#     return reversed
# word = ["pravin","abhishek","avinash"]
# print(my_function(word))

# def my_function(s):
#     return [word[::-1] for word in s]
# print(my_function(["pravin","rohit"]))

# number = list(range(1,11))
# even_num = [i for i in range(1, 11) if i%2 ==0]
# print(even_num)
# odd_num = [i for i in range(1, 11) if i%2 !=0]
# print(odd_num)

# def my_function(l):
#     return [float(i) for i in l if(type(i) ==int or type(i) ==str)]
# print(my_function([True, False, [1,2,3], 1, 1.0, 3

# new_list = []
# for i in range(1, 11):
#     if i%2 ==0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)

# new_list = []
# for j in range(5):
#     new_list.append([1,2,3])
# print(new_list)

# new_list=[[i for i in range(1,5)] for j in range(4)]
# print(new_list)
# square_l = {f"square of {num} is" :num**2 for num in range (1, 11)}
# for k,v in square_l.items():
#     print(f"{k}:{v}")

# def my_function (*args):
#     multiply = 1
#     print(args)
#     for i in args:
#         multiply *= i
#     return multiply
# nums = [2,3,4]
# print(my_function(*nums))

# def my_function(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(f"{k}:{v}")
# my_function(name = "harshit Singh", age = 26)

# def my_function(name, **kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(f"{k}:{v}")
# my_function('mohit', naam='harshit', age= 26)

# def my_function(name, *args, age=26, **kwargs):
#     print(name)
#     print(args)
#     print(age)
#     print(kwargs)
# my_function("pravin singh", 1,2,3, a=1, b=2)
# even = lambda a : a%2 ==0
# print(even(3))

# lamda = lambda s : True if len(s) > 5 else False
# print(lamda("harshit"))

# name =["harshit", "mohit", "shobhit"]
# pos=0
# for i in name:
#     print(f"{pos}---->{i}")
#     pos = +1

# for pos, names in enumerate(name):
#     print(f"{pos}--->{names}")
# names =["harshit", "mohit", "shobhit"]
# def my_function(l, s):
#     for pos, name in enumerate(l):
#         if name ==s:
#             return pos
#     return -1
# print(my_function(names, "mohit"))

# number = [1,2,3,4]
# square = [i**2 for i in number]
# print(square)
# number = [4,6,8,4]
# map(lambda a: a**2, number)
# square = list(map(lambda a: a**2, number))
# print(square)

# numbers=[8,9,5,76,45,98,]
# def my_munction(a):
#     return a%2 ==0
# filter(my_munction, numbers)
# even = tuple(filter(my_munction, numbers))
# print(even)

# number=[8,9,5,76,45,98,]
# even=tuple(filter(lambda a:a%2 ==0, number))
# print(even)

#users1 = ["user1", "user2"]
# users2 = ["ram", "meera", "radha"]
# zip(users1, users2)
# print(list(zip(users1, users2)))

# exam=[(1,2),(3,4),(5,6),(7,8)]
# l1, l2 = list(zip(*exam))
# print(list(l1))
# print(list(l2))

# l1 =[1, 3, 5, 7]
# l2 =[2, 4, 6, 8]
# new_list = []
# for pair in zip(l1, l2):
#     new_list.append(min(pair))
# print(new_list)

# def my_function(*args):
#     average = []
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average
#
# print(my_function([1,2,3],[4,5,6],[7,8,9]))

# average =lambda *args :[sum(pair)/ len(pair) for pair in zip(*args)]
# print(average([1,4,5],[6,8,6],[8,9,6]))
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# number1 = [2,4,6,8,10]
# number2 = [1,4,6,7,24]
# even = []
# for i in number2:
#     even.append(i%2 ==0)
# print(even)

# name = ["pravin", "harshit", "anand"]
# def my_function(item):
#     return len(item)
# print(max(name, key = my_function))


# l = [(1,2),(3,4),(5,6),(7,8)]
# l1, l2 = list(zip(*l))
# print(list(l1))
# print(list(l2))

# l1 = [1,3,5,7]
# l2 = [2,4,6,8]
# l3 = list(zip(l1, l2))
# print(l3)

# user_id = ['user1', 'user2', 'user3']
# user_name = ['harshit', 'anand', 'teluska']
# zip(user_id, user_name)
# user = list(zip(user_id, user_name))
# print(user)

# l1 = [1,3,5,7]
# l2 = [2,4,6,8]
# new_list = []
# for pair in zip(l1, l2):
#     new_list.append(max(pair))
# print(new_list)

# def my_function(l1, l2):
#     average = []
#     for pair in zip(l1, l2):
#         average.append(sum(pair)/len(pair))
#     return average
# print(my_function([1,2,3],[4,5,6]))

# def my_function(*args):
#     average = []
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average
# print(my_function([1,2,3],[4,5,6],[7,8,9]))

# average = lambda *args:[sum(pair)/len(pair) for pair in zip (*args)]
# print(average([1,2,3],[4,5,6],[7,8,9]))

# number = [2,4,6,8,9]
# print(all([num%2 ==0 for num in number]))
#
# print(any([num%2 ==0 for num in number]))

# name = ["harshit", "pravin", "anand"]
# def my_function(item):
#     return len(item)
# print(max(name, key = my_function))

# def my_function():
#     print("hello india")
# a = my_function
# print(type(a))

# def outer_func(x):
#     def inner_func(n):
#         return n**x
#     return inner_func
# cube = outer_func(4)
# print(cube(5))

# def decorator_function(any_function):
#     def wrapper_function():
#         print("this is awesome function")
#         any_function()
#     return wrapper_function()
# @decorator_function
# def my_func():
#     print("this is my first function")
#
# def my_func1():
#     print("this is function 2")
# my_func1 = decorator_function(my_func1)
# my_func1()

# from functools import wraps
# def decorator_function_data(function):
#     @wraps(function)
#     def wrapper_function(*args, **kwargs):
#         print(f"you are calling {function.__name__}")
#         print(f"{function.__doc__}")
#         return function(*args, **kwargs)
#     return wrapper_function
# @decorator_function_data
# def my_func(a,b):
#     '''this function take two numbers as arguments and return thair sum'''
#     return a+b
# print(my_func(4,5))

# d
# import time
#
# t1 = time.time()
# square = (i**2 for i in range(10000000))
# t2 = time.time()
# print(t2-t1)

# class phone:
#     def make_call(self):
#         print("Making a call")
#     def playing_game(self):
#         print("I am playing a game")
#
# phone1 = phone()
# phone1.make_call()

# class car:
#
#     def set_name(self, name):
#         self.name = name
#     def set_cost(self, cost):
#         self.cost = cost
#     def show_name(self):
#         return self.name
#     def show_cost(self):
#         return self.cost
# Car1 = car()
# Car1.set_name("Jaguaar")
# Car1.set_cost(8000000)
# Car1.show_name()

# class Employee:
#     def __init__(self, name, age, gender, salary):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.salary = salary
#     def show_employee_details(self):
#         print("Name of Employee", self.name)
#         print("Age of employee", self.age)
#         print("Gender of Employee", self.gender)
#         print("Salary of employee", self.salary)
#
# emp = Employee("Harshit", 26, "M", 70000)
# emp.show_employee_details()

# class person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def full_details(self):
#         print('the name of person is', self.first_name)
#         print('last name of person is', self.last_name)
#         print('age of user is', self.age)
#
# p1 = person("pravin", "singh", 26)
# p1.full_details()

# class person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def full_details(self):
#         return f'{self.first_name}, {self.last_name}, {self.age}'
#
# p1 = person('harshiot', 'singh', 24)
# print(p1.full_details())

# class laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def percent_discount(self, num):
#         off_price = (num/100)* self.price
#         return self.price - off_price
#
#     def percent1_dis(self, num):
#         dis = (num/100)* self.price
#         print('the total discount is', self.price-dis)
#
# l1 = laptop('hp', 'ryzen5', 45000)
# print(l1.percent_discount(20))
# l1.percent1_dis(31)

# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self._price = price
#         self.complate_specification = f"{self.brand} {self.model} and {self._price}"
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#
# phone1 = phone("nokia", "6.1 plus", 12000)
# phone1._price = 10000
# print(phone1.make_a_call(8294728874))
# phone1.full_name()
# print(phone1.complate_specification)

# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self._price = price
#     def complate_specification(self):
#         return f"{self.brand} {self.model} and {self._price}"
#
# phone1 = phone("nokia", "6.1 plus", 12000)
# phone1._price = 10000
# print(phone1._price )
# print(phone1.complate_specification())

# class phone:
#     def __init__(self, branch, model, price):
#         self.branch = branch
#         self.model =  model
#         self._price = price
#
#     @property
#     def complete_specification(self):
#         return f"{self.branch} {self.model} {self._price}"
#
#     @property
#     def price(self):
#         return self._price
#
#     @price.setter
#     def price(self, new_price):
#         self._price = max(new_price, 0)
#
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")
#
# phone1 = phone("sony", "t2ultra", 24000)
# phone1.price = -25000
# print(phone1.price)
# print(phone1.make_a_call(8294728874))
# print(phone1.complete_specification)

# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self._price = price
#
#     @property
#     def full_details(self):
#         return f"{self.brand} {self.model} {self._price}"
#
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")
#
#     @property
#     def full_name(self):
#         return f"Full name of phone is {self.brand} {self.model}"
#
# phone1 = phone ("nokia", "6.1plus", 15000)
#
# class smartphone(phone):
#     def __init__(self, brand, model, price, ram, internal_memory):
#        super().__init__(brand, model, price)
#        self.ram = ram
#        self.internal_memory = internal_memory
#
# smartphone1 = smartphone("apple", "iphone6s", 49000, "4gb", "64gb")
#
# print(phone1.make_a_call(8294728874))
# print(smartphone1.make_a_call(9759254341))

# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self._price = price
#
#     @property
#     def full_datails(self):
#         return f"{self.brand} {self.model} and price is{self._price}"
#
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#
# class smartphone(phone):
#     def __init__(self, brand, model, price, ram):
#         super().__init__(brand, model, price)
#         self.ram = ram
#
#     def full_name(self):
#         return f"{self.brand} {self.model} and price is {self._price}"
#
# class flagship(smartphone):
#     def __init__(self, brand, model, price, ram, memory):
#         super().__init__(brand, model, price, ram)
#         self.memory = memory
#
# phone1 = phone("sony", "xperia", 24000)
# smart = smartphone("apple", "iphone", 40000, "4GB")
# flag = flagship("nokia", "6.1plus", 12000, "4GB", "128GB")
# print(issubclass(smartphone, phone))

# class A:
#
#     def class_a_method(self):
#         return 'i\'m just a class "A" method'
#     def hello(self):
#         return 'hello from class "A" method'
#
# class B:
#
#     def class_a_method(self):
#         return 'i\'m just a class "B" method'
#     def hello(self):
#         return 'hello from class "B" method'
#
# class C(A, B):
#     pass
# instance_c = C()
# print(instance_c.class_a_method())

# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_details(self):
#         return f"{self.brand} {self.model} and price is {self.price}"
#
#     def make_a_call(self, phone_number):
#         print(f" Calling {phone_number}...")
#
#     def __str__(self):
#         return f"{self.brand} {self.model} {self.price}"
#
#     def __repr__(self):
#         return f"phone(\"{self.brand}\", \"{self.model}\", {self.price}"
#
# phone1 = phone("sony", "xperia", 24000)
# # print(str(phone1))
# # print(repr(phone1))
# print(phone1.__repr__())
#
# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_details(self):
#         return f"{self.brand} {self.model} and price is {self.price}"
#
#     def make_a_call(self, phone_number):
#         print(f" Calling {phone_number}...")
#
#     def __str__(self):
#         return f"{self.brand} {self.model} {self.price}"
#
#     def __repr__(self):
#         return f"phone(\"{self.brand}\", \"{self.model}\", {self.price}"
#
#     def __add__(self, other):
#         return self.price + other.price


# while True:
#     try:
#         age = int(input("enter your age:"))
#         break
#     except ValueError:
#         print("Invalid input age")
#     except:
#         print("unexpected error")
#
# if age > 18:
#     print("you can play this game")
#
# else:
#     print("you can't play this game")

# while True:
#     try:
#         number = int(input('enter your number:'))
#     except ValueError:
#         print('plese type integer value !!')
#
#     except:
#         print('invalid number!!!')
#
#     else:
#         print(f'user input {number}')
#         break

# def divide(a,b):
#     try:
#       return a/b
#     except ZeroDivisionError as err:
#         print(err)
#     except TypeError as err:
#         print(err)
# print(divide(10,"0"))

# class NameTooShortError(ValueError):
#     pass
# def validate(name, number):
#     if len(name) < 8:
#         raise NameTooShortError("Name is Too short")
#
# username =input("Enter your name:")
# usernumber = int(input("Enter your number:"))
# validate(username, usernumber)
# print(f"Hello {username}")
# print(f"calling {usernumber}...")

# f = open("D:\\Notepad\My SQL.txt", "r")
# print(f.readline())

# # f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())

# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#
# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())

# f = open("demofile3.txt", "a")
# f.write("now the file has more contect")
# f.close()
#
# #open and read the file after the appending:
# f = open("demofile3.txt", "r")
# print(f.read())

# f = open('imp.csv', 'w')
# f.write("my name is pravin kumar")
# f.close()
# f = open('imp.csv', 'r')
# print(f.read())

# with open('imp.csv', 'w') as f:
#  f.write("i am a software engineer")
#  f.close()
# with open('imp.csv', 'r') as f:
#  print(f.read())

# if 5 > 2:
#     print("Five is greater than two!")

# import os
# # print(os.getcwd())
# #
# # os.mkdir('python')
# print(os.getcwd())
# os.chdir(r'D:')
# # print(os.getcwd())
# # print(os.listdir(r'E:\Pravin_singh'))
# os.makedirs('new/movie')


# import os
# print(os.getcwd())
# os.chdir(r'D:\Python 3.6.0')

# print("this is first program")
# student = 'sam'
# print(student)
# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE DATABASE mydatabase")

# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Master@123",
#   database="mydatabase"
# )
# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Master@123",
#   database="python_db"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host = "localhost",
#   user = "root",
#   password = "Master@123",
#   database = "python_db"
#   )
# mycur = mydb.cursor()
# sql = "DELETE FROM customers WHERE name = 'john'"

# val = [
#   ("john", "highway 21"),
#   ("devid", "newyork")
# ]
# mycur.execute(sql)
# mydb.commit()

# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Master@123",
#   database="python_db"
# )
#
# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val =[
#   ("Sandy", "Canada"),
#   ("Amy", "one way 98")
# ]
# mycursor.executemany(sql, val)
#
# mydb.commit()

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
#
# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

# names = []
# n = int(input("How many names you want to enter?"))
# for i in range(n):
#   print(i+1, "Enter name")
#   names.append(input())
# s = set(names)
# names = list(s)
# print(names)

# n=int(input("Enter your number:"))
#
# i = 2
# sum = 0
# while (i <= n):
#     sum = sum+i
#     i += 2
#     print(sum)

# ram = 90
# print("print is", ram)
# a = 90
# b = 5.6
# c = 5j
# print(a)
# print(b)
# print(c)
# print(type(a), type(b,), type(c))


'''age = int(input("Enter your age:"))
if age >18:
    print("Your are elligle for PAN card")

else:
    print("you are not elligble for PAN card")'''

# a = 1
# sum = 0
# while a < 3:
#       a += 1
#       sum += a
# print(sum)

# for x in "India":
#       if x == "a":
#             break
#       print(x)
# print("Successfull")

# li = ['aiohkhku', 'v', 'j', 'g']
# # li.append('d')
# # print(li)
# # print(len(li[0]))
# li[0] = "Jaguaar"
# print(li)

# a = 'pravin'
# print(a.replace('v', 'z'))

# def my_function(s,k,j):
#     return s*k*j
# print(my_function(4,6,1))

# def function(country):
#     print(f'i am from {country}')
# print(function("india"))

#....
# num1 = int(input("Enter your1st number:"))
# num2 = int(input("Enter your 2nd number:"))
# num3 = int(input("Enter your 3rd number:"))
#
# print(f"The total average number of {(int(num1) + int(num2) + int(num3)) / 3}")

#.......
# user_name = input("Enter your name:")
# reversed_name = user_name[-1::-1]
# print(f"your reversed name is{reversed_name}")

#....
# name = "my name is pravin singh"
# print(name.replace("my name", "i am"))
# print(name.find("am"))
# print(name.index("singh"))

#....

# winning_number = (80)
# guess = 1
# numbers=int(input("guess a number between 1 to 100:"))
# game_over = False
# while not game_over:
#     if numbers == winning_number:
#         print(f"you win and you guessed in {guess} times")
#         game_over=True
#     else:
#         if numbers < winning_number:
#             print("Too Low")
#         else:
#             print("Too High")
#         guess=guess+1
#         numbers=int(input("Try Again"))

# user_name = input("enter your name:")
# user_age = int(input("enter your age:"))
# if user_age >= 10 and (user_name [0] == "a" or user_name[0] == "A"):
#     print("You can wathch the coco movie")
#
# else:
#     print("You can not watch the coco movie")

#.......
# n = int(input("enter your number"))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(sum)

#.....
# def my_function(*args):
#    avrage = sum(args)/len(args)
#    print(avrage)
# my_function(10,20,30)

#.......
# x = 5
# s = "10"
# y= int("10")
# print(x+y)

#...
# class Test:
#     x=20*2
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#     def full_details(self):
#         print(f"the user name is {self.name} and user address is {self.address}")
# t1=Test("pravin", "patna")
# print(t1.full_details())

#......
# l1 = [12,54,87,23,3,1,8,98]
# l1.sort()
# print(l1)
# print(type(l1))

# l2 = [12,54,87,23,3,1,8,98]
# l3 = sorted(l2)
# print(l3)

#.....
# class mobile:
#     def __init__(self, price, model):
#         self.price = price
#         self.model = model
#
#     def __add__(self, other):
#         return self.price + other.price
#
# phone1 = mobile(48000, "iphone 6s")
# phone2 = mobile(2000, "lenovo")
# print(phone2 + phone1)

#.....
# def my_function(x,y):
#     return x+y
#
# def my_function(a,b):
#     return a*b
# print(my_function(4,7))
# print(my_function(6,7))

#......
# class mobile:
#     def __init__(self):
#         print("this is my first prograam")
#     def my_function(self):
#         return "i am  just a method"
#
# class mobile1:
#     def __init__(self):
#         print("this is my second prograam")
#     def my_function(self):
#         return "i am  just a method"
#
# class mobile2(mobile, mobile1):
#     pass
# mob = mobile2()
# print(mob.my_function())

#.....
# def myfunc():
#   x = 300
#   def myinnerfunc(a,b):
#     return a*b
#   print(myinnerfunc(2,4))
#
# print(myfunc())

#........
# l = [1,5,76,87,"ram", 2.5,"harshit",45,3,89]
# l2 = []
# for i in l:
#     if type(i)==str:
#         l2.append(i)
# print(l2)

#......
# s1 = "harshit"
# print(s1[::-1])

#.......
# class phone:
#     def __init__(self):
#         self.a = 5
#         self.b = 2
#     def multiply(self):
#         return 5*2
# phone1 = phone()
# print(phone1.multiply())

#......
# class phone:
#     def __init__(self):
#         self.a = 5
#     def multiply(self):
#         self.b = 2
#
# p1 = phone()
# p2 = phone()
# p1.multiply()
# p2.multiply()
# p1.c=12
# print(p1.__dict__)
# print(p2.__dict__)

#.....
# class student:
#     a = 4
#     def __init__(self):
#         self.x = 4
#         student.b = 6
#         y = 8
#
#     def my_function(self):
#         student.c = 3
#
#     @staticmethod
#     def hello():
#         student.d = 9
#
#     @classmethod
#     def clmethod(cls):
#         student.e = 4

#.......

# def revstr(mystr):
#     length = len(mystr)
#     for i in range(length - 1,-1,-1):
#         yield mystr[i]
#
# for char in revstr("MasterPrograming"):
#      print(char)

#......
# h = "harshit"
# har = iter(h)
# print(har.__next__())
# print(har.__next__())
# print(har.__next__())
# print(har.__next__())
# print(har.__next__())
# print(har.__next__())
# print(har.__next__())
# print(har.__next__())

#.........
# def even_genrater(n):
#     for num in range(2, n+1):
#         if num % 2 == 0:
#             yield (num)
# for num in even_genrater(20):
#     print(num)

#.......
# def even_genrater(n):
#     for num in range(2, n+1, 2):
#             yield (num)
# for num in even_genrater(20):
#     print(num)

#.........
# square = (i**2 for i in range(11))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))

#......
# square = (i**2 for i in range(11))
# print(square.__next__())
# print(square.__next__())
# print(square.__next__())
# print(square.__next__())

#..........
# def my_function(num):
#     if num % 2 ==0:
#         return True
#     else:
#         return False
# number = int(input("Enter your number:"))
# print(my_function(number))

#....
# def my_function(a,b):
#     return a/b
# print(my_function(2852, 4000))

#.............
# def linnear_search(arr, size, key):
#     flag = 0
#     for i in range (size):
#         if arr[i]==key:
#             flag = 1
#             pos = i+1
#             break
#     if flag==1:
#         print(f"Number found at: {pos} position")
#     else:
#             print("number not found")
#
# # __main()__
# size = int(input("Enter your size of the list:"))
# arr = []
# for i in range(size):
#     value = int(input("Enter your value:"))
#     arr.append(size)
# key = int(input("Enter number to search:"))
# linnear_search(arr,size,key)

#.....
# tup1 = (1, 'a', True)
# tup2 = (1,2,3)
# tup3 = tup2 + tup1
# print(tup3)

#....
# def my_function(name, id, age =24):
#     print(name)
#     print(id)
#     print(age)
#
# print(my_function("pravin kumar", 2))

#......
# l1 = [1,3,6,8]
# l2 = ['a,b,c,d']
# l3 = l1 + l2
# print(l3)

#.......
# a = {'cars': 'jaguaar', 'model': 'XE' }
# print(type(a))

#.....
# python = "This is an object oriented programming language"
# print(python.upper())

#.........
# a = {'cars': 'jaguaar', 'model': 'XE' }
# l1 = dict.keys(a)
# print(l1)

#......
# python = "This is an object oriented programming language"
# print(python.swapcase())
# print(python.capitalize())

#.......
# l1 = [1,3,6,8]
# l1.insert(2,5)
# print(l1)

#.......
# l1 = [1,3,4,4,6,8]
# l2 = set(l1)
# l1 = list(l2)
# print(l1)

#........
# new_nested = [[i for i in range(1, 11) for j in range(5)]]
# print(new_nested)
#
# #.......
# new_nest = []
# for i in range(4):
#     new_nest.append([1,2,3,4,5])
# print(new_nest)

#.....
# n = 10
# a = (str(n))
# print(type(a))

#.........
# n = int(input("Enter your number"))
# i = 1
# sum = 0
# while (i <= n):
#     sum = sum + i
#     i = i +1
# print(sum)

#.........
# li = [i for i in range(100)]
# print(li)

