"""Dictionary related utility functions."""

__author__ = "730575054"


from csv import DictReader
# Define youDATA_DIRECTORY="../../data"
DATA_DIRECTORY = "../../data"
DATA_FILE_PATH = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the date file 
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read the date file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Read that file 
    # Close the file when we're done, to free its resources
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], rows_num: int) -> dict[str, list[str]]:
    """Returns column based table with N number of rows of data for each column."""
    result: dict[str, list[str]] = dict()
    i = 0
    if rows_num >= len(column_table):
        return column_table
    for column in column_table:
        a_list: list[str] = list()
        i = 0
        while i < rows_num:
            a_list.append(column_table[column][i])
            i += 1
        result[column] = a_list
    return result


def select(column_table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with subset of the original columns."""
    result: dict[str, list[str]] = dict()
    i = 0
    for value in col_names:
        result[value] = column_table[value]
        i += 1
    return result


def concat(column_table: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        result[column] = column_table[column]
    for column in column_table_2:
        if column in result:
            result[column] += (column_table_2[column])
        else:
            result[column] = column_table_2[column]
    return result


def count(a_list: list[str]) -> dict[str, int]:
    """Returns # of repeat keys."""
    result: dict[str, int] = dict()
    for value in a_list:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result
