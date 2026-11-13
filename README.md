# Programming Assignment 1 - Simple Data Collections

## Assignment Overview

In this assignment, you will practice working with Python's built-in simple data
collections (lists, tuples, and sets) to solve a series of small, focused
programming exercises. Each exercise is implemented as a single function that
you must complete inside `data_collections.py`. The assignment is designed as 
an applied lab: you will not be designing a program from scratch, but instead 
filling in the logic for a set of well-defined functions using the tools you 
have learned so far (console I/O, variables/arithmetic, conditionals, loops, 
strings, and functions), together with your new knowledge of lists, tuples, and sets.


## Learning Objectives

By the end of this assignment, you should be able to:

- Create, read, and manipulate Python lists, tuples, and sets.
- Choose the appropriate collection type (list, tuple, or set) for a given
  problem based on its properties (ordering, mutability, uniqueness).
- Use loops and conditionals together with collections to solve problems
  such as counting, filtering, grouping, and de-duplicating data.
- Use set operations (union, intersection) to compare collections of data.
- Write and test small, self-contained functions with clear inputs and
  outputs.
- Use `pytest` to run a suite of unit tests against your own code.


## Assignment Structure

This assignment is split across a few files: a starter file containing
function stubs for you to complete, a test file used to automatically grade
your work, and supporting configuration for running the tests both locally
and on GitHub Actions.


### Directory Structure

```
218-pa-1/
├── README.md
├── requirements.txt
├── data_collections.py
├── test_data_collections.py
└── .github
    └── workflows
        └── classroom.yml
```


## Functions to Implement

All of the functions below live in `data_collections.py`. Do not change any
function names or parameter lists -- the autograder depends on these exact
signatures. Read each function's docstring carefully for the exact expected
behavior and return type.

| Function | Description |
| --- | --- |
| `get_unique_words(text)` | Return a **set** of the unique, lowercased words in a string. |
| `count_word_frequencies(words)` | Return a **list** of `(word, count)` tuples for how many times each word appears. |
| `find_common_elements(list1, list2)` | Return a **set** containing the elements shared by two lists. |
| `remove_duplicates_preserve_order(lst)` | Return a **list** with duplicates removed, preserving the original order. |
| `create_student_records(name, age, grade)` | Return a **list** of `(name, age, grade)` tuples. |
| `calculate_statistics(numbers)` | Return a **tuple** `(min, max, sum, average)` for a list of numbers. |
| `merge_sets(set1, set2)` | Return the union of two **sets**. |
| `filter_and_sort(numbers, threshold)` | Return a **list**, sorted ascending, of numbers greater than a threshold. |
| `group_by_length(words)` | Return a **list** of `(length, words)` tuples grouping words by length. |
| `is_palindrome(s)` | Return `True` if a string is a palindrome, ignoring case and spaces. |


## Testing and Performance Analysis

Your implementations are checked with `test_data_collections.py`, a suite of
`pytest` unit tests covering every function listed above, including typical
inputs, edge cases (empty lists/sets, single-element inputs), and checks on
the returned data type (e.g., making sure a function returns a `set` and not
a `list`).

This test suite is also used to **autograde** your submission through a
GitHub Actions workflow (`.github/workflows/classroom.yml`), which
automatically runs `pytest` every time you push your changes. You can (and
should) run the same tests locally before submitting.


## How to Run

1. Make sure you have Python 3 and `pip` installed.
2. Install the testing dependency:

   ```
   pip install -r requirements.txt
   ```

3. Open `data_collections.py` and complete each function marked with a
   `# TODO: Implement this function` comment.
4. Run the program directly to try it out interactively:

   ```
   python data_collections.py
   ```

5. Run the automated test suite to check your work:

   ```
   pytest test_data_collections.py -v
   ```


## Expected Output

When you run the test suite with `pytest test_data_collections.py -v`, it
will print one line per test case, showing the test's name followed by
`PASSED` or `FAILED`. Tests are grouped by the function they check, so a
failing test's name (for example
`TestIsPalindrome::test_case_insensitive`) tells you exactly which function
and which scenario is not yet working correctly. When every function has
been implemented correctly, all tests should report `PASSED`, and pytest
will print a final summary line such as `38 passed in 0.02s`.
