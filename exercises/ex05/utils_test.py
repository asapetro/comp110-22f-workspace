"""test for list utility functions Ex05."""

__author__ = "730575054"

from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """m."""
    ints_list: list[int] = [4, 4, 4]
    assert only_evens(ints_list) == [4, 4, 4]


def test_only_evens1() -> None:
    """m."""
    ints_list: list[int] = [-1, -2, 3]
    assert only_evens(ints_list) == [-2]


def test_only_evens2() -> None:
    """m."""
    ints_list: list[int] = [1, 2, 4]
    assert only_evens(ints_list) == [2, 4]


def test_concat() -> None:
    """m."""
    int_list1: list[int] = [1, 2, 3]
    int_list2: list[int] = [1, 2, 3]
    assert concat(int_list1, int_list2) == [1, 2, 3, 1, 2, 3]


def test_concat1() -> None:
    """m."""
    int_list1: list[int] = [1, 1, 1]
    int_list2: list[int] = [1, 1, 1]
    assert concat(int_list1, int_list2) == [1, 1, 1, 1, 1, 1]


def test_concat2() -> None:
    """m."""
    int_list1: list[int] = []
    int_list2: list[int] = []
    assert concat(int_list1, int_list2) == []


def test_sub() -> None:
    """m."""
    a_list: list[int] = [10, 20, 30, 40]
    start_index: int = 1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == [20, 30]


def test_sub1() -> None:
    """m."""
    a_list: list[int] = [-1, 20, 30, 40]
    start_index: int = 1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == [20, 30]


def test_sub2() -> None:
    """m."""
    a_list: list[int] = []
    start_index: int = 1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == []