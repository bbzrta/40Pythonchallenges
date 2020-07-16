# Welcome to my Rock Paper Scissors app
import random

options = ["Rock", "Paper", "Scissors"]
user_point = 0
computer_point = 0
print("Welcome to the Rock, Paper, Scissors App.")
name = input("whats your name:").title().strip()
rounds = int(input("How many rounds would you like to play:"))

for i in range(rounds):

    print("\nRound {0}".format(i+1))
    print("Player: {0}\tComputer:{1}".format(user_point,computer_point))
    user = int(input(" \n\t1..Rock \n\t2..Paper \n\t3..Scissors \n\nChoose your hand: "))
    user = user - 1
    user = options[user]
    computer = random.choice(options)
    print("Computer Chose: {0}\n".format(computer))


    if computer == options[0] and user == options[1]:
        print("You win!! Point for {0}".format(name))
        user_point = user_point + 1
        print("Player: {0}\tComputer:{1}\n".format(user_point, computer_point))
        input("\nPress ENTER ro continue")
    elif computer == options[0] and user == options[2]:
        print("Computer wins!! Point for Computer")
        computer_point = + 1
        print("Player: {0}\tComputer:{1}\n".format(user_point, computer_point))
        input("\nPress ENTER ro continue")
    elif computer == options[0] and user == options[0]:
        print("its a tie! hoe boring.")
        print("Player: {0}\tComputer:{1}\n".format(user_point, computer_point))
        input("\nPress ENTER ro continue")

    elif computer == options[1] and user == options[0]:
        print("You win!! Point for {0}".format(name))
        user_point = user_point + 1
        print("Player: {0}\tComputer:{1}\n".format(user_point, computer_point))
        input("\nPress ENTER ro continue")
    elif computer == options[1] and user == options[2]:
        print("Computer wins!! Point for Computer")
        computer_point = + 1
        print("Player: {0}\tComputer:{1}\n".format(user_point, computer_point))
        input("\nPress ENTER ro continue")
    elif computer == options[1] and user == options[1]:
        print("its a tie! hoe boring.")
        print("Player: {0}\tComputer:{1}\n".format(user_point, computer_point))
        input("\nPress ENTER ro continue")

    elif computer == options[2] and user == options[0]:
        print("You win!! Point for {0}".format(name))
        user_point = user_point + 1
        print("Player: {0}\tComputer:{1}\n".format(user_point, computer_point))
        input("\nPress ENTER ro continue")
    elif computer == options[2] and user == options[1]:
        print("Computer wins!! Point for Computer")
        computer_point = + 1
        print("Player: {0}\tComputer:{1}\n".format(user_point, computer_point))
        input("\nPress ENTER ro continue")
    elif computer == options[2] and user == options[2]:
        print("its a tie! how boring.")
        print("Player: {0}\tComputer:{1}\n".format(user_point, computer_point))
        input("\nPress ENTER ro continue")
    else:
        print("Invalid input please enter the number of  you choice:")
