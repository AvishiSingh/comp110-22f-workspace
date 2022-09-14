"""EX01 - Chardle - A cute step toward Wordle!"""
__author__ = "730524902"

total_matches: int = (0)

user_guess_word: str = input("Enter a 5-character word:")
if len(user_guess_word) != int(5):
    print("Error: Word must contain 5 letters")
    exit()
user_guess_letter: str = input("Enter a single character:")
if len(user_guess_letter) != int(1):
    print("Error: Character must be a single character") 
    exit()
print("Searching for " + user_guess_letter + " in " + user_guess_word)
if user_guess_letter == user_guess_word[0]:
    print(user_guess_letter + " found at index 0!")
    total_matches = total_matches + (1)
if user_guess_letter == user_guess_word[1]:
    print(user_guess_letter + " found at index 1!")
    total_matches = total_matches + 1
if user_guess_letter == user_guess_word[2]:
    print(user_guess_letter + " found at index 2!")
    total_matches = total_matches + 1
if user_guess_letter == user_guess_word[3]:
    print(user_guess_letter + " found at index 3!")
    total_matches = total_matches + 1
if user_guess_letter == user_guess_word[4]:
    print(user_guess_letter + " found at index 4!")
    total_matches = total_matches + 1
if total_matches == 1:
    print(str(total_matches) + " instance of " + user_guess_letter + " found in " + user_guess_word)
if total_matches > 1:
    print(str(total_matches) + " instances of " + user_guess_letter + " found in " + user_guess_word)
if total_matches == 0: 
    print("No instances of " + user_guess_letter + " found in " + user_guess_word)