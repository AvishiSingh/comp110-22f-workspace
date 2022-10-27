"""This is my ex07 assignment submission/progress!"""
__author__ = "730524902"


def invert(a: dict[str, str]) -> dict[str, str]: 
    """This function will reverse order of the strs given in a list!"""
    reversed: dict[str, str] = {}
    for value in a: 
        if a[value] in reversed: 
            raise KeyError("KeyError")
        else: 
            reversed[a[value]] = value 
    return reversed 


def favorite_color(a: dict[str, str]) -> str: 
    """Given a dictionary of names and fav colors it returns the color that appears the most frequently!"""
    my_dict: dict[str, int] 
    my_dict = {}
    for item in a: 
        if a[item] in my_dict: 
            my_dict[a[item]] += 1 
        else:
            my_dict[a[item]] = 1
    popular_count: int = 0 
    popular_color: str = ""
    for color in my_dict: 
        if popular_count < my_dict[color]: 
            popular_color = color
            popular_count = my_dict[color]
    return popular_color
        

def count(a: list[str]) -> dict[str, int]: 
    """This function will tell you the most popular color in a dictionary of people and colors!"""
    my_dict: dict[str, int]
    my_dict = {}
    for item in a: 
        if item in my_dict: 
            my_dict[item] += 1 
        else: 
            my_dict[item] = 1 
    return my_dict