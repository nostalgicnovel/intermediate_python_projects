"""
CS 218 - Intermediate Python
Programming Assignment 3: File I/O and Exception Handling

Unit tests for library_records.py

These tests are used to autograde the assignment via GitHub Actions.
Run them locally with:

    pytest test_library_records.py -v

You should not need to modify this file.
"""
import csv
import json

try:
    import pytest
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])
    import pytest

import library_records as lr


class TestAppendCheckoutRecord:
    def test_creates_file(self, tmp_path):
        target = tmp_path / "log.txt"
        lr.append_checkout_record(str(target), "alice", "Dune")
        assert target.exists()

    def test_writes_expected_line(self, tmp_path):
        target = tmp_path / "log.txt"
        lr.append_checkout_record(str(target), "alice", "Dune")
        with open(target, "r") as f:
            lines = f.read().splitlines()
        assert lines == ["alice|Dune"]

    def test_appends_without_overwriting(self, tmp_path):
        target = tmp_path / "log.txt"
        lr.append_checkout_record(str(target), "alice", "Dune")
        lr.append_checkout_record(str(target), "bob", "1984")
        with open(target, "r") as f:
            lines = f.read().splitlines()
        assert lines == ["alice|Dune", "bob|1984"]

    def test_multiple_records_same_member(self, tmp_path):
        target = tmp_path / "log.txt"
        lr.append_checkout_record(str(target), "alice", "Dune")
        lr.append_checkout_record(str(target), "alice", "1984")
        with open(target, "r") as f:
            lines = f.read().splitlines()
        assert lines == ["alice|Dune", "alice|1984"]


class TestLoadCheckoutCounts:
    def test_basic_case(self, tmp_path):
        target = tmp_path / "log.txt"
        target.write_text("alice|Dune\nbob|1984\nalice|1984\n")
        result = lr.load_checkout_counts(str(target))
        assert result == {"alice": 2, "bob": 1}

    def test_returns_a_dict(self, tmp_path):
        target = tmp_path / "log.txt"
        target.write_text("alice|Dune\n")
        result = lr.load_checkout_counts(str(target))
        assert isinstance(result, dict)

    def test_missing_file_returns_empty_dict(self, tmp_path):
        target = tmp_path / "does_not_exist.txt"
        result = lr.load_checkout_counts(str(target))
        assert result == {}

    def test_skips_malformed_lines(self, tmp_path):
        target = tmp_path / "log.txt"
        target.write_text("alice|Dune\nthis line has no separator\nbob|1984\n")
        result = lr.load_checkout_counts(str(target))
        assert result == {"alice": 1, "bob": 1}

    def test_skips_lines_with_too_many_separators(self, tmp_path):
        target = tmp_path / "log.txt"
        target.write_text("alice|Dune|extra\nbob|1984\n")
        result = lr.load_checkout_counts(str(target))
        assert result == {"bob": 1}

    def test_empty_file_returns_empty_dict(self, tmp_path):
        target = tmp_path / "log.txt"
        target.write_text("")
        result = lr.load_checkout_counts(str(target))
        assert result == {}


class TestCloseOutSession:
    def test_returns_normal_status_for_valid_note(self, tmp_path):
        target = tmp_path / "log.txt"
        result = lr.close_out_session(str(target), "All books returned.")
        assert result == "Session closed normally."

    def test_returns_warning_status_for_empty_note(self, tmp_path):
        target = tmp_path / "log.txt"
        result = lr.close_out_session(str(target), "")
        assert result == "Session closed with warning: Final note cannot be empty."

    def test_returns_warning_status_for_whitespace_note(self, tmp_path):
        target = tmp_path / "log.txt"
        result = lr.close_out_session(str(target), "   ")
        assert result == "Session closed with warning: Final note cannot be empty."

    def test_valid_note_is_written_to_file(self, tmp_path):
        target = tmp_path / "log.txt"
        lr.close_out_session(str(target), "All books returned.")
        with open(target, "r") as f:
            lines = f.read().splitlines()
        assert "All books returned." in lines

    def test_session_end_always_written_on_success(self, tmp_path):
        target = tmp_path / "log.txt"
        lr.close_out_session(str(target), "All books returned.")
        with open(target, "r") as f:
            lines = f.read().splitlines()
        assert "SESSION END" in lines

    def test_session_end_always_written_on_failure(self, tmp_path):
        target = tmp_path / "log.txt"
        lr.close_out_session(str(target), "")
        with open(target, "r") as f:
            lines = f.read().splitlines()
        assert "SESSION END" in lines

    def test_appends_to_existing_log(self, tmp_path):
        target = tmp_path / "log.txt"
        target.write_text("alice|Dune\n")
        lr.close_out_session(str(target), "Done for today.")
        with open(target, "r") as f:
            lines = f.read().splitlines()
        assert lines == ["alice|Dune", "Done for today.", "SESSION END"]


