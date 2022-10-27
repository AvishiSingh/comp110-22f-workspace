"""These are my tests for my EX07 assignment!"""
__author__ = "730524902"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count 


def test_invert_empty() -> None: 
    """This makes sure that the function given an empty list will return an empty list!"""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_use1() -> None: 
    """This function will test invert with a dictionary of only 1!"""
    xs: dict[str, str] = {'dog': 'cat'}
    assert invert(xs) == {'cat': 'dog'}


def test_invert_use2() -> None: 
    """This function will test the invert function with a dictionary with multiple keys!"""
    xs: dict[str, str] = {'dog': 'cat', 'elephant': 'mouse'}
    assert invert(xs) == {'cat': 'dog', 'mouse': 'elephant'}


def test_favoritecolor_empty() -> None: 
    """This function will test what happens when the given an empty dictionary!"""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_favoritecolor_use1() -> None: 
    """This function tests a dictionary with one 1 key!"""
    xs: dict[str, str] = {'mike': 'blue'}
    assert favorite_color(xs) == "blue"


def test_favoritecolor_use2() -> None: 
    """This function tests a dictionary with multiple items!"""
    xs: dict[str, str] = {'mike': 'blue', 'tana': 'pink', 'ben': 'pink'}
    assert favorite_color(xs) == "pink"


def test_count_empty() -> None: 
    """This function will test what happens when the given an empty list!"""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_use1() -> None: 
    """This function tests a list of length 1!"""
    xs: list[str] = ["fun"]
    assert count(xs) == {'fun': '1'}


def test_count_use2() -> None: 
    """This function tests a list with multiple objects!"""
    xs: list[str] = ["fun", "apple"]
    assert count(xs) == {'fun': '1', 'apple': '1'}