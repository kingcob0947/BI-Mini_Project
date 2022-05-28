##sort the given list:-
fruits = ["apple", "mango", "orange", "kiwi"]
fruits.sort()
print(fruits)
#
# ##Sort the given list according to price:
cars = [
    {'model': 'Jaguaar',    'price': 20800000},
    {'model': 'rangerover', 'price': 10000000},
    {'model': 'Landrover',  'price': 16000000}
]
print(sorted(cars, key= lambda a: a['price']))
print(sorted(cars, key= lambda d: d.get('price')))

## Sorted the given dictinaries:-
student2 ={
    'Harshit':{'score':98, 'age': 25},
    'Anand'  :{'score':93, 'age': 64},
    'Teluska':{'score':95, 'age': 45},
}
print(sorted(student2, key= lambda d:student2[d] ['age']))
print(sorted(student2, key= lambda d:student2[d]['age'], reverse= True ))
### OR we can store in variable:-
sorted_student = sorted(student2, key= lambda d:student2[d]['age'])
print(sorted_student)