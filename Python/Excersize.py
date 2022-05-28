# name, char = input("Enter your comma saperate name and char").split(",")
# print(f"length of your name is {len(name)}")
# print(f"count the name charactor {name}")

# Winning_Number = 89
# User_Input = ("Guess the number b/w 1 and 100")
# User_Input = int(User_Input)
# if User_Input == Winning_Number:
#     print("You Won")
# elif User_Input < Winning_Number:
#     print("To Low")
# else:
#     print("Too High")


# user_name = input("enter your name")
# user_age = input("enter your age")
# user_age = int(user_age)
# if user_age >= 18 and (user_name[0] == "a" or user_name[0] == "A"):
#     print("you can watch coco movie")
# else:
#     print("you cannot watch coco")

# n=int(input("enter your number"))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+i
#     i=i+1
# print(f"Total number of sum is = {sum}")

############################
# winning_number = 60
# guess = 1
# numbers=int(input("guess a number between 0 to 100:"))
# game_over = False
# while not game_over:
#     if numbers == winning_number:
#         print(f"you win and guessed this {guess} times")
#         game_over = True
#     else:
#         if numbers < winning_number:
#             print("Too low")
#             guess = guess+1
#             numbers=int(input("guess again:"))
#         else:
#             print("Too high")
#             guess=guess+1
#             numbers=int(input("guess again"))
#
            ############OR With DRY Run###############
            # import random
            #
            # winning_number = random.randint(1, 50)
            # guess = 0
            # numbers = int(input("guess a number between 1 to 100:"))
            # game_over = False
            # while not game_over:
            #     if numbers == winning_number:
            #         print(f"you win and you guessed in {guess} times")
            #         game_over = True
            #     else:
            #         if numbers < winning_number:
            #             print("Too Low")
            #         else:
            #             print("Too High")
            #         guess = guess + 1
            #         numbers = int(input("Try Again"))
#
def wich_grater(a,b):
    if a > b:
        return "a is grater than b"
    else:
        return "b is grater than a"
user1=int(input("enter your number"))
user2=int(input("Enter your number"))
print(wich_grater(user1, user2))
