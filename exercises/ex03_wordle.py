"""Homework 3 for COMP110!"""
__author__ = "730524902"




def contains_char(word :str, letter:str) -> bool: 
    """This function will take character b and search if it occurs in string a"""
    assert len(letter) == 1
    i = 0 
    while i <= len(word)-1:
        if letter != word[i] and i == len(word) - 1:
            return(False)
            i = i + 1
        else: 
            if letter != word[i]:
                i = i + 1

            if letter == word[i]:
                return(True)
                i = len(word)

def emojified (guess: str, secret: str) -> str: 
    """This will return a string of emojis of different colors that codify the matching indices between the guessed word and the secret word"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    ind_x = ""
    x: int = 0
    while x < len(secret): 
        if contains_char(secret, guess[x]) == False: 
            ind_x = ind_x + WHITE_BOX
        
        if contains_char(secret, guess[x]) == True:
            if secret[x] == guess[x]:
                ind_x = ind_x + GREEN_BOX
            else: 
                ind_x = ind_x + YELLOW_BOX
            
        x = x + 1
    # if contains_char(secret,guess[1]): 
    #     if secret[1] == guess[1]: 
    #         ind_1 = GREEN_BOX
    #     else: 
    #         ind_1 = YELLOW_BOX
    # else: 
    #     ind_1: str = WHITE_BOX
    # if contains_char(secret, guess[2]): 
    #     if secret[2] == guess[2]: 
    #         ind_2 = GREEN_BOX
    #     else: 
    #         ind_2 = YELLOW_BOX
    # else: 
    #     ind_2: str = WHITE_BOX
    # if contains_char(secret, guess[3]): 
    #     if secret[3] == guess[3]: 
    #         ind_3 = GREEN_BOX
    #     else: 
    #         ind_3 = YELLOW_BOX
    # else: 
    #     ind_3: str = WHITE_BOX
    # if contains_char(secret, guess[4]): 
    #     if secret[4] == guess[4]: 
    #         ind_4 = GREEN_BOX
    #     else: 
    #         ind_4 = YELLOW_BOX
    # else: 
    #     ind_4: str = WHITE_BOX

    return(ind_x)


def input_guess(expeclen:int) -> str: 
    """This function will prompt the user for a guess and continue to prompt them until the length of the guess is equal to the expected length"""
    user_guess: str = input(f"Enter a {expeclen} character word:")
    while len(user_guess) != expeclen:
        user_guess: str = input(f"That wasn't {expeclen} chars! Try again:")
    return(user_guess)



def main() -> None: 
    """The entrypoint of the program and the main game loop"""
    attempts: int = 1
     # this variable will act as a counter variable to determine when we need to exit the game loop
    secret_word: str = "codes"
    while attempts < 7: 
        print(f"==Turn {attempts}/6==")
        user_try: str = input_guess(len(secret_word))
        #this verifies that the input of the user fits within the parameters we want for our game. 
        print(emojified(user_try,secret_word))
        if user_try == secret_word: 
            print(f"You won in {attempts}/6 turns!")
        else: 
            attempts = attempts + 1
    if attempts == 7: 
        print("X/6 - Sorry, try again tomorrow!")
    
#Line 101 is actually calling the game so that we can evaluate it
if __name__ == "__main__":
    main()







        
            
        
    
            


    

