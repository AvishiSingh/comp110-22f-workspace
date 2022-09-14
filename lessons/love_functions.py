"""Some tender, loving functions"""

def love (subject: str) -> str: 
    """Given a subject as a parameter it returns a loving string!"""
    return f"I love you {subject}!"

print(love ("Avishi"))

def spread_love (to: str, n: int) -> str: 
    """Generates a str repeating a love message n times"""
    love_note: str = ""
    counter_variable: int = 0
    while counter_variable < n:
        love_note += love(to)+ "\n"
        counter_variable += 1
    return love_note

