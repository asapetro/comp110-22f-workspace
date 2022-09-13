"""Structured Wordle."""

__author__ = "730575054"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# differentiates yellow and white square outputs
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
    # True is returned if guess_word contains single_char
    # otherwise False is returned
    return False
# correct guess letters of correct position add green boxes to the string
# correct guess letter and incorrect position add yellow boxes to string 
# incorrect guess letter adds white box to the string
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
        # fully emojified guess word is returned
    return empty_string       
# Int is inputed and the same length guess word is returned
def input_guess(exp_length: int) -> str:
    """Returns the user's guess of the correct length to the caller."""
    guess_word: str = input(f"Enter a {exp_length} character word:")
    while len(guess_word) != exp_length:
        guess_word = input(f"That wasn't {exp_length} chars! Try again:")
    return guess_word
# secret word is assigned 
def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_count: int = 1
    secret_word: str = "codes"
    while turn_count <= 6:
        print(f"=== Turn {turn_count}/6 ===")
        # input_guess is called to return the user's guess of the correct length
        guess: str = input_guess(len(secret_word))
        # emojified is called to emojify the guess word against the secret word
        print(emojified(guess, secret_word))
        # if guessed correctly, the turn count is automatically assigned to 6 and the loop ends
        if guess == secret_word:
            print(f"You won in {turn_count}/6 turns!")
            turn_count = 6 
        turn_count += 1
    if guess != secret_word:
        print("X/6 - Sorry, try again tomorrow!")
if __name__ == "__main__":
    main()