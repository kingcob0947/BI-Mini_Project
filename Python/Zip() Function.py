# This is first item in each passed iterator is paired togather then second.
# l1 = ["user1", "user2", "user3"]
# l2 = ["pravin", "harshit","anand"]
# zip(l1, l2)
# lis = list(zip(l1, l2))
# print(lis)

##Create a two new list in given itarable:-
# l = [(1,2),(3,4),(5,6),(7,8)]
# l1, l2 =list(zip(*l))
# print(list(l1))
# print(list(l2))

##print a new itarable in given list:-
# l1 = [1,3,5,7]
# l2 = [2,4,6,8]
# zip(l1, l2)
# l3 = zip(l1, l2)
# print(list(l3))

##you have two list and crate a new list and store in new list and find the garter element in l1 & l2.
# l1 = [1,3,5,7]
# l2 = [2,4,6,8]
# new_list = []
# for pair in zip(l1, l2):
#     new_list.append(max(pair))
# print(new_list)

##define a function take any number of lists containing any number,and return average:
# def my_function(l1, l2):
#     average = []
#     for pair in zip(l1, l2):
#         average.append(sum(pair)/len(pair))
#     return average
# print(my_function([1,2,3], [4,5,6]))
######if i pass multiple arguments in same function:-
# def my_function(*args):
#     average = []
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average
# print(my_function([1,2,3],[2,3,4],[5,6,7],[8,9,1]))

##Solve with the help of lambda expression:-
# average = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
# print(average([1,2,3],[2,3,4],[5,6,7],[8,9,1]))

#....
# l1 = [1,2,3,4]
# l2 = ["Harshit","Harry","anand","pravin"]
# for a,b in zip(l1, l2):
#       print(l1, l2)

#....
# a = [[1,2,3],[3,5,6],[5,5,3],[4,6,2]]
# print(a)
# print(zip(*a))
# for x in zip(*a):
#     print(x)

#....
# l1 = [1,3,5,7]
# l2 = [2,4,6,8]
# new_list =[]
# for c in zip(l1, l2):
#     new_list.append(max(c))
# print(new_list)

#.....
# l1 = [1,3,5,7]
# l2 = [2,4,6,8]
# zip(l1, l2)
# total = zip(l1,l2)
# print(list(total))

#........
def my_function(l1, l2):
    average = []
    for pair in zip(l1, l2):
        average.append(sum(pair)/len(pair))
        return average
print(my_function([1,2,3,4], [6,7,4,9]))