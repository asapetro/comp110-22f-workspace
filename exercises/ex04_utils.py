"""List utility functions ex4."""

__author__ = "730575054"


def all(ints_list: list[int], single_int: int) -> bool:
    # If ints list does not contain single int print retrun False
    """Returns True if all ints in int list are single_int."""
    i = 0
    if len(ints_list) == 0:
        return False
    while i < len(ints_list):
        if single_int != ints_list[i]:
            return False
        i += 1
    return True 


def max(input1: list[int]) -> int:
    """Returns the largest int in the list."""
    if len(input1) == 0:
        raise ValueError("max() arg is an empty List")
    i = 0
    max_int: int = input1[i + 1]
    while i < len(input1):
        # cycle each int through whole list
        if input1[i] > max_int:
            max_int = input1[i]
        i += 1
    return max_int


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Returns True is both lists are equal, False if otherwise."""
    i = 0
    if len(int_list1) == 0 and len(int_list2) == 0:
        return True
    if len(int_list1) == 0:
        return False
    if len(int_list2) == 0:
        return False
    while i < len(int_list1):
        if int_list1[i] != int_list2[i] or len(int_list1) != len(int_list2):
            return False
        i += 1
    return True
