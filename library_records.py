"""
CS 218 - Intermediate Python
Programming Assignment 3: File I/O and Exception Handling

In this assignment, you will practice reading, writing, and appending
text files, CSV files, and JSON files, along with handling exceptions
using try/except/finally, applied to a small library checkout and
catalog scenario.

Complete each function below according to its docstring. Do NOT change
the function names or parameter lists -- the autograder
(test_library_records.py) depends on these exact signatures.

You may add helper functions of your own if you would like, but every
function listed in the README's "Functions to Implement" section must
be completed for the tests to pass.
"""
import os  # if you want to use `os.path.isfile(file_path)` to check existance
import csv
import json


def append_checkout_record(filename: str, member: str, title: str) -> None:
    """
    Record that a library member has checked out a book by APPENDING a
    single line to a plain text log file.

    Open `filename` in append mode ("a") using a context manager and
    write one line formatted exactly as:

        member|title

    (followed by a newline). Because the file is opened in append
    mode, calling this function multiple times should add multiple
    lines to the file rather than overwriting previous entries. If the
    file does not already exist, it should be created.

    :param filename: str, path to the text log file to append to
    :param member: str, the name of the library member
    :param title: str, the title of the book being checked out
    :return: None
    """
    # TODO: Implement this function
    pass


def load_checkout_counts(filename: str) -> dict[str, int]:
    """
    Read the checkout log written by `append_checkout_record` and tally
    how many books each member has checked out.

    Read `filename` line by line (using a `for` loop). Each line is
    expected to look like "member|title". Split each line on "|" and
    increment that member's count in the result dictionary.

    Handle errors gracefully:
    - If the file does not exist, catch the `FileNotFoundError` and
      return an empty dictionary.
    - If a line does NOT contain exactly one "|" separator (so
      unpacking it into `member, title` raises a `ValueError`), catch
      the `ValueError` and skip that line (use `continue` in the
      `except` block) rather than letting the whole function fail.

    :param filename: str, path to the text log file to read
    :return: dict mapping member name (str) to number of checkouts (int)
    """
    # TODO: Implement this function
    pass


def close_out_session(filename: str, final_note: str) -> str:
    """
    Close out a library session, writing a final note to the log file
    and *always* recording that the session ended, even if the note
    itself turns out to be invalid.

    - In a `try` block: if `final_note` is empty or only whitespace,
      raise a `ValueError` with the message
      "Final note cannot be empty.". Otherwise, append `final_note`
      (plus a trailing newline) to `filename`.
    - In an `except ValueError` block: catch the error and set the
      status message to `f"Session closed with warning: {e}"` (where
      `e` is the caught exception).
    - In a `finally` block: regardless of whether the note was valid,
      ALWAYS append the line "SESSION END" (plus a trailing newline)
      to `filename`.
    - If no error occurred, the status message should be
      "Session closed normally.".

    Return the status message in all cases.

    :param filename: str, path to the text log file to append to
    :param final_note: str, the closing note to record
    :return: str, a status message describing how the session closed
    """
    # TODO: Implement this function
    pass


def export_catalog_to_csv(filename: str, catalog: list[tuple[str, int]]) -> None:
    """
    Write a list of (title, copies_available) tuples out to a CSV
    file using `csv.DictWriter`, with the header row
    "title,copies_available".

    Open the file with `newline=""` (as recommended by the `csv`
    module documentation), build a `csv.DictWriter` with fieldnames
    `["title", "copies_available"]`, write the header with
    `writeheader()`, and then write one row per entry in `catalog`.

    :param filename: str, path to the CSV file to create/overwrite
    :param catalog: list of (title: str, copies_available: int) tuples
    :return: None
    """
    # TODO: Implement this function
    pass


def import_available_titles(filename: str, min_copies: int) -> list[str]:
    """
    Read a catalog CSV file (with headers "title" and
    "copies_available") using `csv.DictReader`, and return a sorted
    (ascending, alphabetical) list of titles that have AT LEAST
    `min_copies` copies available.

    Handle errors gracefully:
    - If a row's `copies_available` value cannot be converted to an
      int, catch the `ValueError` and skip that row.
    - If the file does not exist, catch the `FileNotFoundError` and
      return an empty list.

    :param filename: str, path to the CSV file to read
    :param min_copies: int, the minimum number of copies (inclusive)
    :return: sorted list of str, titles meeting the threshold
    """
    # TODO: Implement this function
    pass


def update_library_settings(filename: str, key: str, value: object) -> dict:
    """
    Update a single setting in a JSON library-settings file.

    1. Attempt to read the existing JSON settings at `filename` into a
       dictionary using `json.load`. If the file does not exist, catch
       the `FileNotFoundError` and start with an empty dictionary
       instead.
    2. If `value` is `None`, REMOVE `key` from the dictionary if it is
       present (do nothing if it is already absent). Otherwise, set
       `dictionary[key] = value` (adding the key if it is new, or
       overwriting it if it already exists).
    3. Write the updated dictionary back to `filename` using
       `json.dump` with `indent=4`.
    4. Return the updated dictionary.

    :param filename: str, path to the JSON file to read/update
    :param key: str, the setting key to set or remove
    :param value: the value to assign to `key`, or `None` to remove it
    :return: dict, the updated settings dictionary
    """
    # TODO: Implement this function
    pass


def main():
    """
    A small console driver so you can manually exercise the functions
    above. This function is not graded, but is a useful way to try out
    your implementations interactively. Otherwise, just run the test
    suite.
    """
    append_checkout_record("checkout_log.txt", "alice", "Dune")
    append_checkout_record("checkout_log.txt", "bob", "1984")
    append_checkout_record("checkout_log.txt", "alice", "1984")
    print("Checkout log updated.")

    counts = load_checkout_counts("checkout_log.txt")
    print(f"Checkout counts: {counts}")

    missing_counts = load_checkout_counts("missing_log.txt")
    print(f"Missing log counts: {missing_counts}")

    status = close_out_session("checkout_log.txt", "")
    print(status)

    catalog = [("Dune", 4), ("1984", 0), ("Hamlet", 2), ("bad_entry", "N/A")]
    export_catalog_to_csv("catalog.csv", catalog)

    available = import_available_titles("catalog.csv", 1)
    print(f"Available titles: {available}")

    update_library_settings("settings.json", "theme", "dark")
    settings = update_library_settings("settings.json", "max_checkouts", 5)
    print(f"Updated settings: {settings}")


if __name__ == "__main__":
    main()
