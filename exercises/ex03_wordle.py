"""Structured Wordle."""

__author__ = "730575054"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(guess_word: str, single_char: str) -> bool:
    """Returns True if the single character of the second string is found at any index of the first string."""
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
    """Returns emojified answer to guess."""
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
        
def input_guess(exp_length: int) -> str:
    """Returns the user's guess of the correct length to the caller."""
    guess_word: str = input(f"Enter a {exp_length} character word:")
    while len(guess_word) != exp_length:
        guess_word = input(f"That wasn't {exp_length} chars! Try again:")
    return guess_word

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_count: int = 1
    secret_word: str = "codes"
    while turn_count <= 6:
        print(f"=== Turn {turn_count}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turn_count}/6 turns!")
            turn_count = 6 
        turn_count += 1
    if guess != secret_word:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()





       # input_guess(len(secret_word))
        #print(emojified(guess_word, secret_word))
        #if guess_word == secret_word:
          # print(f"You won in {turn_count}/6 turns!")
            #return None
        
        


