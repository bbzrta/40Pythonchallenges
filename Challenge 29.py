# Guess The Word
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Welcome to the guess my word app!")

game_dict = {
    "sports": ['basketball', 'tennis', 'baseball', 'soccer', 'curling'],
    "colours": ['orange', 'yellow', 'purple', 'black', 'red', 'blue'],
    "fruits": ['apple', 'peach', 'banana', 'pear', 'mango', 'strawberry'],
    "classes": ['english', 'history', 'science', 'mathematics', 'art'],
    "movies": ['shutter island', 'ponyo', 'drop dead fred', 'silicone valley']
}

game_keys = []

for key in game_dict.keys():
    game_keys.append(key)

while True:
    category = game_keys[random.randint(0, len(game_dict) - 1)]
    word = game_dict[category][random.randint(0, len(game_dict[category]) - 1)]

    blank_word = []
    for letter in word:
        blank_word.append("-")

    clear()
    print("\nguess a {0} letter word from the {1} category!".format(len(word), category))

    guess = ""
    guess_count = 0

    while guess != word:
        print(*blank_word, sep='')
        guess = input("Enter your guess: ")
        guess_count += 1

        if guess == word:
            print("\nCorrect! you guessed it after {0} tries!".format(guess_count))
        else:
            clear()
            print("\nThat is incorrect. lets reveal a letter!")
            while True:
                word_index = random.randint(0, len(word) - 1)
                blank_word[word_index] = word[word_index]
                break

    if input("\nwould you like ot play again(Y/n): ").lower() == "n":
        clear()
        quit("Thank you! Quitting...")
