# Frequency Analysis App
from collections import Counter

print("Welcome to the Frequency Analysis App")

# List of elements to remove
non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "'", '"', '.', '(', ')', '!', '?', ':', ';', ',', ' ']

key_phrase_1 = input("Enter a word, phrase or sentence to analyse: ").lower().strip()


# Removing all the extra elements
for non_letters in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letters, '')

key1_list = list(key_phrase_1)
key1_list.sort()
print(key1_list)
total_occurrences = len(key_phrase_1)

# Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_1)

# Displaying the Frequency Analysis
print("\nHere is the frequency analysis from the key phrase 1: ")
print("\n\tLetter\t\tOccurrences\t\tPercentage")
for key, value in letter_count.items():
    percentage = round(100*value/total_occurrences, 2)
    print("\t{0}\t\t\t{1}\t\t\t\t{2}%".format(key, value, percentage))


# Make a list of letters from highest to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_list = []
for pair in ordered_letter_count:
    key_phrase_1_ordered_list.append(pair[0])

# Print the list
print("\n Letters ordered from highest occurrences to lowest: ")
for letter in key_phrase_1_ordered_list:
    print(letter, end=" ")


####

key_phrase_2 = input("\n\nEnter a word, phrase or sentence to analyse: ").lower().strip()


# Removing all the extra elements
for non_letters in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letters, '')

key2_list = list(key_phrase_2)
key2_list.sort()
print(key2_list)
total_occurrences = len(key_phrase_2)

# Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_2)

# Displaying the Frequency Analysis
print("\nHere is the frequency analysis from the key phrase 2: ")
print("\n\tLetter\t\tOccurrences\t\tPercentage")
for key, value in letter_count.items():
    percentage = round(100*value/total_occurrences, 2)
    print("\t{0}\t\t\t{1}\t\t\t\t{2}%".format(key, value, percentage))


# Make a list of letters from highest to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_2_ordered_list = []
for pair in ordered_letter_count:
    key_phrase_2_ordered_list.append(pair[0])

# Print the list
print("\n Letters ordered from highest occurrences to lowest: ")
for letter in key_phrase_2_ordered_list:
    print(letter, end=" ")