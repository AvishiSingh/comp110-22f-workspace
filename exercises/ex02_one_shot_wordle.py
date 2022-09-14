"""Homework 2 for COMP110!"""
__author__ = "730524902"
secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
ind_0: str = WHITE_BOX
ind_1: str = WHITE_BOX
ind_2: str = WHITE_BOX
ind_3: str = WHITE_BOX
ind_4: str = WHITE_BOX
ind_5: str = WHITE_BOX
user_guess_word: str = input("What is your 6-letter guess?")
while len(user_guess_word) != 6:
    user_guess_word = input("That was not 6 letters! Try again:")
if len(user_guess_word) == 6 and user_guess_word == secret_word:
    print(GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX)
    print("Woo! You got it!")
else:
    if user_guess_word[0] == secret_word[0]:
        ind_0 = GREEN_BOX
    elif user_guess_word[0] == secret_word[1]:
        ind_0 = YELLOW_BOX
    elif user_guess_word[0] == secret_word[2]:
        ind_0 = YELLOW_BOX
    elif user_guess_word[0] == secret_word[3]: 
        ind_0 = YELLOW_BOX
    elif user_guess_word[0] == secret_word[4]:
        ind_0 = YELLOW_BOX
    elif user_guess_word[0] == secret_word[5]:
        ind_0 = YELLOW_BOX
    if user_guess_word[1] == secret_word[1]:
        ind_1 = GREEN_BOX
    elif user_guess_word[1] == secret_word[0]:
        ind_1 = YELLOW_BOX
    elif user_guess_word[1] == secret_word[2]:
        ind_ = YELLOW_BOX
    elif user_guess_word[1] == secret_word[3]: 
        ind_1 = YELLOW_BOX
    elif user_guess_word[1] == secret_word[4]:
        ind_1 = YELLOW_BOX
    elif user_guess_word[1] == secret_word[5]:
        ind_1 = YELLOW_BOX
    if user_guess_word[2] == secret_word[2]:
        ind_2 = GREEN_BOX
    elif user_guess_word[2] == secret_word[1]:
        ind_2 = YELLOW_BOX
    elif user_guess_word[2] == secret_word[0]:
        ind_2 = YELLOW_BOX
    elif user_guess_word[2] == secret_word[3]: 
        ind_2 = YELLOW_BOX
    elif user_guess_word[2] == secret_word[4]:
        ind_2 = YELLOW_BOX
    elif user_guess_word[2] == secret_word[5]:
        ind_2 = YELLOW_BOX
    if user_guess_word[3] == secret_word[3]:
        ind_3 = GREEN_BOX
    elif user_guess_word[3] == secret_word[1]:
        ind_3 = YELLOW_BOX
    elif user_guess_word[3] == secret_word[2]:
        ind_3 = YELLOW_BOX
    elif user_guess_word[3] == secret_word[0]: 
        ind_3 = YELLOW_BOX
    elif user_guess_word[3] == secret_word[4]:
        ind_3 = YELLOW_BOX
    elif user_guess_word[3] == secret_word[5]:
        ind_3 = YELLOW_BOX
    if user_guess_word[4] == secret_word[4]:
        ind_4 = GREEN_BOX
    elif user_guess_word[4] == secret_word[1]:
        ind_4 = YELLOW_BOX
    elif user_guess_word[4] == secret_word[2]:
        ind_4 = YELLOW_BOX
    elif user_guess_word[4] == secret_word[3]: 
        ind_4 = YELLOW_BOX
    elif user_guess_word[4] == secret_word[0]:
        ind_4 = YELLOW_BOX
    elif user_guess_word[4] == secret_word[5]:
        ind_4 = YELLOW_BOX
    if user_guess_word[5] == secret_word[5]:
        ind_5 = GREEN_BOX
    elif user_guess_word[5] == secret_word[1]:
        ind_5 = YELLOW_BOX
    elif user_guess_word[5] == secret_word[2]:
        ind_5 = YELLOW_BOX
    elif user_guess_word[5] == secret_word[3]: 
        ind_5 = YELLOW_BOX
    elif user_guess_word[5] == secret_word[4]:
        ind_5 = YELLOW_BOX
    elif user_guess_word[5] == secret_word[0]:
        ind_5 = YELLOW_BOX
    print(ind_0 + ind_1 + ind_2 + ind_3 + ind_4 + ind_5)
    print("Not quite. Play again soon!")