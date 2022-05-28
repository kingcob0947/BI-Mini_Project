# total = 0
# for i in range(1, 11):
#     total=total+i
#    print(total)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# fruits = ["apple", "banana", "cherry", "orange"]
# for x in fruits:
#   print(x)
#   if x == "cherry":
#     break

# fruits = ["apple", "orange", "mango", "cherry"]
# for x in fruits:
#   if x == "mango":
#     break
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "apple":
#     continue
#   print(x)

#  Increment the sequence with 3 (default is 1):
# for x in range(2, 30, 3):
#   print(x)

#  Print all numbers from 0 to 5, and print a message when the loop has ended:

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

#  Break the loop when x is 3, and see what happens with the else block:

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")

#  Print each adjective for every fruit:

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#   for y in fruits:
#     print(x, y)

# for x in [0, 1, 2]:
#   pass

#############OR###############
import random

winning_number = random.randint(1, 50)
guess = 0
numbers = int(input("guess a number between 1 to 100:"))
game_over = False
while not game_over:
                if numbers == winning_number:
                    print(f"you win and you guessed in {guess} times")
                    game_over = True
                else:
                    if numbers < winning_number:
                        print("Too Low")
                    else:
                        print("Too High")
                    guess = guess + 1
                    numbers = int(input("Try Again"))