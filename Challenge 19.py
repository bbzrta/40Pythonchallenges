import random

# Guess My Number App

print("Welcome to The Guess My Number App")

name = input("\n\nHello! What is your name:").title().strip()
print("well hi " + name + ", I am thinking of a number between 1 and 20.")

num = random.randint(1, 20)
for i in range(5):
    guess = int(input("\nTake a guess:"))
    if guess < num:
        print("Your guess is too low.")
    elif guess > num:
        print("Your guess is too high.")
    elif guess == num:
        print("Nice job! you got it in " + str(i+1) + " Guesses!!")
        break
    else:
        print("invalid input! please use numbers only!")

if guess != num:
    print("\nyou lost! The answer was " + str(num) + ":(")
