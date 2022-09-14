""" Example of a looping through all characters in a string"""

from re import I


user_string: str = input("Give me a string! ")

# The varible i is a common counter variable name in programming. I is short for iteration. 
i: int = 0

while i < len(user_string):
    print (user_string[i])
    i = i + 1

print("Done!")
