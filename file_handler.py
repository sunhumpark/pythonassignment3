import os

# Name of the file that stores all grade records
FILE_NAME = "grades.txt"


def load_records():
    """
    Load saved grade records from the file.

    Returns:
        list[str]: A list of strings, each string is one saved record line.
    """
    records = []

    # If the file exists, read all lines
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                records.append(line.strip())

    return records


def save_records(records):
    """
    Save all grade records to the file.

    Args:
        records (list[str]): List of grade record strings.
    """
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for r in records:
            file.write(r + "\n")