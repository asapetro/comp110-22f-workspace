"""Structured Wordle."""

__author__ = "730575054"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"



def contains_char(guess_word: str, single_char: str) -> bool:
    """Returns True if the single character of the second string is found at any index of the first string"""
    assert len(single_char) == 1
    alt_index = 0
    while alt_index < len(guess_word):
        if guess_word[alt_index] == single_char:
            alt_index += 1 
            return True
        else:
            alt_index = alt_index + 1
    return False
   
def emojified(guess_word: str, secret_word: str) -> str:
    """Returns emojified answer to guess"""
    assert len(guess_word) == len(secret_word)
    count = 0
    empty_string: str = ""

    while count < len(guess_word):
        if guess_word[count] == secret_word[count]:  
            empty_string = empty_string + GREEN_BOX
        else:
            single_char = guess_word[count]
            if contains_char(secret_word, single_char):
                empty_string = empty_string + YELLOW_BOX
            else: 
                empty_string = empty_string + WHITE_BOX
        count = count + 1
    return empty_string
        

    #while count < len(guess_word):
       # if guess_word[count] == secret_word[count]:  
            #count = count + 1
           # print(GREEN_BOX)
        #else:
           # return contains_char
           # if contains_char is True:
                #count = count + 1
                #return YELLOW_BOX
           # if contains_char is not True:
               # count = count + 1
               # return WHITE_BOX
                
