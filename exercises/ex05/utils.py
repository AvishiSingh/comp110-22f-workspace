"""The code I wrote for an ex05 assignment!"""


def only_evens(a: list[int]) -> list[int]:
    """This will return all the even numbers in a given list!"""
    i = 0 
    final_list: list[int] = []
    while i < len(a): 
        if a[i] % 2 == 0: 
            final_list.append(a[i])
        i = i + 1
    return final_list


def concat(a: list[int], b: list[int]) -> list[int]: 
    """This will take two lists and put them together!"""
    final_list: list[int] = []
    ia = 0 
    ib = 0
    while ia < len(a): 
        final_list.append(a[ia])
        ia = ia + 1
    while ib < len(b):
        final_list.append(b[ib])
        ib = ib + 1
    return final_list


def sub(a: list[int], b: int, c: int) -> list[int]:
    """This will take a list and give you what its contains from indicies b to c minus 1!"""
    starting_index: int = b
    ending_index: int = c - 1
    final_list: list[int] = []
    if b > c:
        return []
    if len(a) == 0:
        return []
    if b == len(a):
        return []
    if starting_index < 0: 
        starting_index = 0 
    if ending_index > len(a):
        ending_index = len(a) - 1
    while starting_index <= ending_index: 
        final_list.append(a[starting_index])
        starting_index = starting_index + 1
    return final_list 