class TestExportCatalogToCsv:
    def test_creates_file(self, tmp_path):
        target = tmp_path / "catalog.csv"
        lr.export_catalog_to_csv(str(target), [("Dune", 4)])
        assert target.exists()

    def test_header_row(self, tmp_path):
        target = tmp_path / "catalog.csv"
        lr.export_catalog_to_csv(str(target), [("Dune", 4)])
        with open(target, "r", newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
        assert header == ["title", "copies_available"]

    def test_data_rows(self, tmp_path):
        target = tmp_path / "catalog.csv"
        lr.export_catalog_to_csv(str(target), [("Dune", 4), ("1984", 0)])
        with open(target, "r", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)
        assert rows[1] == ["Dune", "4"]
        assert rows[2] == ["1984", "0"]

    def test_empty_catalog_writes_only_header(self, tmp_path):
        target = tmp_path / "catalog.csv"
        lr.export_catalog_to_csv(str(target), [])
        with open(target, "r", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)
        assert rows == [["title", "copies_available"]]

    def test_handles_non_numeric_copies_without_crashing(self, tmp_path):
        target = tmp_path / "catalog.csv"
        lr.export_catalog_to_csv(str(target), [("bad_entry", "N/A")])
        with open(target, "r", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)
        assert rows[1] == ["bad_entry", "N/A"]


class TestImportAvailableTitles:
    @staticmethod
    def _write_catalog_csv(path, rows):
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "copies_available"])
            writer.writerows(rows)

    def test_basic_case(self, tmp_path):
        target = tmp_path / "catalog.csv"
        self._write_catalog_csv(target, [["Dune", 4], ["1984", 0], ["Hamlet", 2]])
        result = lr.import_available_titles(str(target), 1)
        assert result == ["Dune", "Hamlet"]

    def test_returns_a_list(self, tmp_path):
        target = tmp_path / "catalog.csv"
        self._write_catalog_csv(target, [["Dune", 4]])
        result = lr.import_available_titles(str(target), 1)
        assert isinstance(result, list)

    def test_result_is_sorted(self, tmp_path):
        target = tmp_path / "catalog.csv"
        self._write_catalog_csv(target, [["Zorro", 5], ["Anna Karenina", 3]])
        result = lr.import_available_titles(str(target), 1)
        assert result == ["Anna Karenina", "Zorro"]

    def test_missing_file_returns_empty_list(self, tmp_path):
        target = tmp_path / "does_not_exist.csv"
        result = lr.import_available_titles(str(target), 1)
        assert result == []

    def test_skips_non_numeric_copies(self, tmp_path):
        target = tmp_path / "catalog.csv"
        self._write_catalog_csv(target, [["Dune", 4], ["bad_entry", "N/A"]])
        result = lr.import_available_titles(str(target), 1)
        assert result == ["Dune"]

    def test_boundary_value_is_inclusive(self, tmp_path):
        target = tmp_path / "catalog.csv"
        self._write_catalog_csv(target, [["Dune", 2]])
        result = lr.import_available_titles(str(target), 2)
        assert result == ["Dune"]

    def test_excludes_titles_below_threshold(self, tmp_path):
        target = tmp_path / "catalog.csv"
        self._write_catalog_csv(target, [["1984", 0]])
        result = lr.import_available_titles(str(target), 1)
        assert result == []


class TestUpdateLibrarySettings:
    def test_creates_file_if_missing(self, tmp_path):
        target = tmp_path / "settings.json"
        lr.update_library_settings(str(target), "theme", "dark")
        assert target.exists()

    def test_returns_a_dict(self, tmp_path):
        target = tmp_path / "settings.json"
        result = lr.update_library_settings(str(target), "theme", "dark")
        assert isinstance(result, dict)

    def test_adds_new_key(self, tmp_path):
        target = tmp_path / "settings.json"
        result = lr.update_library_settings(str(target), "theme", "dark")
        assert result == {"theme": "dark"}

    def test_updates_existing_key(self, tmp_path):
        target = tmp_path / "settings.json"
        target.write_text(json.dumps({"theme": "light"}))
        result = lr.update_library_settings(str(target), "theme", "dark")
        assert result == {"theme": "dark"}

    def test_preserves_other_keys(self, tmp_path):
        target = tmp_path / "settings.json"
        lr.update_library_settings(str(target), "theme", "dark")
        result = lr.update_library_settings(str(target), "max_checkouts", 5)
        assert result == {"theme": "dark", "max_checkouts": 5}

    def test_none_value_removes_existing_key(self, tmp_path):
        target = tmp_path / "settings.json"
        target.write_text(json.dumps({"theme": "dark", "max_checkouts": 5}))
        result = lr.update_library_settings(str(target), "theme", None)
        assert result == {"max_checkouts": 5}

    def test_none_value_on_absent_key_is_a_no_op(self, tmp_path):
        target = tmp_path / "settings.json"
        target.write_text(json.dumps({"theme": "dark"}))
        result = lr.update_library_settings(str(target), "nonexistent", None)
        assert result == {"theme": "dark"}

    def test_persists_to_disk(self, tmp_path):
        target = tmp_path / "settings.json"
        lr.update_library_settings(str(target), "theme", "dark")
        with open(target, "r") as f:
            on_disk = json.load(f)
        assert on_disk == {"theme": "dark"}


if __name__ == "__main__":
    pytest.main(["-v", __file__])
