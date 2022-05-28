##print square of dictionary:-
# square_l = {num:num**2 for num in range(1, 11) }
# print(square_l)
#if we want print to print {'square of 1 is : 1}:-
# square = {f"square of {num} is": num**2 for num in range(1, 11)}
# print(square)

##if we want print in different line:-
square = {f"square of {num} is": num**2 for num in range(1, 5)}
for k, v in square.items():
 print(f"{k}:{v}")

##print the odd even value in dictinaries comprehension:-
odd_even = {i:('even' if i%2 ==0 else 'odd') for i in range(1, 11) }
print(odd_even)