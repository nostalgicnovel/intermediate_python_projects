"""
CS 218 - Intermediate Python
Programming Assignment 1: Simple Data Collections

In this assignment, you will practice working with Python's core data
collections: lists, tuples, and sets. You will also review console I/O,
variables/arithmetic, conditionals, loops, strings, and functions.

Complete each function below according to its docstring. Do NOT change the
function names or their parameters -- the autograder (test_data_collections.py)
depends on these exact signatures.

You may add helper functions of your own if you would like, but every
function listed in the README's "Functions to Implement" section must be
completed for the tests to pass.
"""


def get_unique_words(text: str) -> set[str]:
    """
    Given a string of text, return a set containing every unique word in
    the text, converted to lowercase. Words are separated by whitespace.

    Example:
        get_unique_words("The cat sat on the mat") ->
            {"the", "cat", "sat", "on", "mat"}

    :param text: str, a sentence or paragraph of text
    :return: set of str, the unique lowercase words in the text
    """
    # TODO: Implement this function
    pass


def count_word_frequencies(words: list[str]) -> list[tuple[str, int]]:
    """
    Given a list of words, return a list of (word, count) tuples, where
    each tuple gives a word from the list and the number of times it
    appears in the list. Each word should appear only once in the
    result, in the order it first appears in the original list.

    Example:
        count_word_frequencies(["a", "b", "a", "c", "b", "a"]) ->
            [("a", 3), ("b", 2), ("c", 1)]

    :param words: list of str
    :return: list of (str, int) tuples
    """
    # TODO: Implement this function
    pass


def find_common_elements(list1: list, list2: list) -> set:
    """
    Given two lists, return a set containing the elements that appear in
    both lists (i.e., the intersection of the two lists).

    Example:
        find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) -> {3, 4}

    :param list1: list
    :param list2: list
    :return: set, the elements common to both lists
    """
    # TODO: Implement this function
    pass


def remove_duplicates_preserve_order(lst: list) -> list:
    """
    Given a list, return a new list with duplicate values removed, keeping
    only the first occurrence of each value and preserving the original
    order of the remaining elements.

    Example:
        remove_duplicates_preserve_order([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]

    :param lst: list
    :return: list with duplicates removed, order preserved
    """
    # TODO: Implement this function
    pass


def create_student_records(names: list[str], ages: list[int], grades: list[float]) -> list[tuple[str, int, float]]:
    """
    Given lists of student names, ages, and grades, return a list of tuples
    containing each student's data in the order (name, age, grade).

    Example:
        create_student_records(["Ada", "Grace"], [20, 22], [95.5, 88]) ->
            [("Ada", 20, 95.5), ("Grace", 22, 88)]

    :param names: list of str
    :param ages: list of int
    :param grades: list of float or int
    :return: list of (name, age, grade) tuples
    """
    # TODO: Implement this function
    pass


def calculate_statistics(numbers: list[float]) -> tuple[float, float, float, float]:
    """
    Given a list of numbers, return a tuple containing, in this order:
    (minimum, maximum, sum, average).

    The average should be a float. Assume the list is never empty.

    Example:
        calculate_statistics([2, 4, 6, 8]) -> (2, 8, 20, 5.0)

    :param numbers: list of int/float, guaranteed non-empty
    :return: tuple of (min, max, sum, average)
    """
    # TODO: Implement this function
    pass


def merge_sets(set1: set, set2: set) -> set:
    """
    Given two sets, return a new set that is the union of both sets
    (i.e., contains every element that appears in either set).

    Example:
        merge_sets({1, 2, 3}, {3, 4, 5}) -> {1, 2, 3, 4, 5}

    :param set1: set
    :param set2: set
    :return: set, the union of set1 and set2
    """
    # TODO: Implement this function
    pass


def filter_and_sort(numbers: list[float], threshold: float) -> list[float]:
    """
    Given a list of numbers and a threshold value, return a new list,
    sorted in ascending order, containing only the numbers that are
    strictly greater than the threshold.

    Example:
        filter_and_sort([5, 1, 9, 3, 7], 4) -> [5, 7, 9]

    :param numbers: list of int/float
    :param threshold: int/float
    :return: list of numbers greater than threshold, sorted ascending
    """
    # TODO: Implement this function
    pass


def group_by_length(words: list[str]) -> list[tuple[int, list[str]]]:
    """
    Given a list of words, return a list of (length, words_of_that_length)
    tuples, where each tuple pairs a word length (int) with a list of the
    words of that length. The tuples should be sorted in ascending order
    by length, and within each list, the words should appear in the same
    relative order as in the original list.

    Example:
        group_by_length(["a", "at", "cat", "hat", "I"]) ->
            [(1, ["a", "I"]), (2, ["at"]), (3, ["cat", "hat"])]

    :param words: list of str
    :return: list of (int, list of str) tuples, sorted by length
    """
    # TODO: Implement this function
    pass


def is_palindrome(s: str) -> bool:
    """
    Given a string, return True if it is a palindrome (reads the same
    forwards and backwards), ignoring case and spaces. Otherwise, return
    False.

    Example:
        is_palindrome("Was it a car or a cat I saw") -> True
        is_palindrome("Hello World") -> False

    :param s: str
    :return: bool, True if s is a palindrome, False otherwise
    """
    # TODO: Implement this function
    pass


def main():
    """
    A small console driver so you can manually exercise the functions
    above. This function is not graded, but is a useful way to try out
    your implementations interactively. Otherwise, just run the test suite.
    """
    sentence = input("Enter a sentence: ")
    unique_words = get_unique_words(sentence)
    print(f"Unique words: {unique_words}")

    frequencies = count_word_frequencies(sentence.lower().split())
    print(f"Word frequencies: {frequencies}")

    numbers_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [float(n) for n in numbers_input.split()]
    stats = calculate_statistics(numbers)
    print(f"Min, Max, Sum, Average: {stats}")

    palindrome_candidate = input("Enter a phrase to check for a palindrome: ")
    print(f"Is palindrome: {is_palindrome(palindrome_candidate)}")


if __name__ == "__main__":
    main()
