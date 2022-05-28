# ##find the maximun charactor of string in given in given list:-
name = ["harshit", "anand", "teluska"]
def my_function(item):
    return len(item)
print(max(name, key = my_function))
#
# ##find the minimum charactor of string:-
name = ["harshit", "anand", "teluska"]
def my_function(item):
    return len(item)
print(min(name, key = my_function))

##With Lambda function:-
name = ["harshit", "anand", "teluska"]
print(max(name, key= lambda item: len(item)))

##Find the maximum number of score in given list:-
student =[
    {'name':'harshit', 'score':90, 'age':24},
    {'name':'anand',   'score':98, 'age':25},
    {'name':'Teluska', 'score':96, 'age':27}
]
print(max(student, key=lambda item: item.get('score')))
print(max(student, key=lambda item: item.get('score'))['name'])

## find the maximum age in given dictinaries:-
student2 ={
    'Harshit':{'score':98, 'age': 25},
    'Anand'  :{'score':93, 'age': 64},
    'Teluska':{'score':95, 'age': 45},
}
print(max(student2, key=lambda a:student2[a]['age']))
