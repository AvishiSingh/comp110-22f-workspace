"""Homework 3 for COMP110!"""
__author__ = "730524902"


def all(a: list[int], b: int) -> bool: 
    """This function, given a list of integers and an integer, this function will tell you if the numbers in a list match the given integer!"""
    limit_all: int = len(a)
    i: int = 0
    alllist_var: list[int] = []
    alllist_var = a
    result: bool = True
    if len(a) == 0: 
        return False 
    while i < limit_all:
        if alllist_var[i] != b: 
            return False
        i = i + 1
    return result


def max(a: list[int]) -> int: 
    """This function will show you the largest number in a list of integers!"""
    limit_max: int = len(a)
    i: int = 0 
    largest_number: int = a[0]
    maxlist_var: list[int] = a
    while i < limit_max:
        if largest_number < maxlist_var[i]: 
            largest_number = maxlist_var[i]
        i = i + 1
    return largest_number


def is_equal(a: list[int], b: list[int]) -> bool: 
    """This function will help determine if two lists are the same!"""
    i: int = 0
    if len(a) != len(b): 
        return False 
    while i < len(a): 
        if a[1] != b[1]: 
            return False
        i = i + 1
    return True
