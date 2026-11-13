"""
CS 218 - Intermediate Python
Programming Assignment 2: Advanced Data Collections

Unit tests for inventory_management.py

These tests are used to autograde the assignment via GitHub Actions.
Run them locally with:

    pytest test_inventory_management.py -v

You should not need to modify this file.
"""
try:
    import pytest
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])
    import pytest

import inventory_management as im


class TestTallyScannedItems:
    def test_basic_case(self):
        result = im.tally_scanned_items(["box", "pallet", "box", "box", "crate"])
        assert result == {"box": 3, "pallet": 1, "crate": 1}

    def test_returns_a_dict(self):
        result = im.tally_scanned_items(["item"])
        assert isinstance(result, dict)

    def test_empty_log(self):
        result = im.tally_scanned_items([])
        assert result == {}

    def test_all_unique(self):
        result = im.tally_scanned_items(["a", "b", "c"])
        assert result == {"a": 1, "b": 1, "c": 1}


class TestMergeDepartmentBudgets:
    def test_basic_case(self):
        result = im.merge_department_budgets({"Sales": 1000.0, "IT": 500.0}, {"IT": 250.5, "HR": 300.0})
        assert result == {"Sales": 1000.0, "IT": 750.5, "HR": 300.0}

    def test_returns_a_dict(self):
        result = im.merge_department_budgets({"A": 1.0}, {"B": 2.0})
        assert isinstance(result, dict)

    def test_no_overlap(self):
        result = im.merge_department_budgets({"A": 1.0}, {"B": 2.0})
        assert result == {"A": 1.0, "B": 2.0}

    def test_both_empty(self):
        result = im.merge_department_budgets({}, {})
        assert result == {}

    def test_rounding(self):
        result = im.merge_department_budgets({"A": 1.111}, {"A": 2.222})
        assert result == {"A": 3.33}


class TestFilterLowStock:
    def test_basic_case(self):
        result = im.filter_low_stock({"bolts": 5, "screws": 50, "nails": 3}, 10)
        assert result == ["bolts", "nails"]

    def test_returns_a_list(self):
        result = im.filter_low_stock({"a": 1}, 10)
        assert isinstance(result, list)

    def test_none_below_threshold(self):
        result = im.filter_low_stock({"a": 100, "b": 200}, 10)
        assert result == []

    def test_strictly_less_than(self):
        result = im.filter_low_stock({"a": 10}, 10)
        assert result == []

    def test_empty_inventory(self):
        result = im.filter_low_stock({}, 10)
        assert result == []


class TestConvertMetersToFeet:
    def test_basic_case(self):
        result = im.convert_meters_to_feet([1.0, 10.0])
        assert result == [3.28, 32.81]

    def test_returns_a_list(self):
        result = im.convert_meters_to_feet([1.0])
        assert isinstance(result, list)

    def test_empty_list(self):
        result = im.convert_meters_to_feet([])
        assert result == []

    def test_zero_distance(self):
        result = im.convert_meters_to_feet([0.0])
        assert result == [0.0]


class TestLabelBatchSizes:
    def test_basic_case(self):
        result = im.label_batch_sizes([10, 75, 49, 50])
        assert result == ["Small", "Large", "Small", "Large"]

    def test_returns_a_list(self):
        result = im.label_batch_sizes([10])
        assert isinstance(result, list)

    def test_empty_list(self):
        result = im.label_batch_sizes([])
        assert result == []

    def test_boundary_value_is_large(self):
        result = im.label_batch_sizes([50])
        assert result == ["Large"]


class TestExtractUniqueEmailDomains:
    def test_basic_case(self):
        result = im.extract_unique_email_domains(["Alice@Warehouse.com", "bob@shipping.com", "carl@WAREHOUSE.com"])
        assert result == {"warehouse.com", "shipping.com"}

    def test_returns_a_set(self):
        result = im.extract_unique_email_domains(["a@b.com"])
        assert isinstance(result, set)

    def test_empty_list(self):
        result = im.extract_unique_email_domains([])
        assert result == set()

    def test_all_same_domain(self):
        result = im.extract_unique_email_domains(["a@x.com", "b@x.com"])
        assert result == {"x.com"}


class TestBucketAgesByGroup:
    def test_basic_case(self):
        result = im.bucket_ages_by_group([8, 15, 42, 70])
        assert result == {8: "Child", 15: "Teen", 42: "Adult", 70: "Senior"}

    def test_returns_a_dict(self):
        result = im.bucket_ages_by_group([10])
        assert isinstance(result, dict)

    def test_boundary_values(self):
        result = im.bucket_ages_by_group([12, 13, 19, 20, 64, 65])
        assert result == {12: "Child", 13: "Teen", 19: "Teen", 20: "Adult", 64: "Adult", 65: "Senior"}

    def test_empty_list(self):
        result = im.bucket_ages_by_group([])
        assert result == {}


class TestEmployeeRecord:
    def test_fields_accessible_by_name(self):
        emp = im.Employee("E1", "Ada Lovelace", 20.0)
        assert emp.emp_id == "E1"
        assert emp.name == "Ada Lovelace"
        assert emp.hourly_rate == 20.0

    def test_equality(self):
        e1 = im.Employee("E1", "Ada Lovelace", 20.0)
        e2 = im.Employee("E1", "Ada Lovelace", 20.0)
        assert e1 == e2


class TestCalculateGrossPay:
    def test_basic_case(self):
        employees = [im.Employee("E1", "Ada", 20.0), im.Employee("E2", "Grace", 25.0)]
        result = im.calculate_gross_pay(employees, {"E1": 10.0, "E2": 8.0})
        assert result == {"E1": 200.0, "E2": 200.0}

    def test_returns_a_dict(self):
        employees = [im.Employee("E1", "Ada", 20.0)]
        result = im.calculate_gross_pay(employees, {"E1": 1.0})
        assert isinstance(result, dict)

    def test_missing_hours_defaults_to_zero(self):
        employees = [im.Employee("E1", "Ada", 20.0), im.Employee("E2", "Grace", 25.0)]
        result = im.calculate_gross_pay(employees, {"E1": 10.0})
        assert result == {"E1": 200.0, "E2": 0.0}

    def test_empty_employee_list(self):
        result = im.calculate_gross_pay([], {"E1": 10.0})
        assert result == {}

    def test_rounding(self):
        employees = [im.Employee("E1", "Ada", 19.995)]
        result = im.calculate_gross_pay(employees, {"E1": 2.0})
        assert result == {"E1": 39.99}


if __name__ == "__main__":
    pytest.main(["-v", __file__])
