##create a and print dictinaries:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# print(thisdicti)

## WAP duplicate not allowed, duplicate value will overwrite existing values:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Last_name" : "Sinha"
# }
# print(thisdicti)

##Print the number of items in the dictinaries:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# print(len(thisdicti))

##WAP that data type string, int, boolean and list data types:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Boolean" : "True",
#     "Id" : [4],
#     "DOB" : "06-01-1994"
# }
# print(thisdicti)

# ##Get the values of model key(Accessing items):-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# print(thisdicti["Middle_name"])
        ## OR ##
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# print(thisdicti.get("First_name"))

##Return a list of all the keys in the dictinariy(Key function):-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# print(thisdicti.keys())

##Return a list of all the values in the dictinariy(Key function):-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# print(thisdicti.values())

##Return a list of all the values in the dictinariy(Key function):-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# print(thisdicti.items())

##Check if "id" is present in thisdicti:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# if "Id" in thisdicti:
#     print("Yes, id is present in thisdicti")
# else:
#     print("No, id is not present in thisdicti")

## Change value in dictinary:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# thisdicti["Id"] = 5
# print(thisdicti)

##Update values in dictinary:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# thisdicti.update({"id" : 6})
# print(thisdicti)

##Add a itmem in dictinaries by using a new index key and assigned a value to it.
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
# }
# thisdicti ["year"] = 2021
# print(thisdicti.items())

##Removing item using pop method:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# thisdicti.pop("DOB")
# print(thisdicti)

##delete items using popitem:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# thisdicti.popitem()
# print(thisdicti)

##delete keyword removes the item with the specified key name:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# del thisdicti["Id"]
# print(thisdicti)
           ##OR##
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# del thisdicti()
# print(thisdicti)

##Empty the dictinary using clear method:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# thisdicti.clear()
# print(thisdicti)

##using for loop:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# for i in thisdicti:
#     print(thisdicti)

## print all values using for loop method:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# for i in thisdicti.values():
#     print(i)

##print all values using for loop method:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# for i in thisdicti.keys():
#     print(i)

##print the value with the help of keys:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# for i in thisdicti:
#     print(thisdicti(i))

##print the items in for loop:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# for keys, values in thisdicti.items():
#     print(thisdicti)

##Copy a dictinary:-
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# copydata = thisdicti.copy()
# print(copydata)
 ## OR ##
# thisdicti = {
#     "First_name" : "Pravin",
#     "Middle_name" : "Kumar",
#     "Last_name" : "Singh",
#     "Id" : 4,
#     "DOB" : "06-01-1994"
# }
# copy1 = dict(thisdicti)
# print(copy1)

## Fromekeys:-
# d = dict.fromkeys(["name", "age", "hight"], 'unknown')
# print(d)
#
# d = dict.fromkeys(range[1, 11], "unknown")

##Change the default output in if get not found true value.:-
# n = {
#     "name": "harshit",
#     "id": 4,
#     "age": 24,
# }
# print(n.get("age", "Not found"))

##define a function that take a number(n), and return a dictionary containing cube of number from 1 to 10.:-
# def my_func(n):
#   cube = {}
#   for i in range(1, n+1):
#     cube[i] = i**3
#   return cube
# print(my_func(10))

##Wordcounter:-
# def my_function(s):
#     count = {}
#     for char in s:
#         count[char]= s.count(char)
#         return count
# print(my_function("harshit"))

## Create a dictionary that contain three dictionaries(Use nested loop)

# family1 : {
#      "name": "harshit",
#      "id": 1,
#      "age": 20,
# }
#
# family2 : {
#      "name": "piyish",
#      "id": 2,
#      "age": 21,
# }
#
# family3 : {
#     "name": "meera",
#     "id": 3,
#     "age": 22,
# }
#
# my_family = {
#         "family1" : family1,
#         "family2" : family2,
#         "family3" : family3
# }
# print(my_family)

