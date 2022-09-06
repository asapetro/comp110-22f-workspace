"""One shot wordle exercise."""

__author__ = "730575054"



secret_word: str = "python"
guess_word: str = input("What is your 6-letter guess?")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess_word) != len(secret_word):
    print(f"That was not 6 letters! Try again: {guess_word}")
    guess_word = input("")

if guess_word != secret_word:
    print("Not quite. Play again soon!")
elif guess_word == secret_word:
    print("Woo! You got it!")

count = 0
#correct_letter = 0

while count < len(guess_word):
    if guess_word[count] == secret_word[count]:  
        print(GREEN_BOX, end ="")
        count = count + 1
    else:
        letter_exists: bool = False
        alt_index = 0
        correct_letter = 0
        while letter_exists != True and alt_index < len(secret_word):
            if secret_word[alt_index] == guess_word[count]:
                letter_exists = True
                alt_index = alt_index + 1
            else:
                alt_index = alt_index + 1
        if letter_exists == True:
            print(YELLOW_BOX, end ="")
        else:
            print(WHITE_BOX, end ="")
    count = count + 1

      



#hile guess_word[0] != secret_word[0]:





#if chr(guess_word)[0] ==ch

#if len(guess_word) == 6 and 
    