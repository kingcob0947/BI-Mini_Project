##Create Tuple:-
# thistuple = ("Ram", "Mohan", "Bajrang", "Krishna")
# print(thistuple)

##To determine how many items a tuple has in this tuple(Len function):-
# thistuple = ("Ram", "Mohan", "Bajrang", "Krishna")
# print(len(thistuple))

##Type items can be of any data type:-
# string = ("A", "B", "C", "D", "E")
# int = (1,2,3)
# boolean = (True, False, False)
# print(string, int, boolean)

##type a tuple with string, int and boolean:-
# tuple = ("Krishna", 25, True)
# print(tuple)

## Use For loop in tuple:-
# tuple = ("Krishna", 25, True)
# for i in tuple:
#  print(i)

## Tuple with one element:-
# tuple = ("tuple",)
# print(type(tuple))
#     ##OR##
# tuple = ("tuple",)
# print(tuple)

##Tuple without parenthesis:-
# thistuple = "apple", "cherry", "kiwi", "cherry"
# print(thistuple)
# ###or###
# print(type(thistuple))

##Tuple unpacking:-
# thistuple = ("apple", "cherry", "kiwi")
# (red, green, yellow,) = thistuple
# print(red)
# print(green)
# print(yellow)

##Assign the rest of the values as a list called "red":-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# (green, yellow, *red) = fruits
#
# print(green)
# print(yellow)
# print(red)

##List inside tuple:-
# thistuple = ("harshit", "vashitha", ["john", "devid", "c"])
# print(thistuple)

##update in tuple using list method(add item):-
# thistuple = ("harshit", "vashitha", ["john", "devid", "c"])
# thistuple[2].append("michale")
# print(thistuple)

##update in tuple using list method(remove item):-
# thistuple = ("harshit", "vashitha", ["john", "devid", "c"])
# thistuple[2].pop(2)
# print(thistuple)

# ##Find the minimum value on the tuple(Min):-
# number = (1,4,87,56,64,98,)
# print(min(number))

##Find the minimum value on the tuple(Min):-
# number = (1,4,87,56,64,98,)
# print(max(number))

##sum the all value in the tuple(sum):-
# number = (1,4,87,56,64,98,)
# print(sum(number))

##create tuple in range, using range method:-
# number = tuple(range(1, 11))
# print(number)

##Change tuple to list:-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# fruits = list(("apple", "banana", "cherry", "strawberry", "raspberry"))
# print(fruits)

##Change tuple to string:-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# fruits = str(("apple", "banana", "cherry", "strawberry", "raspberry"))
# print(fruits)

##Print the second item in the tuple:-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# print(fruits[1])

####Print the negative indexing:-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# print(fruits[-1])

##Range of index:-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# print(fruits[0:3])

##By leaving out the start value, the range will start at the first item:-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# print(fruits[:4])

##range the negative index:-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# print(fruits[-3:-1])

##check if item exists, check if "apple" is present in the tuple:-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# if "apple" in fruits:
#     print("yes, apple is present in fruits")
# else:
#     print("Apple is not present in 'Fruits' ")

## change the tuple value:-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# f1 = list(fruits)
# f1[2] = "kiwi"
# fruits = tuple(f1)
# print(fruits)

##Add item in tuple:-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# f1 = list(fruits)
# f1.append("kiwi")
# fruits = tuple(f1)
# print(fruits)
#   ## or ##
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# f1 = list(fruits)
# f1.insert(1, "kiwi")
# fruits = tuple(f1)
# print(fruits)

##Add tuple to a tuple:-
# a1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
# b1 = ("mango", "kiwi")
# a1 += b1
# print(a1)

## Delete or remove in tuple:-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# f1 = list(fruits)
# f1.remove("cherry")
# fruits = tuple(f1)
# print(fruits)

##Loop with index number(For loop):-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# for i in range(len(fruits)):
#     print(fruits[i])

##Loop with index number(while loop):-
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# i=0
# while i < len(fruits):
#     print(fruits[i])
#     i=i+1

##Join two tuple:-
# a = (1,2,3)
# b = (4,5,6)
# C = a+b
# print(C)

##multiply two tuple:-
# a = (2)
# multiply = 2*2
# print(a)