##kwargs as a parameter:-
# def my_function(**kwargs):
#   print(kwargs)
# my_function(name= "harshit", age = 26)

##Pass loop in dictinaries:-
# def my_function(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(f"{k}:{v}")
# my_function(name = "harshit", age = 26)

## if i pass more one parameter in kwargs:-
# def my_function(names, **kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(f"{k}: {v}")
# my_function("mohit", name = "harshit", age = 26 )

##dictinaries unpacking:-
# def my_function(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(f"{k}:{v}")
# d = {'name' : 'pravin Singh', 'age': 26,}
# my_function(**d)

##function with all parameters:-
# def my_function(name, *args, age = 26, **kwargs):
#     print(name)
#     print(args)
#     print(age)
#     print(kwargs)
# my_function("paravin", 1,2,3, a=1, b=2)

##define a function print args in reversed:-

