##Create a List:-
# name = ["pravin", "subham", "rohit", "ankit"]
# print(name)

## If access any name:-
# name = ["pravin", "subham", "rohit", "ankit"]
# print(name[1])

# print first two name:-
# name = ["pravin", "subham", "rohit", "ankit"]
# print(name[:2])

##Print Last name:-
# name = ["pravin", "subham", "rohit", "ankit"]
# print(name[-1])

##print the number of items in this list:-
# name = ["pravin", "subham", "rohit", "ankit"]
# print(len(name))

##change the items in list:-
# name = ["pravin", "subham", "rohit", "ankit"]
# name[1]= "shubham"
# print(name)

##number
# number=[1,2,3,4,5,]
# print(number)

##change number in list:-
# number=[1,2,3,4,5,]
# number[2]= "three"
# print(number)

##change number in list:-
# number=[1,2,3,4,5,]
# number[0:3]= "three"
# print(number)
## ORRR
# number=[1,2,3,4,5,]
# number[1:]= ["two", "three", "four", "five"]
# print(number)

##Add item in list(Append method):-
# number=[1,2,3,4,5,]
# number.append(6)
# print(number)
##OR
# number=[]
# number.append(1)
# number.append(2)
# print(number)

##Add item in list(insert  method):-
# number=[1,3,4,5,]
# number.insert(1, 2)
# print(number)

##concatenate of two number in list:-
# number1=[1,2,3,4,5,]
# number2=[6,7,8,9,10]
# number3=number1+number2
# print(number3)

##concatenate of two string in list:-
# name1 = ["pravin", "subham", "rohit", "ankit"]
# name2 = ["rishu", "divyansh", "mohit", "aaryan"]
# name = name1 + name2
# print(name)
####OR####
#name1 = ["pravin", "subham", "rohit", "ankit"]
# name2 = ["rishu", "divyansh", "mohit", "aaryan"]
# print(name1+name2)

##Add all the element of both list(extend method):-
# name1 = ["pravin", "subham", "rohit", "ankit"]
# name2 = ["rishu", "divyansh", "mohit", "aaryan"]
# name1.extend(name2)
# print(name1)

##store the list inside the list(Append method):-
# name1 = ["pravin", "subham", "rohit", "ankit"]
# name2 = ["rishu", "divyansh", "mohit", "aaryan"]
# name1.append(name2)
# print(name1)

##Delete the itmes in list(Pop method)(by default delete last item in the list):-
# name1 = ["pravin", "subham", "rohit", "ankit"]
# name1.pop()
# print(name1)
### or if you define the parameter##
# name1 = ["pravin", "subham", "rohit", "ankit"]
# name1.pop(1)
# print(name1)

####Delete the itmes in list(DEL method)(It is not delete any item by default, for delete need the define parameter):-
# name1 = ["pravin", "subham", "rohit", "ankit"]
# del name1[1]
# print(name1)

##delete the given object using remove method:-
# name1 = ["pravin", "subham", "rohit", "ankit"]
# name1.remove("subham")
# print(name1)

##IF find any item in the list:-
# name1 = ["pravin", "subham", "rohit", "ankit"]
# if "pravin" in name1:
#     print("True")
# else:
#     print("False")

##Find the number of name in the list(Count method):-
# name1 = ["pravin", "subham", "rohit", "ankit"]
# name1.count("rohit")
# print(name1.count("rohit"))

##WAP name in ascendind order(sort method):-
# name1 = ["pravin", "subham", "rohit", "ankit"]
# name1.sort()
# print(name1)

##Use of sorted method print in sort form:-
# name1 = ["pravin", "subham", "rohit", "ankit"]
# print(sorted(name1))

## Clear all the item in the list(Clear method):-
# name1 = ["pravin", "subham", "rohit", "ankit"]
# name1.clear()
# print(name1)

# def square_list(l):
#     square = []
#     for i in l:
#         square.append(i**2)
#     return square
# number = list(range(1, 11))
# print(square_list(number))

