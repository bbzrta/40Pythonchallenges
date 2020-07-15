# Welcome to my Rock Paper Scissors app
import random

user_point = 0
computer_point = 0
print("Welcome to the Rock, Paper, Scissors App.")
name = input("whats your name:")
rounds=int(input("How many rounds would you like to play:"))

for i in range(rounds):
    user = input(" \n\t1..Rock \n\t2..Paper \n\t3..Scissors \nChoose your hand:")
    computer = random.randint(1, 3)
    print(computer)
    if computer == 1 and user == 2:
        print("You Win\n Point for {0}".format(name))
        user_point = user_point + 1
    else: print("its working")
