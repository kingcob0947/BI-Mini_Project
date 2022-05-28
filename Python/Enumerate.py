###Without enumerate function you can enumerate:-
# name = ["pravin", "harshit", "anand"]
# position = 0
# for names in name:
#     print(f"{position}----> {names}")
#     position  +=1

## with enumerate function we can enumerate:-
# name = ["pravin", "harshit", "anand"]
# for position, name in enumerate(name):
#     print(f"{position}----> {name}")

## define a function that take two arguments. list containing string and that want to find in your list.and this function
# will return the index of string in your list and if string is not present then return -1.
# names =["pravin", "harshit", "anand"]
# def my_function(l, s):
#     for pos, name in enumerate(l):
#         if name ==s:
#             return pos
#     return -1
# print(my_function(names, "pravin"))

name = ["pravin","harshit", "anand"]
def my_function(li, st):
    for pos, names in enumerate(li):
        if names == st:
            return pos
    return -1
print(my_function(name, "unknown"))