"""These are the test I will use to test the code I made for assignment 5!"""


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_empty() -> None: 
    """Makes sure that given an empty list it will return an empty list!"""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_negative() -> None: 
    """Makes sure that negative functions do not disrupt the code!"""
    xs: list[int] = [1, -2, 3]
    assert only_evens(xs) == [-2]


def test_only_evens_zero() -> None: 
    """Makes sure the modulo function works with zeros!"""
    xs: list[int] = [0, 0, 0]
    assert only_evens(xs) == [0, 0, 0]


def test_concat_empty() -> None: 
    """Makes sure the function will work with empty lists!"""
    xs: list[int] = []
    xxs: list[int] = []
    assert concat(xs, xxs) == []


def test_concat_length() -> None:
    """Makes sure the function will work with lists of different length!"""
    xs: list[int] = [1]
    xxs: list[int] = [1, 0, 3]
    assert concat(xs, xxs) == [1, 1, 0, 3]


def test_concat_negative() -> None: 
    """Makes sure that the negative symbol is able to be properly inserted an represented in the list!"""
    xs: list[int] = [1, 2, -3]
    xss: list[int] = [0, -1, 2]
    assert concat(xs, xss) == [1, 2, -3, 0, -1, 2]


def test_sub_mismatch() -> None: 
    """Makes sure that a backwards indices results in a blank list!"""
    a: list[int] = [1, 2, 3, 4, 5]
    b: int = 4
    c: int = 2
    assert sub(a, b, c) == []


def test_sub_wrong_range() -> None: 
    """Makes sure that an out of range indices results in the first and last digit of the list!"""
    a: list[int] = [1, 2, 3, 4, 5]
    b: int = -100
    c: int = 100 
    assert sub(a, b, c) == [1, 2, 3, 4, 5]


def test_sub_empty() -> None: 
    """Asserts that an empty list will still work!"""
    a: list[int] = []
    b: int = 1
    c: int = 4
    assert sub(a, b, c) == []