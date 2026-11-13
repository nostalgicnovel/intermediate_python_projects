# Programming Assignment 6 - Functional Programming

## Assignment Overview

In this assignment, you will use functional programming techniques to process
employee expense reports. Each expense records an ID, an employee, a category,
an amount, and whether it has been approved. Finance staff regularly need to
total expenses, find large or unapproved items, apply tax rates, and produce
short summaries for review.

Complete the functions in `expense_reports.py`. You will write functions that
return other functions, pass functions as arguments, and use lambda
expressions with `map`, `filter`, `sorted`, `reduce`, `any`, and `all`. This is
an applied lab, not a program-design project: use the supplied signatures and
complete the functions marked with `TODO`. Do not change required function
names or parameter lists because the tests depend on them.

## Learning Objectives

By the end of this assignment, you should be able to:

- Treat functions as first-class values by storing, passing, and returning them.
- Write a higher-order function that returns a new function.
- Write a higher-order function that accepts a function as an argument.
- Use lambda expressions for short, single-purpose operations.
- Transform sequences with `map()` and select items with `filter()`.
- Convert lazy `map` and `filter` results into lists.
- Sort with `sorted()` and a lambda `key`.
- Combine a sequence into one value with `functools.reduce()`.
- Use `any()` and `all()` to test conditions across a collection.
- Chain `filter()` and `map()` into a small processing pipeline.
- Write and run `pytest` tests for small functions.

## Assignment Structure

The assignment includes a starter module with an `Expense` dataclass and
function stubs, a pytest file that checks the required behavior, and a GitHub
Actions workflow that runs the tests for autograding. All assignment code and
test data use Python; no external data files or services are needed.

### Directory Structure

```
218-pa-6/
├── README.md
├── .gitignore
├── requirements.txt
├── expense_reports.py
├── test_expense_reports.py
└── .github
    └── workflows
        └── classroom.yml
```

## Functions to Implement

Complete the functions in `expense_reports.py`. Keep each required name and
parameter list unchanged. The `Expense` dataclass is provided. The docstrings
in the starter module are the authoritative reference for exact formatting and
return values. Do not use explicit `for` or `while` loops in these functions.

| Function | Description |
| --- | --- |
| `make_amount_checker(limit)` | Return a lambda that tests whether an expense's amount is strictly greater than `limit`. |
| `apply_to_expenses(expenses, transform)` | Use `map()` to apply the given function to every expense and return a list of results. |
| `amounts_with_tax(expenses, tax_rate)` | Use `map()` and a lambda to return each amount plus tax, rounded to 2 decimals. |
| `filter_by_category(expenses, category)` | Use `filter()` and a lambda to keep expenses with an exactly matching category. |
| `filter_expenses(expenses, predicate)` | Use `filter()` with a caller-supplied predicate, such as one from `make_amount_checker`. |
| `sort_by_amount(expenses, descending=False)` | Return a new list sorted by amount using `sorted()` and a lambda key. |
| `total_amount(expenses)` | Use `reduce()` to sum amounts, rounded to 2 decimals; return `0.0` for an empty list. |
| `largest_expense(expenses)` | Use `reduce()` to find the largest expense (earlier wins ties); return `None` for an empty list. |
| `total_approved_by_employee(expenses, employee)` | Combine `filter()` and `reduce()` to total one employee's approved expenses. |
| `has_unapproved_over(expenses, limit)` | Use `any()` to test whether any unapproved expense is over `limit`. |
| `all_have_category(expenses, allowed)` | Use `all()` to test whether every category is in the allowed set. |
| `approved_summaries(expenses)` | Use `filter()` and `map()` to build summary strings for approved expenses. |

## Testing and Performance Analysis

Your implementation is checked with `test_expense_reports.py`, a suite of
`pytest` unit tests covering every required function. The tests check that:

- Returned functions are callable, apply the correct comparison, and keep their
  own limit values.
- Functions passed as arguments are applied correctly, including named
  functions and lambdas.
- Results are returned as lists in the original order, with the required
  rounding.
- Filtering handles exact matches, no matches, and the original objects.
- Sorting works in both directions and does not modify the input list.
- Reduction handles totals, rounding, ties, and empty lists.
- `any()` and `all()` behavior is correct for boundary values and empty lists.
- Summary strings use the required format.

The tests are also run by `.github/workflows/classroom.yml` for GitHub Actions
autograding. They use in-memory data, so running pytest does not create or
modify files. Each function makes a single pass over its input (sorting takes
O(n log n) time), and `map()` and `filter()` are lazy, so they produce items
only as they are consumed.

## How to Run

1. Make sure Python 3.12 or later and `pip` are installed.
2. From this directory, install the testing dependency:

   ```
   pip install -r requirements.txt
   ```

3. Open `expense_reports.py` and complete each function marked with
   `# TODO: Implement this function`.
4. Optionally run the sample program to inspect the output:

   ```
   python expense_reports.py
   ```

5. Run the automated test suite:

   ```
   pytest test_expense_reports.py -v
   ```

## Expected Output

When you run `pytest test_expense_reports.py -v`, pytest displays one line for
each test, including its test name and a `PASSED` or `FAILED` result. The tests
are grouped by topic (`TestFirstClassFunctions`, `TestMapAndFilter`,
`TestReduce`, and `TestAnyAllAndPipelines`), so a failure name (for example,
`TestReduce::test_largest_expense_tie_keeps_earlier`) identifies the behavior
that needs attention. When all required behavior is implemented correctly, all
tests report `PASSED`, followed by a summary with the total number of passed
tests and the test run time.
