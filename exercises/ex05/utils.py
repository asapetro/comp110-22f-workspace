"""list utility functions Ex05."""

__author__ = "730575054"

def only_evens(ints_list: list[int]) -> list[int]:
    """Returns even numbers from list."""
    new_list: list[int] = list()
    for number in ints_list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

def concat(int_list1: list[int], int_list2: list[int]) -> list[str]:
    """Returns new list containing all elements of first list followed by second."""
    new_list: list[str] = list()
    i = 0
    for number in int_list1:
        new_list.append(str(int_list1[i]) + str(int_list2[i]))
        i += 1
    return new_list

def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """enerate a List which is a subset of the given list, between the specified start index and the end index."""
    new_list: list[str] = list()
    i = start_index
    for number in a_list:
        new_list.append(a_list[i])
        i += 1
        if i == end_index:
            return new_list
