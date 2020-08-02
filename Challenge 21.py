import random
# The Thesaurus App

# Setting the keys and the values
dictionary = {'hot': ['blazing', 'boiling', 'heated', 'sizzling'],
              'cold': ['chilled', 'bleak', 'snowy', 'frozen'],
              'happy': ['merry', 'peaceful', 'thrilled', 'lively'],
              'sad': ['bitter', 'dismal', 'sorry', 'wistful'],
              }

# Print Welcome info
print("Welcome to the Thesaurus App!!")
print("\nChoose a word from  the thesaurus and I will give you  a synonym.")
print("Here are the list of the words:")

for i in dictionary.keys():
    print("\t\t-{0}".format(i))

# Get user's input
choice = input("\nWhat word would you like a synonym for: ").lower().strip()

if choice in dictionary.keys():
    print("The synonym for {0} is {1}!".format(choice,random.choice(dictionary[choice])))
else:
    print("I'm sorry, that word is not currently in the Thesaurus.")

choice = input("\nwould you like to see the whole list? y/n ").lower().strip()

if choice == "y":
    for k, v in dictionary.items():
        print("\n{0} synonyms are:".format(k))
        for value in v:
            print("\t-{0}".format(value))
else:
    print("Thank you for using our app.")