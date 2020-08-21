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
    if name in results.keys():
        print("sorry, it seems like that someone that has already voted.")
    else:
        print("Here is the issue: " + issue)
        vote = input("what do you think.. yes or no:").lower().strip()
    if vote == "yes" or vote == "y":
        vote = "yes"
        yes += 1

    elif vote == "no" or vote == "n":
        vote = "no"
        no += 1

    else:
        print("That is not a yes or no answer, but okay..")

    # Adding vote to the dictionary results

    results[name] = vote
    print("Thank you {0}! Your vote of {1} has been recorded.".format(name, vote))

# show who actually voted
total_votes = len(results.keys())
print("\nThe following {0} poeple voted: ".format(total_votes))
for k in results.keys():
    print(k)

# Summarize the voting results
print("\nOn the following issue: " + issue)
if yes > no:
    print("Yes wins! {0} votes to {1}.".format(yes, no))
elif no > yes:
    print("No wins! {0} votes to {1}.".format(no, yes))
else:
    print("it was a tie! {0} votes to {1}.".format(no, yes))

# Allow the admin to see the voting results
guess = input("to see the voting results enter the admin password: ")

if guess == password:
    for k, v in results.items():
        print("voter: {0} \t\tvote: {1}".format(k, v))
else:
    print("Sorry, That is not the correct password. Goodbye...")
print("\n Thank you for using this software")