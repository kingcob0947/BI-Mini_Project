#### create function
# def my_function():
#     return

##### Calling a function
# def my_function():
#     print("Hello Mr. india")
# my_function()

### Pass the number of argument
# def my_function(A,B):
#     return A*B
# print(my_function(6,8))
            ##OR store function in Variable#
# def my_function(A,B):
#     return A+B
# total=my_function(87,45)
# print(total)

# def my_function(first_name, last_name):
#   print(first_name + " " + last_name)
# my_function("Pravin", "Singh")

### Take input from user####
# def my_function (num1, num2):
#    return num1+num2
# first_num=int(input("enter your 1st number"))
# last_num=int(input("Enter your 2nd num"))
# print(my_function(first_num, last_num))

# def my_function(A,B):
#   return A+B
# first_name=input("enter your first name")
# last_name=input ("Enter your last name")
# print(my_function(first_name, last_name))

#take single parameter and calling function.
# def my_function(name):
#     return name[-3]
# user=input("enter your name")
# user_name=my_function(user)
# print(user_name)

## Find odd even number with if statement...
# def odd_even(num):
#     if num%2 ==0:
#         return"even"
#     else:
#         return "odd"
# print(odd_even(20))
# def odd_even(num):
#     if num % 2 == 0:
#         return "even"
#     return "odd"
# print(odd_even(21))

### Take input from user##########
# def odd_even(num):
#     if num%2 ==0:
#         return"even"
#     else:
#         return "odd"
# user=int(input("Enter your number"))
# print(odd_even(user))

## print even value in boolean with if else statement.
# def odd_even(num):
#     if num%2 ==0:
#         return True
#     else:
#         return False
# A=int(input("Enter your number"))
# print(odd_even(A))

### equalitity Check  in python###
# def even(num):
#     return num%2 == 0:
# print(even(20)

##show function without parameter###
# def my_function():
#     return "Good morning india"
# print(my_function())

### Define a function which takes two number as a input and return greater of two numbers##
# def grater (A, B):
#     if A > B:
#         return "A is grater than B:"
#     else:
#         return "B is grater than A:"
# u1 = int(input("Enter your first number:"))
# u2=int(input("Enter your second number:"))
# bigger=(grater(u1, u2))
# print(bigger)
       ###find grater value in 3 parameter######
# def grater (A, B, C):
#     if A > B and A > C:
#         return "A is grater than B and C:"
#     elif B > A and B > C:
#         return "B is grater than A and C:"
#     else:
#         return "C is grater than A and B:"
# u1 = int(input("Enter your first number:"))
# u2=int(input("Enter your second number:"))
# u3=int(input("Enter your third number"))
# print(grater(u1, u2, u3))

##### define palindrom  that one take one word in string as input and return true if it is palindrom else return false.
# def this_pelindrom (word):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False
# user = input("Enter your name:")
# print(this_pelindrom(user))

#####Default parameter...........
# def my_function (First_name, Last_name, Age = 26):
#   print(First_name)
#   print(Last_name)
#   print(Age)
# my_function("Pravin")

# def my_function():
#   print("Hello from a function")
# my_function

def my_func(lists):
    for i in lists:
        return i
my_list = [1,2,3,4,5,6]
print(my_func(my_list))
