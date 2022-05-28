## Pass functioon as a argument:-
# def square(a):
#     return a**2
# l = [1,2,3,4,5]
# def my_map(func, l):
#     new_list = []
#     for item in l:
#         new_list.append(func(item))
#     return new_list
# print(my_map(square, l))

## Function returning function:-
# def my_func(msg):
#     def inner_func():
#         print(f'message is {msg}')
#     return inner_func
# var = my_func('Hello Dear')
# var()

## Closour :-
# def my_func(x):
#     def inner_func(n):
#         return n**x
#     return  inner_func
# cube = my_func(3)
# print(cube(5))


## Define decorator and and inhance in other function:-
# def decorator_function(any_function):
#     def wrapper_function():
#         print("this is awesome function")
#         any_function()
#     return wrapper_function
#
# def my_func():
#     print("this is function 1")
# decorate = decorator_function(my_func)
# decorate()
#
# def my_func2():
#     print("this is function 2")
# decorate = decorator_function(my_func2)
# decorate()
            ##### OR #####
# def decorator_function(function):
#     def wrapper_function():
#         print('this is decorate by me')
#         function()
#     return wrapper_function
#
# @decorator_function
# def my_func():
#     print('this is func one')
# my_func()


## If we pass the argument in decorator function:-
# def decorator_function(function):
#     def wrapper_function(*args, **kwargs):
#         print('this is awesome')
#         function(*args, **kwargs)
#     return wrapper_function
#
# @decorator_function
#
# def my_func(a):
#     print(f'this function with {a} argument')
# (my_func(2))


## If decorate return the value:-
# def decorate_function(function):
#     def wrapper_function(*args, **kwargs):
#         print('this function return is')
#         return function(*args, **kwargs)
#     return wrapper_function
#
# @decorate_function
#
# def my_func(a,b):
#     return a*b
# print(my_func(6,5))


## Add the doc file and print docfile:-
# from functools import wraps
# def decorate_function(function):
#     @wraps(function)
#     def wrapper_function(*args, **kwargs):
#         '''This is wrapper function'''
#         print('this function created for define function')
#         return function(*args, **kwargs)
#     return wrapper_function
#
# @decorate_function
#
# def my_func(a,b,c):
#     '''this is my func'''
#     return a+b+c
# print(my_func(7,8,6))
# print(my_func.__name__)
# print(my_func.__doc__)

##define a decorate function that give output
#'you are calling add function', whis is take two argument # print doc(this function take two number as parameter and return their sum),
# return value 9
# from functools import wraps
# def function_data(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args, **kwargs):
#         print(f'you are calling {any_function.__name__} ')
#         print(f'{any_function.__doc__}')
#         return any_function(*args, **kwargs)
#     return wrapper_function
#
# @function_data
#
# def add_function(a, b):
#     '''this function take two number as parameter and return their sum'''
#     return a+b
# print(add_function(4, 5))

## Define a decorator and print int.
import time
from functools import wraps
# def only_int_allow(function):
#     @wraps(function)
#     def wrapper_function(*args, **kwargs):
#         data_types = []
#         for arg in args:
#             data_types.append(type(arg) ==int)
#             if all (data_types):
#                 return function(*args, **kwargs)
#             else:
#                 print("invalid argument")
#     return wrapper_function
#
# @only_int_allow
#
# def add_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(add_all(1,2,3,4,5))
#           ###### OR #####
# from functools import wraps
# def only_int_allow(function):
#     @wraps(function)
#     def wrapper_function(*args, **kwargs):
#         if all([type(arg) ==int for arg in args]):
#                 return function(*args, **kwargs)
#         else:
#                 print("invalid argument")
#     return wrapper_function
#
# @only_int_allow
#
# def add_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(add_all(1,2,3,4,5))

##
from functools import wraps
def calculate_time(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        print(f"executing ....{function.__name__}")
        t1 = time.time()
        returned_value = function(*args, **kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(f"this function took {total_time}")
        return returned_value
    return wrapper_function

@ calculate_time

def square_finder(n):
    return [i**2 for i in range(1, n+1)]
square_finder(1000)