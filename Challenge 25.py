# Frequency Analysis App
from collections import Counter

print("Welcome to the Frequency Analysis App")

# List of elements to remove
non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "'", '"', '.', '(', ')', '!', '?', ':', ';', ',', ' ']

key_phrase_1 = ("""
                There are  certain  sores in  life that, like  a  canker,  
                gnaw  at  the  soul  in solitude and diminish it. 
                Since generally it is the custom to attribute these incredible  sufferings  to  the  
                realm  of  rare  and  singular  accidents  and happenings, 
                it is not possible to speak about them to others. If one does talk or 
                write about  them,  people  pretend  to  accept  them  with  sarcastic remarks  and  dubious smiles.  In  
                reality, however, they  follow  prevalent  beliefs  and  their  own  ideas  about them.  The  reason  is 
                that  these  pains do  not  have  a  remedy.  The  only  remedy  is forgetfulness  induced  by  wine,  
                or artificial  sleep  induced  by  opium  and  other narcotics. Unfortunately, the effect of these drugs 
                is transitory. After a while, instead of soothing, they add to the pain.
                 """)


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

key_phrase_2 = ("""
                    I felt the anguish of one who is awakened from a long, deep sleep. I rubbed my eyes.  
                    I  was  in  my  old  room. It  was  dawnand  a  wet  fog  covered  the  windowpanes. 
                    The crow of a rooster came from afar.The red coal inthe brazier in front of me had turned to cold ash,
                    unable to withstand the blow of a single breath.My thoughts, too, I  felt,like  the  red  pieces  of
                    charcoal,had  turned  into  hollow  ashes  unable  towithstand the blow of a single breath.
                    The first thing I looked for was the Raqjar that the old carriage driver had given me  in  the  
                    graveyard,  but  it  was  not in  front  ofme.  Then,  I  saw  someone  with  a stooped  shadow,  
                    no,  a  stooped  old  man  who  had  covered  his  head  and  face  with  a scarf and who carried 
                    something like a jar wrapped in a dirty handkerchief under his arm. He was laughing: a hideous, 
                    hollow laughter that made one'shair stand on end.The moment I moved, he left my room. I stood up, 
                    intending to pursue him and recover  the  jar thatwas  wrapped  in  a  dirty  handkerchief;  but  
                    the  old  man,with  a peculiar agility, disappeared. I returned to my room and opened  
                    the  window  that gives to the alley. He was carrying the bundle under his arm. His maniacal 
                    laughter made his shoulders shake violently. He trudged  along until he disappeared into the mist. 
                    I returned from the window and looked at myself. My clothes were torn, and I was  covered  from  
                    head to toe with  coagulated  blood. Two  golden flybeeswere flying around me and small, white 
                    worms were wriggling on my body;the weight of a dead body pressed against my chest...
                 """)


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