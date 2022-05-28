##Define a function and pass two parameter:-
# def my_function(A, B):
#     return A+B
# print(my_function(4,5))

## if i pass more than 2 arguments in this function:-
# def my_function(*args):
#     total = 0
#     for num in args:
#          total +=num
#     return total
# print(my_function(4,5,6,8))

##multiply :-
# def my_function(*args):
#     multiply = 2
#     for m in args:
#         multiply *= m
#     return multiply
# print(my_function(2,4,8))

##*args with normal parameter:-
def my_function(num, *args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply
print(my_function(2,3,4,5))