"""
CS 218 - Intermediate Python
Programming Assignment 6: Functional Programming

Unit tests for expense_reports.py. These tests are used for GitHub Actions
autograding. Run them locally with:

    pytest test_expense_reports.py -v
"""


try:
    import pytest
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])
    import pytest

import expense_reports as er


@pytest.fixture
def expenses():
    return [
        er.Expense("E-101", "Marlen Borer", "Travel", 245.50, True),
        er.Expense("E-102", "Aubree Miller", "Software", 99.99, False),
        er.Expense("E-103", "Marlen Borer", "Meals", 42.10, True),
        er.Expense("E-104", "Lane Donnelly", "Travel", 612.00, False),
        er.Expense("E-105", "Aubree Miller", "Equipment", 1180.25, True),
    ]


def ids(items):
    return [e.expense_id for e in items]


class TestFirstClassFunctions:
    def test_checker_returns_callable(self):
        assert callable(er.make_amount_checker(100.0))

    def test_checker_over_limit(self, expenses):
        check = er.make_amount_checker(100.0)
        assert check(expenses[0]) is True
        assert check(expenses[1]) is False

    def test_checker_boundary_is_strict(self):
        e = er.Expense("E-1", "A", "Meals", 100.0, True)
        assert er.make_amount_checker(100.0)(e) is False

    def test_checkers_keep_their_own_limit(self, expenses):
        low = er.make_amount_checker(50.0)
        high = er.make_amount_checker(1000.0)
        assert low(expenses[0]) is True
        assert high(expenses[0]) is False

    def test_apply_to_expenses_with_function(self, expenses):
        assert er.apply_to_expenses(expenses, lambda e: e.amount) == [
            245.50, 99.99, 42.10, 612.00, 1180.25
        ]

    def test_apply_to_expenses_with_named_function(self, expenses):
        def double(e):
            return e.amount * 2

        assert er.apply_to_expenses(expenses[:2], double) == [491.0, 199.98]

    def test_apply_to_expenses_returns_list(self, expenses):
        assert isinstance(er.apply_to_expenses(expenses, lambda e: 1.0), list)

    def test_apply_to_expenses_empty(self):
        assert er.apply_to_expenses([], lambda e: e.amount) == []


class TestMapAndFilter:
    def test_amounts_with_tax(self, expenses):
        assert er.amounts_with_tax(expenses, 0.10) == [
            270.05, 109.99, 46.31, 673.2, 1298.28
        ]

    def test_amounts_with_zero_tax(self, expenses):
        assert er.amounts_with_tax(expenses, 0.0) == [
            245.50, 99.99, 42.10, 612.00, 1180.25
        ]

    def test_amounts_with_tax_empty(self):
        assert er.amounts_with_tax([], 0.08) == []

    def test_amounts_with_tax_returns_list(self, expenses):
        assert isinstance(er.amounts_with_tax(expenses, 0.05), list)

    def test_filter_by_category(self, expenses):
        assert ids(er.filter_by_category(expenses, "Travel")) == ["E-101", "E-104"]

    def test_filter_by_category_no_match(self, expenses):
        assert er.filter_by_category(expenses, "Lodging") == []

    def test_filter_by_category_exact_match(self, expenses):
        assert er.filter_by_category(expenses, "travel") == []

    def test_filter_by_category_returns_same_objects(self, expenses):
        assert er.filter_by_category(expenses, "Meals")[0] is expenses[2]

    def test_filter_expenses_with_checker(self, expenses):
        result = er.filter_expenses(expenses, er.make_amount_checker(200.0))
        assert ids(result) == ["E-101", "E-104", "E-105"]

    def test_filter_expenses_with_lambda(self, expenses):
        result = er.filter_expenses(expenses, lambda e: not e.approved)
        assert ids(result) == ["E-102", "E-104"]

    def test_filter_expenses_empty(self):
        assert er.filter_expenses([], lambda e: True) == []

    def test_sort_by_amount_ascending(self, expenses):
        assert ids(er.sort_by_amount(expenses)) == [
            "E-103", "E-102", "E-101", "E-104", "E-105"
        ]

    def test_sort_by_amount_descending(self, expenses):
        assert ids(er.sort_by_amount(expenses, descending=True)) == [
            "E-105", "E-104", "E-101", "E-102", "E-103"
        ]

    def test_sort_does_not_modify_original(self, expenses):
        original = list(expenses)
        er.sort_by_amount(expenses)
        assert expenses == original

    def test_sort_empty(self):
        assert er.sort_by_amount([]) == []


