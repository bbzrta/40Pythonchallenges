# Challenge 24 Frequency analysis app
from collections import Counter

print('welcome to the Frequency Analysis App.')

non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
               '-', '_', '=', "'", '"', '?', '!', '.', ',', '(',
               ')', ';', ':', '%', ' ', '/', '\n', '*', '[', ']', '#', '  ']

key_phrase_1 = ("""I felt the anguish of one who is awakened from a long, deep sleep. I rubbed my eyes.
I was in  my  old room.It was dawn and a wet fog covered the windowpanes.
The crow of a rooster came from afar.The red coal in the brazier in front of me had turned to cold ash,
unable to withstand the blow of a single breath.My thoughts, too, I felt,like the red pieces of
charcoal,had  turned into hollow ashes unable to withstand the blow of a single breath.
The first thing I looked for was the Raqjar that the old carriage driver had given me in the
graveyard, but it was not in front of me. Then, I saw someone with a stooped shadow,
no, a stooped old man who had covered his head and face with a scarf and who carried
something like a jar wrapped in a dirty handkerchief under his arm. He was laughing: a hideous, 
hollow laughter that made one's hair stand on end.The moment I moved, he left my room. I stood up,
intending to pursue him and recover the jar that was wrapped in a dirty handkerchief; but
the old man,with a peculiar agility, disappeared. I returned to my room and opened
the window that gives to the alley. He was carrying the bundle under his arm. His maniacal
laughter made his shoulders shake violently. He trudged along until he disappeared into the mist.
I returned from the window and looked at myself. My clothes were torn, and I was  covered  from
head to toe with coagulated blood. Two golden fly bees were flying around me and small, white
worms were wriggling on my body;the weight of a dead body pressed against my chest... Jaqi. Qolam. xoda. zamin
""").lower().strip()

# Removing all none letters from our sentence
for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter, '')

total_occurrences = len(key_phrase_1)

# Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_1)

# Print the results up to 2 decimals percentage
print("\nHere is the frequency analysis from key phrase 1: ")
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

key_phrase_2 = ("""There are  certain  sores in  life that, like  a  canker,  
gnaw  at  the  soul  in solitude and diminish it. 
Since generally it is the custom to attribute these incredible  sufferings  to  the  
realm  of  rare  and  singular  accidents  and happenings, 
it is not possible to speak about them to others. If one does talk or 
write about  them,  people  pretend  to  accept  them  with  sarcastic remarks  and  dubious smiles.  In  
reality, however, they  follow  prevalent  beliefs  and  their  own  ideas  about them.  The  reason  is 
that  these  pains do  not  have  a  remedy.  The  only  remedy  is forgetfulness  induced  by  wine,  
or artificial  sleep  induced  by  opium  and  other narcotics. Unfortunately, the effect of these drugs 
is transitory. After a while, instead of soothing, they add to the pain. Jaqi. Qolam. xoda. zamin.
""").lower().strip()

# Removing all none letters from our sentence
for non_letter in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letter, '')

total_occurrences_2 = len(key_phrase_2)

# Create a counter object to tally the number of each letter
letter_count_2 = Counter(key_phrase_2)

# Print the results up to 2 decimals percentage
print("\n\n####################################################")
print("\nHere is the frequency analysis from key phrase 2: ")
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
print("\nLetters ordered from highest to lowest occurrence: ", end='\n\n')
for i in key_phrase_2_ordered_letters:
    print(i, end='')

# Encode/Decode a given message using phrase one and two
choice = input("\n\nwould you like to encode or decode a message: ").strip().lower()
phrase = input("\nWhat is the phrase: ").lower().strip()

for non_letter in non_letters:
    phrase = phrase.replace(non_letter, '')

if choice == 'encode':
    encoded_phrase = []
    for letter in phrase:
        index = key_phrase_1_ordered_letters.index(letter)
        letter = key_phrase_2_ordered_letters[index]
        encoded_phrase.append(letter)

    print("the encode message is: ")
    for i in encoded_phrase:
        print(i, end="")

elif choice == 'decode':
    decoded_phrases = []
    for letter in phrase:
        index = key_phrase_2_ordered_letters.index(letter)
        letter = key_phrase_1_ordered_letters[index]
        decoded_phrases.append(letter)

    print("the decoded message is: ")
    for i in decoded_phrases:
        print(i, end='')

else:
    print("OOPS! please enter encode or decode!")