"""Homework 3 for COMP110!"""
__author__ = "730524902"


def contains_char(word: str, letter: str) -> bool: 
    """This function will take character b and search if it occurs in string a."""
    assert len(letter) == 1
    i = 0 
    limit: int = len(word)
    while i < limit:
        if letter == word[i]:
            return True
            i = len(word)
        if letter != word[i]:
            result: bool = False
            i = i + 1

    return (result)


def emojified(guess: str, secret: str) -> str: 
    """This will return a string of emojis of different colors that codify the matching indices between the guessed word and the secret word."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    ind_x = ""
    x: int = 0
    while x < len(secret): 
        if contains_char(secret, guess[x]) is False: 
            ind_x = ind_x + WHITE_BOX
        
        if contains_char(secret, guess[x]) is True:
            if secret[x] == guess[x]:
                ind_x = ind_x + GREEN_BOX
            else: 
                ind_x = ind_x + YELLOW_BOX
            
        x = x + 1
    
    return (ind_x)


def input_guess(expeclen: int) -> str: 
    """This function will prompt the user for a guess and continue to prompt them until the length of the guess is equal to the expected length."""
    user_guess: str = input(f"Enter a {expeclen} character word: ")
    while len(user_guess) != expeclen:
        user_guess = input(f"That wasn't {expeclen} chars! Try again: ")
    return (user_guess)


def main() -> None: 
    """The entrypoint of the program and the main game loop."""
    attempts: int = 1
    # this variable will act as a counter variable to determine when we need to exit the game loop.
    secret_word: str = "codes"
    user_try: str = ""
    while attempts < 7 and user_try != secret_word: 
        print(f"=== Turn {attempts}/6 ===")
        user_try = input_guess(len(secret_word))
        # this verifies that the input of the user fits within the parameters we want for our game. 
        print(emojified(user_try, secret_word))
        if user_try == secret_word and attempts < 7: 
            final_message: str = (f"You won in {attempts}/6 turns!")
            print(final_message)
        else: 
            attempts = attempts + 1
            
    if attempts == 7: 
        final_message = ("X/6 - Sorry, try again tomorrow!")
        print(final_message)


# Line 101 is actually calling the game so that we can evaluate it.
if __name__ == "__main__":
    main()