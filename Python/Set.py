## Create sets:-
# thisset = {"ram", "mohan", "laxman"}
# print(thisset)

##Duplicate not allowd:-
thisset = {"ram", "mohan", "laxman", "ram"}
print(thisset)

##Get the length of set:-
# thisset = {"ram", "mohan", "laxman", "ram"}
# print(len(thisset))

## SET constructure:-
# thisset = set(("apple", "mango"))
# print(thisset)

##Remove duplicate elelment:-
# num = {1,2,3,43,54,3,8,5,6,4,33,5,6,7,88}
# li = list(num)
# num = set(li)
# print(num)

##Add items:-
# fruits = {"apple", "mango"}
# fruits.add("orange")
# print(fruits)

##Add sets:-
# fruits = {"apple", "kiwi"}
# color = {"red", "black"}
# fruits.update(color)
# print(fruits)

# ## add any iterable:-
# fruits = {"apple", "kiwi"}
# color = ["red", "black"]
# fruits.update(color)
# print(fruits)

##remove items:-
# fruits = {"apple", "kiwi"}
# color = ["red", "black"]
# fruits.update(color)
# fruits.pop()
# print(fruits)

##remove item using remove and discard:-
# fruits = {"apple", "kiwi"}
# color = ["red", "black"]
# fruits.update(color)
# fruits.remove("kiwi")
# print(fruits)
    ## OR ##
# fruits = {"apple", "kiwi"}
# color = ["red", "black"]
# fruits.update(color)
# fruits.discard("kiwi")
# print(fruits)

##Del method:-
# fruits = {"apple", "kiwi"}
# color = ["red", "black"]
# fruits.update(color)
# del fruits
# print(fruits)

##loop setin set:-
# fruits = {"apple", "kiwi"}
# for i in fruits:
#     print(i)
#     ##or##
# fruits = {"apple", "kiwi"}
# if "kiwi" in fruits:
#     print("Yes, kiwi in fruits")
# else:
#     print("no, kiwi in not present in fruits")

##Combine two set(union):-
# s1 = {1,2,3,4,5}
# s2 = {6,7,8,9,0}
# union_set = s1| s2
# print(union_set)

##intersection:-
s1 = {1,2,3,4,5}
s2 = {5,4,1}
s1 & s2
print(s1 & s2)
