"""
CS 218 - Intermediate Python
Programming Assignment 2: Advanced Data Collections

In this assignment, you will practice working with Python dictionaries,
comprehensions (list, set, and dict), and a structured record built with
`dataclasses.dataclass`, applied to a small warehouse/payroll scenario.

Complete each function below according to its docstring. Do NOT change the
function names, class fields, or parameter lists -- the autograder
(test_inventory_management.py) depends on these exact signatures.

You may add helper functions of your own if you would like, but every
function/class listed in the README's "Functions to Implement" section
must be completed for the tests to pass.
"""
from dataclasses import dataclass


def tally_scanned_items(scan_log: list[str]) -> dict[str, int]:
    """
    A warehouse scanner records an entry every time an item is scanned in
    or out of the building. Given a list of item names representing this
    scan log, return a dictionary mapping each unique item name to the
    number of times it appears in the log.

    Example:
        tally_scanned_items(["box", "pallet", "box", "box", "crate"]) ->
            {"box": 3, "pallet": 1, "crate": 1}

    :param scan_log: list of str, item names in the order they were scanned
    :return: dict mapping each item name to its scan count
    """
    # TODO: Implement this function
    pass


def merge_department_budgets(budget1: dict[str, float], budget2: dict[str, float]) -> dict[str, float]:
    """
    Given two dictionaries mapping department names to float budgets,
    return a new dictionary containing every department that appears in
    either dictionary. If a department appears in BOTH dictionaries, its
    value in the result should be the SUM of the two budgets, rounded to
    2 decimal places. Departments that appear in only one dictionary keep
    their original value (also rounded to 2 decimal places).

    Example:
        merge_department_budgets({"Sales": 1000.0, "IT": 500.0},
                                  {"IT": 250.5, "HR": 300.0}) ->
            {"Sales": 1000.0, "IT": 750.5, "HR": 300.0}

    :param budget1: dict of str to float
    :param budget2: dict of str to float
    :return: new dict of str to float, merged budgets
    """
    # TODO: Implement this function
    pass


def filter_low_stock(inventory: dict[str, int], min_stock: int) -> list[str]:
    """
    Given a dictionary mapping item names to integer stock counts, and a
    minimum stock threshold, return a list, sorted alphabetically in
    ascending order, of item names whose stock count is strictly LESS
    THAN min_stock.
    
    Hint: You can use .sort() or sorted() to easily sort a list.
    Both functions can also take "key=str.lower" to sort case-insensitively.

    Example:
        filter_low_stock({"bolts": 5, "screws": 50, "nails": 3}, 10) ->
            ["bolts", "nails"]

    :param inventory: dict of str to int
    :param min_stock: int, the minimum acceptable stock level
    :return: sorted list of str, item names below the threshold
    """
    # TODO: Implement this function
    pass


def convert_meters_to_feet(distances_m: list[float]) -> list[float]:
    """
    Given a list of distances in meters, use a single list comprehension
    (with no `if` conditions or ternary expressions) to convert each
    distance to feet using the formula: feet = meters * 3.28084.
    Round each resulting value to 2 decimal places.

    Example:
        convert_meters_to_feet([1.0, 10.0]) -> [3.28, 32.81]

    :param distances_m: list of float, distances in meters
    :return: list of float, distances in feet rounded to 2 decimal places
    """
    # TODO: Implement this function
    pass


def label_batch_sizes(batch_sizes: list[int]) -> list[str]:
    """
    Given a list of integer batch sizes, use a single list comprehension
    with an embedded **ternary operator** to label each batch: "Small" if
    the size is strictly less than 50, otherwise "Large".

    Example:
        label_batch_sizes([10, 75, 49, 50]) ->
            ["Small", "Large", "Small", "Large"]

    :param batch_sizes: list of int
    :return: list of str, either "Small" or "Large" for each batch size
    """
    # TODO: Implement this function
    pass


def extract_unique_email_domains(emails: list[str]) -> set[str]:
    """
    Given a list of email address strings, use a single **set
    comprehension** to extract the lowercase domain portion (everything
    after the '@' symbol) of each email, returning only the unique
    domains.
    
    Hint: you can use .split() to split a string into parts based on a delimiter.

    Example:
        extract_unique_email_domains(
            ["Alice@Warehouse.com", "bob@shipping.com", "carl@WAREHOUSE.com"]
        ) -> {"warehouse.com", "shipping.com"}

    :param emails: list of str, email addresses
    :return: set of str, unique lowercase domains
    """
    # TODO: Implement this function
    pass


def bucket_ages_by_group(ages: list[int]) -> dict[int, str]:
    """
    Given a list of integer ages, use a single **dict comprehension** to
    map each age to an age group label using the following scale:
    - "Child" for ages strictly less than 13
    - "Teen" for ages 13-19
    - "Adult" for ages 20-64
    - "Senior" for ages 65 and up
    
    Hint: this is very similar to the letter grade example we did in class.

    Example:
        bucket_ages_by_group([8, 15, 42, 70]) ->
            {8: "Child", 15: "Teen", 42: "Adult", 70: "Senior"}

    :param ages: list of int
    :return: dict mapping each age to its age group label
    """
    # TODO: Implement this function
    pass


# TODO: Define a dataclass called 'Employee' with fields
# emp_id (str), name (str), and hourly_rate (float)
class Employee:
    ...


def calculate_gross_pay(employees: list[Employee], hours_worked: dict[str, float]) -> dict[str, float]:
    """
    Given a list of Employee records and a dictionary mapping employee IDs
    (emp_id) to the number of hours they worked, return a dictionary
    mapping each employee's emp_id to their gross pay
    (hourly_rate * hours worked), rounded to 2 decimal places. If an
    employee's emp_id does not appear in hours_worked, treat their hours
    worked as 0.

    Example:
        employees = [Employee("E1", "Ada", 20.0), Employee("E2", "Grace", 25.0)]
        calculate_gross_pay(employees, {"E1": 10.0}) ->
            {"E1": 200.0, "E2": 0.0}

    :param employees: list of Employee dataclass instances
    :param hours_worked: dict mapping emp_id (str) to hours worked (float)
    :return: dict mapping emp_id (str) to gross pay (float)
    """
    # TODO: Implement this function
    pass


def main():
    """
    A small console driver so you can manually exercise the functions
    above. This function is not graded, but is a useful way to try out
    your implementations interactively. Otherwise, just run the test suite.
    """
    scan_input = input("Enter a warehouse scan log (item names separated by spaces): ")
    print(f"Scan tallies: {tally_scanned_items(scan_input.split())}")

    stock_item = input("Enter an item name to check for low stock: ")
    stock_count = int(input(f"Enter the current stock count for {stock_item}: "))
    threshold = int(input("Enter the minimum acceptable stock level: "))
    print(f"Low stock: {filter_low_stock({stock_item: stock_count}, threshold)}")

    distances_input = input("Enter a list of distances in meters separated by spaces: ")
    distances = [float(d) for d in distances_input.split()]
    print(f"Distances in feet: {convert_meters_to_feet(distances)}")

    employees = [
        Employee("E1", "Ada Lovelace", 22.50),
        Employee("E2", "Grace Hopper", 27.00),
    ]
    hours_worked = {"E1": 40.0, "E2": 35.5}
    print(f"Gross pay: {calculate_gross_pay(employees, hours_worked)}")


if __name__ == "__main__":
    main()
