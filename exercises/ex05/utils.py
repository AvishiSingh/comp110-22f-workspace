"""The code I wrote for an ex05 assignment!"""

def only_evans(a: list[int])-> list[int]:
    i = 0 
    final_list: list[int] = []
    while i < len(a): 
        if a[i] % 2 == 0: 
         final_list.append(a[i])
    i = i + 1
    return final_list


def concat(a: list[int], b: list[int])-> list[int]: 
    final_list: list[int] = []
    final_list.append(a)
    final_list.append(b)
    return final_list


def sub(a: list[int], b: int, c: int)-> list[int]:
    assert b > c 
    assert len(a) >= c 
    starting_index: int = b 
    ending_index: int = c - 1
    final_list: list[int] = []
    while starting_index <= ending_index: 
        final_list.append(a[starting_index])
        starting_index = starting_index + 1
    return final_list 


