# Voter Registration App
print("Welcome to the Vote Registration App")

# Asking for the users name
name = input("Please enter your name: ").title().strip()
age = int(input("How old are you: "))

# Checking for the registration age
if age < 18:
    # If under 18, program ends without letting the user to register
    print("\nYou are not old enough to register to vote.")
elif age > 17:
    # If over 18, The program allows the user to continue
    print("\nCongratulations " + name + " you are old enough to vote.")
    print("\nHere is a list of political parties to join")
    print("\t\t1 - Republicans\n\t\t2 - Democrats\n\t\t3 - Independent\n\t\t4 - Libertarian\n\t\t5 - Green")

    party = input("\nWhat party would you like to join: ").title().strip()

    print("\nCongratulations {0}! You have joined the {1} party!".format(name, party))

    # Deciding whether the chosen party is major or no.
    if party == "Republicans" or party == "Democrats":
        print("That is a major party!")
    elif party == "Independent" or party == "Libertarian" or party == "Green":
        print("That is not a major party.")
    else:
        print("invalid input! please choose from the options provided.")
else:
    print("Please enter a valid number!")
