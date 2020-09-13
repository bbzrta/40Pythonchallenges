# Challenge 24 Frequency analysis app
from collections import Counter

print('welcome to the Frequency Analysis App.')

non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
               '-', '_', '=', "'", '"', '?', '!', '.', ',', '(',
               ')', ';', ':', '%', ' ', '/', '\\', '*', '[', ']', '#']

key_phrase_1 = input("\nplease Enter a word or a phrase to analyse: ").lower().strip()

# Removing all none letters from our sentence
for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter, '')

total_occurrences = len(key_phrase_1)

# Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_1)

# Print the results up to 2 decimals percentage
print("Here is the frequency analysis from key phrase 1: ")
print("\n\tLetter\t\tOccurrences\t\tPercentage")
for k, v in sorted(letter_count.items()):
    percentage = round(100 * v / total_occurrences, 2)
    print("\t{0}\t\t\t{1}\t\t\t\t{2}%".format(k, v, percentage))

# Ordering most common in a clean list of the letters
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])

# Printing the above list in a clean way
print("\nLetters ordered from highest to lowest occurrence: ", end='')
for i in key_phrase_1_ordered_letters:
    print(i, end='')

###############################----Phrase 2----###############################

key_phrase_2 = input("\nplease Enter a word or a phrase to analyse: ").lower().strip()

# Removing all none letters from our sentence
for non_letter in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letter, '')

total_occurrences_2 = len(key_phrase_2)

# Create a counter object to tally the number of each letter
letter_count_2 = Counter(key_phrase_2)

# Print the results up to 2 decimals percentage
print("Here is the frequency analysis from key phrase 2: ")
print("\n\tLetter\t\tOccurrences\t\tPercentage")
for k, v in sorted(letter_count_2.items()):
    percentage_2 = round(100 * v / total_occurrences_2, 2)
    print("\t{0}\t\t\t{1}\t\t\t\t{2}%".format(k, v, percentage_2))

# Ordering most common in a clean list of the letters
ordered_letter_count_2 = letter_count_2.most_common()
key_phrase_2_ordered_letters = []
for pair in ordered_letter_count_2:
    key_phrase_2_ordered_letters.append(pair[0])

# Printing the above list in a clean way
print("\nLetters ordered from highest to lowest occurrence: ", end='')
for i in key_phrase_2_ordered_letters:
    print(i, end='')

