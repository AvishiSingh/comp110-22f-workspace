"""This is my progress on assignment ex08"""


from csv import DictReader


def red_csv_rows(path:str) -> list[dict[str, str]]: 
    """This function wil read csv data into a list of rows, where each row if respresented by a dictionary of strings."""
    result: list[dict[str,str]] = []
    file_handle = open(path, "r", enconding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close()
    return result 

def column_values(table:list[dict[str,str]], column:str) -> list[str]: 
    """Make a list of strings of all the values in one column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result

def columnar(rows_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Turn a row oriented table into a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = rows_table[0]
    for column in first_row: 
        result[column] = column_values(rows_table, column)
    return result 

def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]: 
    """Thsi function will make a table withe teh rows of data from the first paraeter for every column."""
    result: dict[str, list[str]] = {}
    start: list[str] = []
    x: list[str] = table[column]
    for column in table: 
        for item in x: 
            if len(start) -1 <= rows: 
                start.append(item)
            result[column] = start
    return result 

def select(table: dict[str, list[str]], x: list[str]) -> dict[str, list[str]]: 
    """Make a table with a subset of original columns."""
    result: dict[str, list[str]] = {}
    for column in x: 
        result.append(table[column])
    return result 


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]: 
    """Combine two tables into one"""
    result: dict[str, list[str]] = {}
    for column in table1: 
        result[column] = table1[column]
    for column in table2: 
        if column in result: 
            result[column]+= table2
        else: 
            result[column] = table2[column]
    return result