class TestReduce:
    def test_total_amount(self, expenses):
        assert er.total_amount(expenses) == 2179.84

    def test_total_amount_rounds(self):
        items = [
            er.Expense("E-1", "A", "Meals", 0.1, True),
            er.Expense("E-2", "A", "Meals", 0.2, True),
        ]
        assert er.total_amount(items) == 0.3

    def test_total_amount_empty(self):
        assert er.total_amount([]) == 0.0

    def test_largest_expense(self, expenses):
        assert er.largest_expense(expenses) is expenses[4]

    def test_largest_expense_single(self, expenses):
        assert er.largest_expense(expenses[:1]) is expenses[0]

    def test_largest_expense_tie_keeps_earlier(self):
        a = er.Expense("E-1", "A", "Meals", 50.0, True)
        b = er.Expense("E-2", "B", "Meals", 50.0, True)
        assert er.largest_expense([a, b]) is a

    def test_largest_expense_empty(self):
        assert er.largest_expense([]) is None

    def test_total_approved_by_employee(self, expenses):
        assert er.total_approved_by_employee(expenses, "Marlen Borer") == 287.6

    def test_total_approved_excludes_unapproved(self, expenses):
        assert er.total_approved_by_employee(expenses, "Aubree Miller") == 1180.25

    def test_total_approved_no_approved(self, expenses):
        assert er.total_approved_by_employee(expenses, "Lane Donnelly") == 0.0

    def test_total_approved_unknown_employee(self, expenses):
        assert er.total_approved_by_employee(expenses, "Nobody") == 0.0


class TestAnyAllAndPipelines:
    def test_has_unapproved_over_true(self, expenses):
        assert er.has_unapproved_over(expenses, 500.0) is True

    def test_has_unapproved_over_ignores_approved(self, expenses):
        assert er.has_unapproved_over(expenses, 700.0) is False

    def test_has_unapproved_over_strict(self, expenses):
        assert er.has_unapproved_over(expenses, 612.0) is False

    def test_has_unapproved_over_empty(self):
        assert er.has_unapproved_over([], 0.0) is False

    def test_all_have_category_true(self, expenses):
        allowed = {"Travel", "Software", "Meals", "Equipment"}
        assert er.all_have_category(expenses, allowed) is True

    def test_all_have_category_false(self, expenses):
        assert er.all_have_category(expenses, {"Travel", "Meals"}) is False

    def test_all_have_category_empty(self):
        assert er.all_have_category([], set()) is True

    def test_approved_summaries(self, expenses):
        assert er.approved_summaries(expenses) == [
            "E-101: Marlen Borer - Travel $245.50",
            "E-103: Marlen Borer - Meals $42.10",
            "E-105: Aubree Miller - Equipment $1180.25",
        ]

    def test_approved_summaries_two_decimals(self):
        item = er.Expense("E-9", "A B", "Meals", 12.0, True)
        assert er.approved_summaries([item]) == ["E-9: A B - Meals $12.00"]

    def test_approved_summaries_none_approved(self, expenses):
        assert er.approved_summaries(expenses[1:2]) == []

    def test_approved_summaries_empty(self):
        assert er.approved_summaries([]) == []


if __name__ == "__main__":
    pytest.main(["-v", __file__])
