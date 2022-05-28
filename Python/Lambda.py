## add 10 to argument a, and return the result:-
# x = lambda a : a+10
# print(x(10))

##multiply arguments a with arguments b and return the result:-
# x = lambda a, b : a*b
# print(x(2,8))

##summarize arguments a, b and c and return the result:-
# x = lambda a, b, c : a+b+c
# print(x(6,4,68))

## Define a lambda function:-
#normal function:-
# def my_function (s):
#     if s%2 ==0:
#         return True
#     return False
# print(my_function(4))

# With lambda:-
# lamda = lambda a : a%2 ==0
# print(lamda(4))


## Print the last charactor of any string:-
# def my_function(s):
#     return s[-1]
# print(my_function("harshit"))

#with lambda:-
# lamda = lambda s : s [-1]
# print(lamda("pravin singh"))


##print the if the length of string is grater than 5 return True otherwise false.
def my_function(s):
    return len(s) > 5
print(my_function("pravin"))
#OR#

def my_function(s):
     if len(s) > 5:
         return True
     else:
         return False
#print(my_function("harshit"))
# in Lambda:-
lamda = lambda a : True if len(a) >5 else False
print(lamda("pravin"))

