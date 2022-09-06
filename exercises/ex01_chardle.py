"""EX01 - Chardle assignment!"""

__author__ = "730575054"


chosen_word: str = input("Enter a 5-letter word:")
if len(chosen_word) != 5:
    print("Error: Word must contain 5 characters")
    quit()

single_character: str = input("Enter a single character:")
if len(single_character) != 1:
    print("Error: Character must be a single character")
    quit()

print("Searching for " + single_character + " in " + chosen_word)

count = 0
if chosen_word[0] == single_character:
    print(single_character + " found at index 0")
    count = count + 1
if chosen_word[1] == single_character:
    print(single_character + " found at index 1")
    count = count + 1
if chosen_word[2] == single_character:
    print(single_character + " found at index 2")
    count = count + 1
if chosen_word[3] == single_character:
    print(single_character + " found at index 3")
    count = count + 1
if chosen_word[4] == single_character:
    print(single_character + " found at index 4")
    count = count + 1

if count == 0:
    print("No instances of " + single_character + " found in " + chosen_word)
if count == 1:
    print("1 instance of " + single_character + " found in " + chosen_word)
if count > 1:
    print(str(count) + " instances of " + single_character + " found in " + chosen_word)