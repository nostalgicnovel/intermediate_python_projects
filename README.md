# Programming Assignment 3 - File IO and Exception Handling

## Assignment Overview

In this assignment, you will practice reading, writing, and appending
text files, CSV files, and JSON files, along with handling exceptions
using `try`/`except`/`finally`. Each exercise is implemented as a
single function that you must complete inside `library_records.py`.
The exercises are framed around a small library checkout and catalog
scenario: appending checkout records to a text log, tallying up how
many books each member has checked out, safely closing out a session
so that a summary line is always recorded, exporting and importing a
book catalog to/from a CSV file, and reading/updating a JSON settings
file.


## Learning Objectives

By the end of this assignment, you should be able to:

- Read from and write to plain text files using a context manager
  (`with open(...) as f:`), including opening a file in **append**
  mode (`"a"`) so that new content is added without erasing what came
  before.
- Read from and write to CSV files using the `csv` module
  (`csv.DictWriter`, `csv.DictReader`).
- Read from and write to JSON files using the `json` module
  (`json.load`, `json.dump`).
- Use `try`/`except` to catch specific exceptions such as
  `FileNotFoundError` and `ValueError`, and recover from them instead
  of crashing.
- Use `try`/`except`/`finally` together so that a piece of code
  (such as writing a final log entry) always runs, whether or not an
  error occurred.
- Raise your own exceptions (`raise ValueError(...)`) to signal
  invalid data.
- Write and test small, self-contained functions with clear inputs and
  outputs.
- Use `pytest` to run a suite of unit tests against your own code.


## Assignment Structure

This assignment is split across a few files: a starter file containing
function stubs for you to complete, a test file used to automatically
grade your work, and supporting configuration for running the tests
both locally and on GitHub Actions.


### Directory Structure

```
218-pa-3/
├── README.md
├── requirements.txt
├── library_records.py
├── test_library_records.py
└── .github
    └── workflows
        └── classroom.yml
```


## Functions to Implement

All of the functions below live in `library_records.py`. Do not change
any function names or parameter lists -- the autograder depends on
these exact signatures. Read each item's docstring carefully for the
exact expected behavior and return type.

| Function | Description |
| --- | --- |
| `append_checkout_record(filename, member, title)` | **Append** a single "member\|title" line to a text log file without erasing previous entries. |
| `load_checkout_counts(filename)` | Return a **dict** tallying how many books each member has checked out, handling a missing file and malformed lines. |
| `close_out_session(filename, final_note)` | Using `try`/`except`/`finally`, append a note (validating it isn't empty) and **always** append a closing "SESSION END" line, returning a status message. |
| `export_catalog_to_csv(filename, catalog)` | Write a list of `(title, copies_available)` tuples to a CSV file (using `csv.DictWriter`) with `"title"`/`"copies_available"` headers. |
| `import_available_titles(filename, min_copies)` | Return a **sorted list** of titles from a CSV file with at least `min_copies` copies available. |
| `update_library_settings(filename, key, value)` | Update (or, if `value` is `None`, remove) a key in a JSON settings file (creating it if missing) and return the updated **dict**. |


## Testing and Performance Analysis

Your implementations are checked with `test_library_records.py`, a
suite of `pytest` unit tests covering every function listed above,
including typical inputs, edge cases (missing files, malformed or
invalid data, boundary values), and checks on the returned data type
(e.g., making sure a function returns a `list` and not `None`). The
tests use temporary files (via pytest's `tmp_path` fixture) so that
running them will not create or overwrite any files in your project
directory.

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

3. Open `library_records.py` and complete each function marked
   with a `# TODO` comment.
4. Run the program directly to try it out interactively:

   ```
   python library_records.py
   ```

5. Run the automated test suite to check your work:

   ```
   pytest test_library_records.py -v
   ```


## Expected Output

When you run the test suite with `pytest test_library_records.py -v`,
it will print one line per test case, showing the test's name followed
by `PASSED` or `FAILED`. Tests are grouped by the function they check,
so a failing test's name (for example
`TestCloseOutSession::test_session_end_always_written_on_failure`)
tells you exactly which function and which scenario is not yet working
correctly. When every function has been implemented correctly, all
tests should report `PASSED`, and pytest will print a final summary
line such as `37 passed in 0.07s`.
