##Create a list and print the square, range between 1 to 10:-
#Without Comprehension:-
# square = []
# for i in range(1, 11):
#     square.append(i**2)
# print(square)
# ##with list comprehension:-
# square = [i**2 for i in range(1, 11)]
# print(square)

## Create a list and print negative number range 1 to 10:-
# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)
# ##or with list comprehension:-
# negative_number = [-i for i in range (1, 11)]
# print(negative_number)

##print first charactor of the list:-
# name = ["Pravin", "ram", "meera"]
# first_char = []
# for names in name:
#     first_char.append(names[0])
# print(first_char)
##OR with list comprehension:-
# name = ["Pravin", "ram", "meera"]
# first_char = [names[0] for names in name]
# print(first_char)

##define a function that take a list of string. list containing reverse of every striing:-
# def my_function(s):
#     reversed_word = []
#     for i in s:
#         reversed_word.append(i[::-1])
#     return reversed_word
# word = ("pravin", "abhishek", "avinash")
# print(my_function(word))
## OR with list comprehension:-
# def my_function(s):
#     return [word [::-1] for word in s]
# print(my_function(["pravin", "abhishek", "avinash"]))



#######LiSt CoPrEhEnSiOn WiTh IF ELSE StAtEmEnT########
#print the even numver in between 1 to 20:-
# even = []
# for i in range(1, 21):
#     if i%2 == 0:
#         even.append(i)
# print(even)
##With Comprehension:-
# number = [1,2,3,4,5,6,7,8,9,76,43]
# even_num = [i for i in number if i%2 ==0]
# print(even_num)
                #OR#
# even_number = [i for i in range(1, 11) if i%2 ==0]
# print(even_number)

##print odd even number with list comprehension:-
# even_number = [i for i in range(1, 21) if i%2 ==0]
# print(even_number)
# odd_number = [i for i in range(1, 21) if i%2 != 0]
# print(odd_number)

## define a function that return string in different different data type:-
# def my_function(s):
#     return [str(i) for i in s if (type(i) ==int or type(i) ==float)]
# print(my_function([True, False,[1,2,3],1,1.0,3]))



############List comp4rehension with if else statement##########
##print the odd in negative and even of multiply number:-
# list = [1,2,3,4,55,5,5,4,3,5,5,6,78,8]
# even = []
# for i in list:
#     if i%2 ==0:
#         even.append(i*2)
#     else:
#         even.append(-i)
# print(even)
#    ###OR###
# new_list =[]
# for i in range(1, 11):
#     if i%2 == 0:
#       new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)
##With list comprehension:-
# new_list = [i*2 if (i%2 ==0) else -i for i in range(1,11)]
# print(new_list)



####### list comprehension in nested loop#######
##print the list 4 times range between 1 to 10.
# nested_loop = []
# for i in range(4):
#     nested_loop.append([1,2,3,4,5,6,7,8,9,10])
# print(nested_loop)
# #######or with list comprehension######
# new_nested = [[i for i in range(1, 11) for j in range(5)]]
# print(new_nested)




