"""Dictionary utility functions Ex07."""

__author__ = "730575054"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Returns dictionary with inverted keys and values."""
    result: dict[str, str] = dict()
    for key in dict_1:
        result[dict_1[key]] = key
    if len(dict_1) > len(result):
        raise KeyError
    return result


def favorite_color(fav_colors: dict[str, str]) -> str:
    """Returns most frequent color."""
    sort_list: list[str] = list()
    for key in fav_colors:
        sort_list.append(fav_colors[key])
    count: dict[str, int] = {}
    top_count: int = 0
    max_item: str = ""
    for color in sort_list:
        if color not in count:
            count[color] = 1
        else:
            count[color] += 1
        if count[color] > top_count:
            top_count = count[color]
            max_item = color
    return max_item


def count(inp_list: list[str]) -> dict[str, int]:
    """Returns dictionary of the counts of each of the items in the input list."""
    count: dict[str, int] = {}
    for v in inp_list:
        if v in count:
            count[v] += 1
        if v not in count:
            count[v] = 1
    return count