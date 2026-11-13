"""
CS 218 - Intermediate Python
Programming Assignment 5: Inheritance and Polymorphism

This starter module models records in a museum collection catalog. Complete
the TODO sections according to the docstrings. Do not change the required
class, method, or function names or parameter lists; the autograder depends
on these exact signatures.
"""

from abc import ABC, abstractmethod
from typing import Protocol, override, runtime_checkable


@runtime_checkable
class ExhibitLabel(Protocol):
    """
    Structural interface for collection records that can produce a short
    label suitable for an exhibit or gallery display.
    """

    def exhibit_label(self) -> str:
        """Return a concise, visitor-facing label for this record."""
        ...


class CollectionRecord(ABC):
    """
    Abstract base class for catalog entries in the museum's collection.

    Every record has a shared accession number, title, and collection name.
    Concrete record types provide their own details for the catalog.
    """

    def __init__(
        self, accession_number: str, title: str, collection: str
    ) -> None:
        """
        Initialize the shared information for a collection record.

        Store each argument as a public instance attribute with the same name:
        `accession_number`, `title`, and `collection`.

        :param accession_number: str, the museum's unique catalog identifier
        :param title: str, the record's public-facing title
        :param collection: str, the collection or department that holds it
        :return: None
        """
        # TODO: Implement this method
        pass

    @abstractmethod
    def catalog_details(self) -> str:
        """
        Declare the method that each concrete record type must implement.

        Do not implement this method in `CollectionRecord`; the ellipsis is
        only a placeholder for this abstract method. Implementations belong
        in `ObjectRecord` and `OralHistoryRecord`. Each implementation should
        return the record-type-specific details without the shared accession
        number, title, or collection.

        :return: str, a concise description specific to the concrete record
        """
        ...

    def catalog_entry(self, include_details: bool = False) -> str:
        """
        Format the shared information as:
        "ACCESSION | TITLE | COLLECTION"

        If `include_details` is True, append " | " and the result of
        `catalog_details()`. If it is False, do not include type-specific
        details. This optional parameter allows callers to request either
        a brief index entry or a detailed catalog entry.

        :param include_details: bool, whether to include record-specific details
        :return: str, the formatted catalog entry
        """
        # TODO: Implement this method
        pass


class ObjectRecord(CollectionRecord, ExhibitLabel):
    """
    Catalog record for a physical object in the museum collection.

    This class extends `CollectionRecord` and explicitly implements the
    `ExhibitLabel` protocol.
    """

    def __init__(
        self,
        accession_number: str,
        title: str,
        collection: str,
        material: str,
        origin: str,
    ) -> None:
        """
        Initialize the shared record data and the physical-object details.

        Use `super()` to initialize the base-class fields. Store `material`
        and `origin` as public attributes with those names.

        :param accession_number: str, the museum's unique catalog identifier
        :param title: str, the object's public-facing title
        :param collection: str, the collection that holds the object
        :param material: str, the primary material (e.g., "wool" or "bronze")
        :param origin: str, the object's place or cultural origin
        :return: None
        """
        # TODO: Implement this method
        pass

    def catalog_details(self) -> str:
        """
        Return details formatted exactly as:
        "Material: MATERIAL; origin: ORIGIN"

        :return: str, the material and origin for this object
        """
        # TODO: Implement this method
        pass

    @override
    def catalog_entry(self, include_details: bool = False) -> str:
        """
        Override the base implementation by prefixing its result with
        "Object: ". Use `super()` to retain the base formatting and optional
        detail behavior.

        :param include_details: bool, whether to include object details
        :return: str, the prefixed catalog entry
        """
        # TODO: Implement this method
        pass

    def exhibit_label(self) -> str:
        """
        Return an exhibit label formatted exactly as:
        "TITLE (ACCESSION): MATERIAL"

        :return: str, a concise visitor-facing label
        """
        # TODO: Implement this method
        pass


class OralHistoryRecord(CollectionRecord, ExhibitLabel):
    """
    Catalog record for an oral-history recording held in the museum archive.

    This class also explicitly implements the `ExhibitLabel` protocol.
    """

    def __init__(
        self,
        accession_number: str,
        title: str,
        collection: str,
        speaker: str,
        duration_minutes: float,
    ) -> None:
        """
        Initialize the shared record data and the recording-specific details.

        Use `super()` to initialize the base-class fields. Store `speaker` and
        `duration_minutes` as public attributes with those names.

        :param accession_number: str, the archive's unique catalog identifier
        :param title: str, the recording's public-facing title
        :param collection: str, the collection that holds the recording
        :param speaker: str, the person whose story is recorded
        :param duration_minutes: float, the recording length in minutes
        :return: None
        """
        # TODO: Implement this method
        pass

    def catalog_details(self) -> str:
        """
        Return details formatted exactly as:
        "Speaker: SPEAKER; duration: DURATION minutes"

        Format the duration without unnecessary trailing zeroes (for example,
        18.0 is displayed as 18 and 18.5 is displayed as 18.5).

        :return: str, the speaker and duration for this recording
        """
        # TODO: Implement this method
        pass

    @override
    def catalog_entry(self, include_details: bool = False) -> str:
        """
        Override the base implementation by prefixing its result with
        "Oral history: ". Use `super()` to retain the base formatting and
        optional detail behavior.

        :param include_details: bool, whether to include recording details
        :return: str, the prefixed catalog entry
        """
        # TODO: Implement this method
        pass

    def exhibit_label(self) -> str:
        """
        Return an exhibit label formatted exactly as:
        "TITLE (ACCESSION): oral history with SPEAKER"

        :return: str, a concise visitor-facing label
        """
        # TODO: Implement this method
        pass


def format_catalog(records: list[CollectionRecord]) -> list[str]:
    """
    Return a list of detailed catalog entries for the supplied records.

    Call each record's `catalog_entry` method with details enabled so Python
    dispatches to the concrete class's override. Preserve the input order.

    :param records: list[CollectionRecord], records to format
    :return: list[str], one detailed catalog entry per input record
    """
    # TODO: Implement this function
    pass


def collect_exhibit_labels(items: list[object]) -> list[str]:
    """
    Return exhibit labels from objects that satisfy the `ExhibitLabel`
    protocol. Ignore objects that do not provide `exhibit_label()`, and
    preserve the order of the compatible objects. Use
    `isinstance(item, ExhibitLabel)` to check whether each item satisfies
    the protocol before calling its `exhibit_label()` method.

    :param items: list[object], objects that may provide an exhibit label
    :return: list[str], the labels produced by compatible objects
    """
    # TODO: Implement this function
    pass


def main() -> None:
    """
    A small console driver so you can manually exercise the class
    above. This function is not graded, but is a useful way to try
    out your implementation interactively. Otherwise, just run the
    test suite.
    """
    textile = ObjectRecord(
        "M-1948-22",
        "Woven River Pattern",
        "Regional Textiles",
        "wool",
        "Upper Valley",
    )
    recording = OralHistoryRecord(
        "OH-2007-06",
        "A Market Day Remembered",
        "Community Voices",
        "Leila Hassan",
        18.5,
    )

    for entry in format_catalog([textile, recording]):
        print(entry)
    for label in collect_exhibit_labels([textile, recording]):
        print(label)


if __name__ == "__main__":
    main()
