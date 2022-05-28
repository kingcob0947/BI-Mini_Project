
#  Find sum of square from 1 to n
# n=int(input("enter your number"))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+i*i
#     i=i+1
# print(f"sum = {sum}")

#  WAP to find sum from 1 to n
# n=int(input("Enter your number"))
# sum=0
# i=1
# while (i<=n):
#     sum=sum+i
#     i=i+1
# print(f"Sum ={sum}")

#  WAP print only even number b/w 1 to n.
# n=int(input("enter your number"))
# i=2
# while(i<=n):
#     print(i)
#     i=i+2
#  WAP to finds sum of even from 1 to n.
# n=int(input("Enter your sum number"))
# i=2
# sum=0
# while(i<=n):
#     sum=sum+2
#     i=i+2
# print(f"Sum of even number is = {sum}")


##################
winning_number = 56
guess = 1
number=int(input("Guess a number between 0 to 100:"))
game_over = False
while not game_over:
    if number == winning_number:
        print(f"you win and you gusses this number in {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("Too Low")
            guess=guess+1
            number=int(input("guess number again:"))
        else:
            print("to high")
            guess=guess+1
            number=int(input("guess number again:"))