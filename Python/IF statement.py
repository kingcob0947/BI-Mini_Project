# a=int(input("enter your number"))
# b=int(input("enter your second number"))
# c=int(input("enter your third number"))
# if a>b and a>c:
#     print("Max number is A = ", a)
# elif b>a and b>c:
#     print("Max number is B = ", b)
# else:
#     print("Max number is C = ", c)

# A=int(input("Enter the number"))
# if A>=5:
#     print("A is positive")
# elif A<5:
#     print("A is negative")
# else:
#     print("A is zero")

A=int(input("Enter your 1st marks"))
B=int(input("Enter your 2nd marks"))
C=int(input("Enter your 3rd marks"))
D=int(input("Enter your 4th marks"))
E=int(input("Enter your 5th marks"))
Total = A+B+C+D+E
Percentage = (Total /500)*100
print(f" Total marks= {Total}, and percent= {Percentage} ")
if Percentage >= 80:
    print("Grade A")
elif Percentage > 60:
    print("Grade B")
elif Percentage > 40:
    print("Grade C")
else:
    print("Grade D")