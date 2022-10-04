"""list utility functions Ex05."""

__author__ = "730575054"


def only_evens(ints_list: list[int]) -> list[int]:
    """Returns even numbers from list."""
    new_list: list[int] = list()
    for number in ints_list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list


def concat(int_list1: list[int], int_list2: list[int]) -> list[int]:
    """Returns new list containing all elements of first list followed by second."""
    new_list: list[int] = list()
    i = 0
    for int_ in int_list1:
        new_list.append(int_list1[i]) 
        i += 1
    i = 0
    for number in int_list2:
        new_list.append(int_list2[i])
        i += 1 
    return new_list


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generate a List which is a subset of the given list, between the specified start index and the end index."""
    new_list: list[int] = list()
    i = start_index
    if start_index == len(a_list):
        return new_list
    if start_index < 0:
        i = 0
    if end_index > len(a_list):
        end_index = len(a_list)       
    for number in a_list:
        new_list.append(a_list[i])
        i += 1
        if i == end_index:
            return new_list
    return new_list