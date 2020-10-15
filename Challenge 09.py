import random

# Welcome message
print("Welcome to the Basketball Roster Program\n")

# Setting the list
team = []

team.append(input("Who is your point guard?").title())
team.append(input("Who is your shooting guard?").title())
team.append(input("Who is your small forward").title())
team.append(input("Who is your power forward?").title())
team.append(input("Who is your centre?").title())

# Summary board
print("\n\tYour starting 5 for the basketball season")
print("\t\tPoint Guard:\t\t" + str(team[0]))
print("\t\tShooting Guard:\t\t" + str(team[1]))
print("\t\tSmall Forward:\t\t" + str(team[2]))
print("\t\tPower Forward:\t\t" + str(team[3]))
print("\t\tCentre:\t\t\t\t" + str(team[4]))

# Remove an injured player
x = random.randint(-1, 5)
injured_player = team.pop(x)
print("\nOh no!" + injured_player + " is injured!\n your team only has " + str(len(team)) + " Players!")
# Add a new player
added_player = input("Who will replace " + injured_player + "?")
team.insert(x, added_player)

# Summary board
print("\n\tYour starting 5 for the basketball season")
print("\t\tPoint Guard:\t\t" + str(team[0]))
print("\t\tShooting Guard:\t\t" + str(team[1]))
print("\t\tSmall Forward:\t\t" + str(team[2]))
print("\t\tPower Forward:\t\t" + str(team[3]))
print("\t\tCentre:\t\t\t\t" + str(team[4]))

print("\ngood luck " + str(team[x]) + ", you will do great.")