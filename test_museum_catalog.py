"""
CS 218 - Intermediate Python
Programming Assignment 5: Inheritance and Polymorphism

Unit tests for museum_catalog.py.py

These tests are used to autograde the assignment via GitHub Actions.
Run them locally with:

    pytest test_museum_catalog.py.py -v

You should not need to modify this file.
"""
try:
    import pytest
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])
    import pytest

import museum_catalog as mc


def make_object(**overrides):
    values = {
        "accession_number": "M-1948-22",
        "title": "Woven River Pattern",
        "collection": "Regional Textiles",
        "material": "wool",
        "origin": "Upper Valley",
    }
    values.update(overrides)
    return mc.ObjectRecord(**values)


def make_oral_history(**overrides):
    values = {
        "accession_number": "OH-2007-06",
        "title": "A Market Day Remembered",
        "collection": "Community Voices",
        "speaker": "Leila Hassan",
        "duration_minutes": 18.5,
    }
    values.update(overrides)
    return mc.OralHistoryRecord(**values)


class TestCollectionRecord:
    def test_base_class_is_abstract(self):
        with pytest.raises(TypeError):
            mc.CollectionRecord("M-1", "Untitled", "Objects")

    def test_subclasses_store_shared_attributes(self):
        record = make_object()
        assert record.accession_number == "M-1948-22"
        assert record.title == "Woven River Pattern"
        assert record.collection == "Regional Textiles"

    def test_base_catalog_entry_without_details(self):
        record = make_object()
        assert mc.CollectionRecord.catalog_entry(record) == (
            "M-1948-22 | Woven River Pattern | Regional Textiles"
        )

    def test_base_catalog_entry_can_include_details(self):
        record = make_object()
        assert mc.CollectionRecord.catalog_entry(record, True) == (
            "M-1948-22 | Woven River Pattern | Regional Textiles | "
            "Material: wool; origin: Upper Valley"
        )


class TestConcreteRecords:
    def test_object_record_initializes_its_own_fields(self):
        record = make_object()
        assert record.material == "wool"
        assert record.origin == "Upper Valley"

    def test_object_record_details_and_entry(self):
        record = make_object()
        assert record.catalog_details() == "Material: wool; origin: Upper Valley"
        assert record.catalog_entry() == (
            "Object: M-1948-22 | Woven River Pattern | Regional Textiles"
        )
        assert record.catalog_entry(True) == (
            "Object: M-1948-22 | Woven River Pattern | Regional Textiles | "
            "Material: wool; origin: Upper Valley"
        )

    def test_object_record_exhibit_label(self):
        assert make_object().exhibit_label() == (
            "Woven River Pattern (M-1948-22): wool"
        )

    def test_oral_history_initializes_its_own_fields(self):
        record = make_oral_history()
        assert record.speaker == "Leila Hassan"
        assert record.duration_minutes == 18.5

    def test_oral_history_details_format_duration(self):
        assert make_oral_history().catalog_details() == (
            "Speaker: Leila Hassan; duration: 18.5 minutes"
        )
        assert make_oral_history(duration_minutes=18.0).catalog_details() == (
            "Speaker: Leila Hassan; duration: 18 minutes"
        )

    def test_oral_history_entry_and_exhibit_label(self):
        record = make_oral_history()
        assert record.catalog_entry(True) == (
            "Oral history: OH-2007-06 | A Market Day Remembered | "
            "Community Voices | Speaker: Leila Hassan; duration: 18.5 minutes"
        )
        assert record.exhibit_label() == (
            "A Market Day Remembered (OH-2007-06): "
            "oral history with Leila Hassan"
        )


class TestPolymorphismAndProtocol:
    def test_both_record_types_implement_the_protocol(self):
        assert isinstance(make_object(), mc.ExhibitLabel)
        assert isinstance(make_oral_history(), mc.ExhibitLabel)
        assert not isinstance(object(), mc.ExhibitLabel)

    def test_protocol_is_structural(self):
        class ExternalExhibitLabel:
            def exhibit_label(self):
                return "Loan item: carved bowl."

        assert isinstance(ExternalExhibitLabel(), mc.ExhibitLabel)

    def test_format_catalog_uses_overrides_and_preserves_order(self):
        records = [make_oral_history(), make_object()]
        assert mc.format_catalog(records) == [
            records[0].catalog_entry(True),
            records[1].catalog_entry(True),
        ]

    def test_format_catalog_accepts_empty_list(self):
        assert mc.format_catalog([]) == []

    def test_collect_exhibit_labels_filters_and_preserves_order(self):
        class ExternalExhibitLabel:
            def exhibit_label(self):
                return "Loan item: carved bowl."

        obj = make_object()
        audio = make_oral_history()
        assert mc.collect_exhibit_labels(
            [obj, object(), ExternalExhibitLabel(), audio]
        ) == [
            obj.exhibit_label(),
            "Loan item: carved bowl.",
            audio.exhibit_label(),
        ]

    def test_collect_exhibit_labels_accepts_empty_list(self):
        assert mc.collect_exhibit_labels([]) == []


if __name__ == "__main__":
    pytest.main(["-v", __file__])
