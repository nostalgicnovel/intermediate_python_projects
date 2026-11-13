"""
CS 218 - Intermediate Python
Programming Assignment 1: Simple Data Collections

Unit tests for data_collections.py

These tests are used to autograde the assignment via GitHub Actions.
Run them locally with:

    pytest test_data_collections.py -v

You should not need to modify this file.
"""
import math

try:
    import pytest
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])
    import pytest

import data_collections as dc


class TestGetUniqueWords:
    def test_simple_sentence(self):
        result = dc.get_unique_words("The cat sat on the mat")
        assert result == {"the", "cat", "sat", "on", "mat"}

    def test_returns_a_set(self):
        result = dc.get_unique_words("one two three")
        assert isinstance(result, set)

    def test_repeated_words(self):
        result = dc.get_unique_words("go go go team team")
        assert result == {"go", "team"}

    def test_mixed_case(self):
        result = dc.get_unique_words("Hello hello HELLO")
        assert result == {"hello"}


class TestCountWordFrequencies:
    def test_basic_counts(self):
        result = dc.count_word_frequencies(["a", "b", "a", "c", "b", "a"])
        assert result == [("a", 3), ("b", 2), ("c", 1)]

    def test_returns_a_list(self):
        result = dc.count_word_frequencies(["a", "b", "a"])
        assert isinstance(result, list)

    def test_empty_list(self):
        result = dc.count_word_frequencies([])
        assert result == []

    def test_single_word(self):
        result = dc.count_word_frequencies(["only"])
        assert result == [("only", 1)]


class TestFindCommonElements:
    def test_basic_intersection(self):
        result = dc.find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
        assert result == {3, 4}

    def test_returns_a_set(self):
        result = dc.find_common_elements([1, 2], [2, 3])
        assert isinstance(result, set)

    def test_no_overlap(self):
        result = dc.find_common_elements([1, 2], [3, 4])
        assert result == set()

    def test_with_strings(self):
        result = dc.find_common_elements(["a", "b", "c"], ["b", "c", "d"])
        assert result == {"b", "c"}


class TestRemoveDuplicatesPreserveOrder:
    def test_basic_case(self):
        result = dc.remove_duplicates_preserve_order([1, 2, 2, 3, 1, 4])
        assert result == [1, 2, 3, 4]

    def test_returns_a_list(self):
        result = dc.remove_duplicates_preserve_order([1, 1, 1])
        assert isinstance(result, list)

    def test_no_duplicates(self):
        result = dc.remove_duplicates_preserve_order([5, 6, 7])
        assert result == [5, 6, 7]

    def test_empty_list(self):
        result = dc.remove_duplicates_preserve_order([])
        assert result == []


class TestCreateStudentRecords:
    def test_multiple_records(self):
        result = dc.create_student_records(
            ["Ada", "Grace"], [20, 22], [95.5, 88]
        )
        assert result == [("Ada", 20, 95.5), ("Grace", 22, 88)]

    def test_returns_a_list(self):
        result = dc.create_student_records(["Alan"], [24], [90])
        assert isinstance(result, list)

    def test_empty_lists(self):
        result = dc.create_student_records([], [], [])
        assert result == []


class TestCalculateStatistics:
    def test_basic_stats(self):
        result = dc.calculate_statistics([2, 4, 6, 8])
        assert result == (2, 8, 20, 5.0)

    def test_returns_a_tuple(self):
        result = dc.calculate_statistics([1, 2, 3])
        assert isinstance(result, tuple)

    def test_single_element(self):
        result = dc.calculate_statistics([10])
        assert result == (10, 10, 10, 10.0)

    def test_negative_numbers(self):
        minimum, maximum, total, average = dc.calculate_statistics([-5, 0, 5])
        assert minimum == -5
        assert maximum == 5
        assert total == 0
        assert math.isclose(average, 0.0)


class TestMergeSets:
    def test_basic_union(self):
        result = dc.merge_sets({1, 2, 3}, {3, 4, 5})
        assert result == {1, 2, 3, 4, 5}

    def test_returns_a_set(self):
        result = dc.merge_sets({1}, {2})
        assert isinstance(result, set)

    def test_empty_sets(self):
        result = dc.merge_sets(set(), set())
        assert result == set()

    def test_disjoint_sets(self):
        result = dc.merge_sets({1, 2}, {3, 4})
        assert result == {1, 2, 3, 4}


class TestFilterAndSort:
    def test_basic_filter_and_sort(self):
        result = dc.filter_and_sort([5, 1, 9, 3, 7], 4)
        assert result == [5, 7, 9]

    def test_returns_a_list(self):
        result = dc.filter_and_sort([1, 2, 3], 0)
        assert isinstance(result, list)

    def test_none_above_threshold(self):
        result = dc.filter_and_sort([1, 2, 3], 10)
        assert result == []

    def test_all_above_threshold(self):
        result = dc.filter_and_sort([3, 1, 2], -1)
        assert result == [1, 2, 3]


class TestGroupByLength:
    def test_basic_grouping(self):
        result = dc.group_by_length(["a", "at", "cat", "hat", "I"])
        assert result == [(1, ["a", "I"]), (2, ["at"]), (3, ["cat", "hat"])]

    def test_returns_a_list(self):
        result = dc.group_by_length(["hi", "yo"])
        assert isinstance(result, list)

    def test_empty_list(self):
        result = dc.group_by_length([])
        assert result == []


class TestIsPalindrome:
    def test_true_palindrome_with_spaces(self):
        assert dc.is_palindrome("Was it a car or a cat I saw") is True

    def test_false_case(self):
        assert dc.is_palindrome("Hello World") is False

    def test_simple_palindrome(self):
        assert dc.is_palindrome("racecar") is True

    def test_case_insensitive(self):
        assert dc.is_palindrome("Racecar") is True

    def test_empty_string(self):
        assert dc.is_palindrome("") is True


if __name__ == "__main__":
    pytest.main(["-v", __file__])
