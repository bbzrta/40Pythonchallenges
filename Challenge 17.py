import random

# initializer
heads = 0
tails = 0

# Welcome to the Coin Toss App
print("Welcome to the Coin Toss App")
print("\nI will flip a coin a set number of times.")

# get user input
counter = int(input("How many times would you like me to flip a coin: "))

# checking if the user wants to print each outcome.
user_choice = input("would like to see each outcome y/n: ").lower().strip()
print("")

# coin tossing
if user_choice == "y":
    for i in range(counter):
        coin = random.randint(1, 2)
        if coin == 1:
            print("HEADS")
            heads += 1
        else:
            print("TAILS")
            tails += 1
else:
    for i in range(counter):
        coin = random.randint(1, 2)
        if coin == 1:
            heads += 1
        else:
            tails += 1


# calculating the percentage
x = heads
y = tails
z = 100/(int(x)+int(y))
heads_percentage = x*z
tails_percentage = y*z

# final outcome
print("\nThere has been {0} Heads. which is {1}% of total.".format(heads, heads_percentage ))
print("There has been {0} Tails. which is {1}% of total.".format(tails,tails_percentage ))

input("press Enter to Exit.")
