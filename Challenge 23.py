# Yes or No polling app
print("Hello! welcome to the yes or no polling app!")

# get user input
issue = input("What is the yes or no issue you will be voting on today: ")
vote_number = int(input("what is the number of voters you will allow on this issue: "))
password = input("Enter a password for polling results: ")

# Variables:
yes = 0
no = 0
results = {}

for i in range(vote_number):
    name = input("\nEnter Your full name: ").title().strip()
    print("Here is the issue: " + issue)
    vote = input("what do you think.. yes or no:").lower().strip()
    print("Thank you {0}! Your vote of {1} has been recorded.")

    if vote == "yes" or vote == "y":
        vote = "yes"
        yes += 1

    elif vote == "no":
        vote = "no"
        no += 1

    else:
        print("That is not a yes or no answer, but okay..")