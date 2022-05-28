## print the Square value with the help of set comprehension range between 1 to 10.:
set1 = {k**2 for k in range(1, 11)}
print(set1)

## print the first charactor of name with the help of set comprehension:-
name = {'harshit', 'vathistha', 'shrivastav'}
first_char ={names[0] for names in name}
print(first_char)