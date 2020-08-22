# Frequency Analysis App
from collections import Counter

print("Welcome to the Frequency Analysis App")

# List of elements to remove
non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '"', '.', '(', ')', '!', '?', ':', ';', ',']

key_phrase_1 = input("Enter a word, phrase or sentence to analyse: ").lower().strip()

# Removing all the extra elements
for non_letters in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letters, '')

total_occurrences = len(key_phrase_1)

# Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_1)

print("\nHere is the frequency analysis from the key phrase 1: ")
print("\n\tLetter\t\tOccurrences\t\tPercentage")
for key, value in letter_count.items():
    percentage = round(100*value/total_occurrences, 2)
    print("\t{0}\t\t\t{1}\t\t\t\t{2}%".format(key, value, percentage))