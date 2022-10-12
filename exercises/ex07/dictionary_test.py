"""test for dictionary functions Ex07."""

__author__ = "730575054"

from dictionary import invert, favorite_colors


def test_duplicate_kvalues() -> None:
    """Should return KeyError."""
    dict_1: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    assert invert(dict_1) == KeyError


def test_chars() -> None:
    """Tests single char strings."""
    dict_1: dict[str, str] = {'a': 'b', 'c': 'd'}
    assert invert(dict_1) == {'b': 'a', 'd': 'c'}


def test_words() -> None:
    """Tests words for key and value."""
    dict_1: dict[str, str] = {'House': 'Pie', 'Dog': 'Cat'}
    assert invert(dict_1) == {'Pie': 'House', 'Cat': 'Dog'}


def test_tied_best_color() -> None:
    """Test dict with two max color counts."""
    fav_colors: dict[str, str] = {"Marc": "yellow", "Jean": "yellow", "Ezri": "blue", "Kris": "blue", "John": "red"}
    assert favorite_colors(fav_colors) == 'yellow'


def test_more_blue() -> None:
    """Tests dict with more 'blue' values."""
    fav_colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_colors(fav_colors) == 'blue'


def test_all_fav() -> None:
    """Tests dict with all fav colors values."""
    fav_colors: dict[str, str] = {"Marc": "blue", "Ezri": "blue", "Kris": "blue"}
    assert favorite_colors(fav_colors) == 'blue'