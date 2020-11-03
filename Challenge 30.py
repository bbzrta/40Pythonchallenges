# Power-Ball Simulator app
import random
print("------------------------Power-Ball Simulator------------------------")

white_balls = int(input("How many white-balls to from from for the 5 winning number(Normally 69): "))
if white_balls < 5:
    white_balls = 5

red_balls = int(input("How many red-balls to from for the Power-Ball (Usually 26): "))
if red_balls < 1:
    red_balls = 1

odds = 1

for i in range(5):
    odds *= white_balls - i
    print(odds)

odds *= red_balls/120
print("you have 1 in {0} chance of winning this lottery.".format(odds))

ticket_interval = int(input("Purchase tickets in what interval: "))

winning_numbers = []
while len(winning_numbers) < 5:
    number = random.randint(1, white_balls)
    if number not in winning_numbers:
        winning_numbers.append(number)
winning_numbers.sort()

number = random.randint(1, red_balls)
winning_numbers.append(number)

