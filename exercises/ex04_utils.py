"""List utility functions ex4."""

__author__ = "730575054"

def all(ints_list: list[int], single_int: int) -> bool:
    # If ints list does not contain single int print retrun False
    """Returns True if all ints in int list are single_int"""
    i = 0
    while i < len(ints_list):
        if single_int != ints_list[i]:
            return False
        i += 1
    return True 

def max(ints_list2: list[int]) -> int:
    """Returns the largest int in the list"""
    i = 0
    max_int: int = ints_list2[i + 1]
    while i < len(ints_list2):
        # cycle each int through whole list
        if ints_list2[i] > max_int:
            max_int = ints_list2[i]
        i += 1
    return max_int
    
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Returns True is both lists are equal, False if otherwise"""
    i = 0
    while i < len(int_list1):
        if int_list1[i] != int_list2[i]:
            return False
        i += 1
    return True
