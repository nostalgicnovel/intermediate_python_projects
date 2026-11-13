# Programming Assignment 2 - Advanced Data Collections

## Assignment Overview

In this assignment, you will practice working with Python dictionaries and
comprehensions (list, set, and dict), including comprehensions that embed a
ternary (conditional) expression, along with a structured record built
using `dataclasses.dataclass`. Each exercise is implemented as a single
function (or, in one case, a small class) that you must complete inside
`inventory_management.py`. The exercises are framed around a small
warehouse/payroll scenario: tallying scanned items, merging department
budgets, checking stock levels, converting units, labeling batches,
extracting email domains, bucketing ages, and calculating employee pay.


## Learning Objectives

By the end of this assignment, you should be able to:

- Build and manipulate Python dictionaries, including counting, merging,
  and filtering based on values.
- Write list, set, and dict comprehensions, including comprehensions that
  embed a ternary (conditional) expression.
- Choose the appropriate collection type (dict, list, or set) for a given
  problem based on its properties.
- Define a `dataclass` with typed fields and use it to model a simple,
  mutable record.
- Write and test small, self-contained functions with clear inputs and
  outputs.
- Use `pytest` to run a suite of unit tests against your own code.


## Assignment Structure

This assignment is split across a few files: a starter file containing
function/class stubs for you to complete, a test file used to
automatically grade your work, and supporting configuration for running
the tests both locally and on GitHub Actions.


### Directory Structure

```
218-pa-2/
├── README.md
├── requirements.txt
├── inventory_management.py
├── test_inventory_management.py
└── .github
    └── workflows
        └── classroom.yml
```


## Functions to Implement

All of the functions/classes below live in `inventory_management.py`. Do
not change any function/class names, field names, or parameter lists --
the autograder depends on these exact signatures. Read each item's
docstring carefully for the exact expected behavior and return type.

| Function | Description |
| --- | --- |
| `tally_scanned_items(scan_log)` | Return a **dict** counting how many times each item name appears in a warehouse scan log. |
| `merge_department_budgets(budget1, budget2)` | Return a **dict** merging two department budgets, summing values for departments in both. |
| `filter_low_stock(inventory, min_stock)` | Return a **sorted list** of item names whose stock is strictly below `min_stock`. |
| `convert_meters_to_feet(distances_m)` | Return a **list**, built with a list comprehension, of distances converted from meters to feet. |
| `label_batch_sizes(batch_sizes)` | Return a **list**, built with a list comprehension and ternary operator, labeling each batch "Small" or "Large". |
| `extract_unique_email_domains(emails)` | Return a **set**, built with a set comprehension, of unique lowercase email domains. |
| `bucket_ages_by_group(ages)` | Return a **dict**, built with a dict comprehension, mapping each age to an age group label. |
| `Employee` | A `dataclass` with fields `emp_id` (str), `name` (str), `hourly_rate` (float). |
| `calculate_gross_pay(employees, hours_worked)` | Return a **dict** mapping each employee's `emp_id` to their gross pay. |


## Testing and Performance Analysis

Your implementations are checked with `test_inventory_management.py`, a
suite of `pytest` unit tests covering every function/class listed above,
including typical inputs, edge cases (empty inputs, boundary values), and
checks on the returned data type (e.g., making sure a function returns a
`set` and not a `list`).

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

3. Open `inventory_management.py` and complete each function/class marked
   with a `# TODO` comment.
4. Run the program directly to try it out interactively:

   ```
   python inventory_management.py
   ```

5. Run the automated test suite to check your work:

   ```
   pytest test_inventory_management.py -v
   ```


## Expected Output

When you run the test suite with `pytest test_inventory_management.py -v`,
it will print one line per test case, showing the test's name followed by
`PASSED` or `FAILED`. Tests are grouped by the function they check, so a
failing test's name (for example
`TestCalculateGrossPay::test_missing_hours_defaults_to_zero`) tells you
exactly which function and which scenario is not yet working correctly.
When every function has been implemented correctly, all tests should
report `PASSED`, and pytest will print a final summary line such as
`34 passed in 0.02s`.