##Copy the list in new list(Copy method):-
# name = ["ram","meera","soumya"]
# newname = name.copy()
# print(newname)

##if the same item in both list its give output True or False(Compare method):-
# number1=[1,2,3,4,5]
# number2=[1,2,3,4,5]
# print(number1 == number2)

##Convert atring into list(.split method):-
# a1 = "ram", "24".split(",")
# print(a1)

##convert list into string(.Join method):-
# name=["harshit, 24"]
# print("," .join(name))

##loping in list(For loop):-
# fruits = ["apple", "mango", "orange", "cheery"]
# for i in fruits:
#     print(i)

##While loop:-
# fruits = ["apple", "mango", "orange", "cheery"]
# i = 0
# while i < len(fruits):
#     print(fruits(i))
#   i=i+1

## List in list:-
# word = [["a","b","c"],["e","f","g"],["h","i","j"]]
# print(word[1])

## How to data type:-
# word = [["a","b","c"],["e","f","g"],["h","i","j"]]
# print(type(word))

##generets list with range function:-
# number = list(range(1, 11))
# print(number)

##generet list and with range function and delete element using pop method and return the value:-
# number = list(range(1,11))
# popped_item = number.pop()
# print(popped_item)

##find the element where is executed(index method):-
# fruits = ["apple", "mango", "orange", "cheery"]
# print(fruits.index("orange"))

##Pass a function of list and print the negative value:-
# number = [1,2,3,4,5,6,78,9]
# def my_function(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative
# print(my_function(number))

## define a function, which will take list containing numbers as input and return list containing square of every element-
# def my_function(l):
#     square=[]
#     for i in l:
#         square.append(i**2)
#     return square
# number=list(range(1, 11))
# print(my_function(number))

##define a funtion which will take list as argument and this function will return a reversed list:-
# def reversed_list(l):
#     output=[]
#     return l [::-1]
# numbers=list(range(1, 11))
# print(reversed_list(numbers))
            ######OR######
# def reversed_list(l):
#     l.reversed()
#     return l
# number=[1,2,5,7,9,8]
# print(reversed_list(number))
        #####OR#####
# def my_function(f):
#     reversed_lis = []
#     for i in range(len(f)):
#         popped_item = f.pop()
#         reversed_lis.append(popped_item)
#     return reversed_lis
# number=list(range(1, 11))
# print(my_function(number))
         #####OR#####
# def my_function(l):
#     return l[::-1]
# number=list(range(1,11))
# print(my_function(number))

##define a function which will take list of words as argument and return list with reverse of every element in that list:-
# def my_function(f):
#     name = []
#     for i in f:
#         name.append(i[::-1])
#     return name
# word = ["Pravin", "Kumar", "Singh"]
# print(my_function(word))

## Extend method:-
# fruits = ["ram", "mohan", "john"]
# tuple = ("devid", "rocky")
# fruits.extend(tuple)
# print(tuple)

##Reversed Method:-
# fruits = ["ram", "mohan", "john"]
# fruits.reverse()
# print(fruits)

##reversed in descending order:-
# fruits = ["ram", "mohan", "john"]
# fruits.sort(reverse=True)
# print(fruits)

## Copy with list method:-
# fruits = ["ram", "mohan", "john"]
# newfruits =list(fruits)
# print(newfruits)

##Define function which takes two list as input and return a list, which contain comman element both file.
# def my_function(num1, num2,):
#     output = []
#     for i in num1:
#         if i in num2:
#
#             output.append(i)
#         return output
# n1=[1,2,3]
# n2=[1,2,4]
# print(my_function(n1, n2))

## define a function take a input one list and find the how much list inside the list.
def my_function(l1):
    count = 0
    for i in l1:
        if type(l1) ==list:
            count = +1
            return count
number = [[1,2,3],[4,5,6],[7,8,9]]
print(my_function(number))