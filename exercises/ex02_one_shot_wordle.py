"""One shot wordle exercise."""

__author__ = "730575054"


secret_word: str = "python"
guess_word: str = input("What is your 6-letter guess?")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# loop to make sure that the len() of your guess word is = to the secret word
while len(guess_word) != len(secret_word):
    print(f"That was not 6 letters! Try again: {guess_word}")
    # input to ask for a new guess word if your previous one wasnt 6 letters
    guess_word = input("")

count: int = 0
# loop cycles through each letter of guess word until the count has reached the legnth of the secret word
while count < len(guess_word):
    # the program will print a green box if the position and type of letter for the secret and guess words are the same followed by an empty string so other boxes can be printed in the same line
    if guess_word[count] == secret_word[count]:  
        print(GREEN_BOX, end="")
        count = count + 1
    # If the position of the letter is incorrect then the program will determine whether the letter itself is also incorrect
    else:
        letter_exists: bool = False
        alt_index = 0
        correct_letter = 0
        # letter_exists is the variable to represent the presence of each letter in the guess word that is not in the correct position in the secret word. 
        # it starts off false but if the letter is found in the word, letter_exists will be assigned to True
        # The alternative index will tick up until each letter of the secret word is checked against each letter of the guess word
        while letter_exists is not True and alt_index < len(secret_word):
            if secret_word[alt_index] == guess_word[count]:
                letter_exists = True
                alt_index = alt_index + 1
            else:
                alt_index = alt_index + 1
        # Letters that are assigned to true will print yellow squares
        if letter_exists is True:
            print(YELLOW_BOX, end="")
            count = count + 1
        # Letters that are in the guess word but not in the secret word will print white squares
        else:
            print(WHITE_BOX, end="")
            count = count + 1
if guess_word != secret_word:
    print()
    print("Not quite. Play again soon!")
elif guess_word == secret_word:
    print()
    print("Woo! You got it!")
