"""
CS 218 - Intermediate Python
Programming Assignment 6: Functional Programming

This starter module processes employee expense records using first-class
functions, lambda expressions, map, filter, reduce, any, and all.

Complete each function below according to its docstring. Do NOT change
the function names or parameter lists -- the autograder
(test_expense_reports.py) depends on these exact signatures.

You may add helper functions of your own if you would like, but every
function listed in the README's "Functions to Implement" section must
be completed for the tests to pass.

!!! NOTE: some of the expected lambda expressions are very long.
If you prefer, you may define a nested helper function instead of the lambda;
if you do, remember that lambdas CANNOT contain statements (e.g., assignment,
loops, etc.), so you should avoid using them in your helper function
to mimic the intended lambda behavior.

!!! NOTE: for the functions that expect you to use reduce(), you may find a
clearer solution using a built-in function (e.g., sum(), max()) --- if it works,
you may use it at no penalty.
"""

from functools import reduce
from dataclasses import dataclass
from collections.abc import Callable


@dataclass(frozen=True)
class Expense:
    """A single expense submitted by an employee."""
    expense_id: str
    employee: str
    category: str
    amount: float
    approved: bool


def make_amount_checker(limit: float) -> Callable[[Expense], bool]:
    """
    Return a function that tests whether an expense is over a limit.

    The returned function accepts one Expense and returns True when its
    amount is strictly greater than limit. Use a lambda expression.

    Example:
        make_amount_checker(100.0)(expense_of_150) -> True
    """
    # TODO: Implement this function
    pass


def apply_to_expenses(
    expenses: list[Expense], transform: Callable[[Expense], float]
) -> list[float]:
    """
    Apply a function to every expense and return the results in order.

    Use map() with the transform function that is passed in.
    """
    # TODO: Implement this function
    pass


def amounts_with_tax(expenses: list[Expense], tax_rate: float) -> list[float]:
    """
    Return each expense amount increased by tax_rate, rounded to 2 decimals.

    tax_rate is a fraction (0.08 means 8%). Use map() with a lambda
    expression. Order matches the input list.

    Example:
        amount 50.0 with tax_rate 0.10 -> 55.0
    """
    # TODO: Implement this function
    pass


def filter_by_category(expenses: list[Expense], category: str) -> list[Expense]:
    """
    Return only the expenses whose category equals category (exact match).

    Use filter() with a lambda expression. Preserve input order.
    """
    # TODO: Implement this function
    pass


def filter_expenses(
    expenses: list[Expense], predicate: Callable[[Expense], bool]
) -> list[Expense]:
    """
    Return the expenses for which predicate returns True, in input order.

    Use filter() with the predicate that is passed in. This function should
    work with any predicate, such as one from make_amount_checker.
    """
    # TODO: Implement this function
    pass


def sort_by_amount(expenses: list[Expense], descending: bool = False) -> list[Expense]:
    """
    Return a new list sorted by amount (ascending unless descending is True).

    Use sorted() with a lambda expression as the key. Do not modify the
    original list.
    """
    # TODO: Implement this function
    pass


def total_amount(expenses: list[Expense]) -> float:
    """
    Return the sum of all expense amounts, rounded to 2 decimals.

    Use reduce() with a lambda expression and an initial value of 0.0.
    Return 0.0 for an empty list.
    """
    # TODO: Implement this function
    pass


def largest_expense(expenses: list[Expense]) -> Expense | None:
    """
    Return the expense with the greatest amount, or None for an empty list.

    Use reduce() with a lambda expression that keeps the larger of two
    expenses. If two amounts are equal, keep the earlier expense.
    """
    # TODO: Implement this function
    pass


def total_approved_by_employee(expenses: list[Expense], employee: str) -> float:
    """
    Return the total of approved expenses belonging to employee.

    Combine filter() (with a lambda) and reduce(). Round to 2 decimals and
    return 0.0 if nothing matches.
    """
    # TODO: Implement this function
    pass


def has_unapproved_over(expenses: list[Expense], limit: float) -> bool:
    """
    Return True if at least one unapproved expense is over limit.

    Use any() with a generator expression or map(). "Over" means strictly
    greater than limit. Return False for an empty list.
    """
    # TODO: Implement this function
    pass


def all_have_category(expenses: list[Expense], allowed: set[str]) -> bool:
    """
    Return True if every expense's category is in the allowed set.

    Use all() with a generator expression or map(). Return True for an empty
    list.
    """
    # TODO: Implement this function
    pass


def approved_summaries(expenses: list[Expense]) -> list[str]:
    """
    Return one summary string for each approved expense, in input order.

    Use filter() to keep approved expenses, then map() with a lambda to
    format each one as:

        "<expense_id>: <employee> - <category> $<amount>"

    where amount has exactly 2 decimal places.

    Example:
        "E-101: Priya Nair - Travel $245.50"
    """
    # TODO: Implement this function
    pass


def main() -> None:
    """Run the functions on sample data so you can inspect their output."""
    expenses = [
        Expense("E-101", "Marlen Borer", "Travel", 245.50, True),
        Expense("E-102", "Aubree Miller", "Software", 99.99, False),
        Expense("E-103", "Marlen Borer", "Meals", 42.10, True),
        Expense("E-104", "Lane Donnelly", "Travel", 612.00, False),
        Expense("E-105", "Aubree Miller", "Equipment", 1180.25, True),
    ]

    print("Amounts with 8% tax:", amounts_with_tax(expenses, 0.08))
    print("Travel expenses:", filter_by_category(expenses, "Travel"))
    print("Total:", total_amount(expenses))
    print("Largest:", largest_expense(expenses))
    print("Unapproved over $500:", has_unapproved_over(expenses, 500.0))
    for line in approved_summaries(expenses):
        print(line)


if __name__ == "__main__":
    main()
