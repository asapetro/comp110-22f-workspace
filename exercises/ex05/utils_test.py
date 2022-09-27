"""test for list utility functions Ex05."""

__author__ = "730575054"

from utils import only_evens, sub, concat



def test_only_evens() -> None:
    ints_list: list[int] = [4, 4, 4]
    assert only_evens(ints_list) == [4, 4, 4]

def test_only_evens() -> None:
    ints_list: list[int] = [-1, -2, 3]
    assert only_evens(ints_list) == [-2]

def test_only_evens() -> None:
    ints_list: list[int] = [1, 2, 4]
    assert only_evens(ints_list) == [2, 4]

def test_concat() -> None:
    int_list1: list[int] = [1, 2, 3]
    int_list2: list[int] = [1, 2, 3]
    assert concat(int_list1, int_list2) == ['11', '22', '33']

def test_concat() -> None:
    int_list1: list[int] = [1, 1, 1]
    int_list2: list[int] = [1, 1, 1]
    assert concat(int_list1, int_list2) == ['11', '11', '11']

def test_concat() -> None:
    int_list1: list[int] = []
    int_list2: list[int] = []
    assert concat(int_list1, int_list2) == []

def test_sub() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    start_index: int = 1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == [20, 30]

def test_sub() -> None:
    a_list: list[int] = [-1, 20, 30, 40]
    start_index: int = 1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == [20, 30]

def test_sub() -> None:
    a_list: list[int] = []
    start_index: int = 1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == []