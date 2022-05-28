##without *args argument:-
# def my_function(a, b):
#     return a+b
# print(my_function(3,6))

## if we pass more than two arguments:-
# def my_function (a,b):
#     return a+b
# print(my_function(4,6,8))

## if we use *args and pass multiple arguments:-
# def my_function(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(my_function(4,5,37))

## *args with parameter:-
# def my_function (*args):
#     multiply = 2
#     for i in args:
#         multiply *= i
#     return multiply
# print(my_function(5,4,6))

##*args with normal parameters:-
# def my_function(num, *args):
#     multiply = 1
#     for i in args:
#         multiply *= i
#     return multiply
# print(my_function(1,2,3))

##if i dont pass any argument:-
# def my_function(*args):
#     multiply = 2
#     for i in args:
#         multiply *= i
#     return multiply
# print(my_function())

##if i dont pass any argument in normal parameter:-
# def my_function(num, *args):
#     multiply = 2
#     for i in args:
#         multiply *= i
#     return multiply
# print(my_function())

##if i pass two parameter with args:-
# def my_function(num,num1, *args):
#     multiply = 2
#     for i in args:
#         multiply *= i
#     return multiply
# print(my_function(1,2,3))

##if i dont pass the *args argument:-
# def my_function(num,num1, *args):
#     multiply = 2
#     for i in args:
#         multiply *= i
#     return multiply
# print(my_function(2,3))

##args as a argument:-
# def my_function( *args):
#     multiply = 1
#     print(args)
#     for i in args:
#         multiply *= i
#     return multiply
# nums = [1,2,3,4]
# print(my_function(nums))

##unpack the arguments:-
# def my_function( *args):
#     multiply = 1
#     print(args)
#     for i in args:
#         multiply *= i
#     return multiply
# nums = [1,2,3,4]
# print(my_function(*nums))

##define a function take input num, iterable containing number as args. if user didnot pass any args then give a
# user message "hey you did not pass any args"(use list comprehension):-
# def my_function(num, *args):
#     if args:
#         return [i**num for i in args]
#     else:
#         "Hey, you didn't pass any args"
# nums = [2,4,8,4]
# print(my_function(2, *nums))