# Programming Assignment 5 - Inheritance and Polymorphism

## Assignment Overview

In this assignment, you will use inheritance and polymorphism to build part
of a museum collection catalog. The catalog contains records for two kinds of
holdings: physical objects and oral-history recordings. Both kinds of records
share an accession number, title, and collection name, but each kind has
different information to show in a detailed catalog entry.

Complete the class methods and helper functions in `museum_catalog.py`. The
abstract `CollectionRecord` class defines the common data and behavior.
`ObjectRecord` and `OralHistoryRecord` extend it, provide their own catalog
details, and override the shared catalog-entry method. Each concrete class
also explicitly implements the `ExhibitLabel` protocol, which describes the
short label an exhibit display can use.

This is an applied lab, not a program-design project: use the supplied
signatures and complete the methods marked with `TODO`. Do not change required
class, method, or function names or parameter lists because the tests depend
on them.

## Learning Objectives

By the end of this assignment, you should be able to:

* Define an abstract base class using `ABC` and `@abstractmethod`.
* Put shared attributes and reusable behavior in a parent class.
* Initialize inherited state by calling `super().__init__(...)`.
* Implement abstract methods in concrete subclasses.
* Override a concrete parent method and use `super()` to reuse its behavior.
* Use `@override` to identify methods that replace concrete parent methods.
* Use an optional parameter to support both brief and detailed catalog entries.
Python does not select methods by parameter signature; an optional parameter
is one straightforward way to support these related calls.
* Define a `Protocol` and explicitly inherit from it alongside a regular
parent class (for example, `class ObjectRecord(CollectionRecord, ExhibitLabel)`).
* Use a protocol to write a function that accepts different compatible object
types without requiring them to share a concrete parent class.
* Write and test small, self-contained class methods and functions with
`pytest`.

## Assignment Structure

The assignment includes a starter module with class and function stubs, a
pytest file that checks the required behavior, and a GitHub Actions workflow
that runs the tests for autograding. All assignment code and test data use
Python; no external data files or services are needed.

### Directory Structure

```
218-pa-5/
├── README.md
├── .gitignore
├── requirements.txt
├── museum_catalog.py
├── test_museum_catalog.py
└── .github
    └── workflows
        └── classroom.yml
```

## Functions to Implement

Complete the methods and functions in `museum_catalog.py`. Keep each required
name and parameter list unchanged. The docstrings in the starter module are the
authoritative reference for exact formatting and return values.

|Method or function|Description|
|-|-|
|`CollectionRecord.__init__(accession_number, title, collection)`|Store the three shared record fields as public attributes.|
|`CollectionRecord.catalog_details()`|Abstract method that each record type implements to describe its own information.|
|`CollectionRecord.catalog_entry(include_details=False)`|Format the shared fields and optionally append the concrete record's details.|
|`ObjectRecord.__init__(..., material, origin)`|Initialize the shared record with `super()` and store the object's material and origin.|
|`ObjectRecord.catalog_details()`|Return the required material-and-origin description.|
|`ObjectRecord.catalog_entry(include_details=False)`|Override the parent method, preserve its formatting with `super()`, and prefix the result with `"Object: "`.|
|`ObjectRecord.exhibit_label()`|Return the short display label for the physical object.|
|`OralHistoryRecord.__init__(..., speaker, duration_minutes)`|Initialize the shared record with `super()` and store the speaker and recording duration.|
|`OralHistoryRecord.catalog_details()`|Return the speaker and duration, formatting whole-minute durations without a decimal part.|
|`OralHistoryRecord.catalog_entry(include_details=False)`|Override the parent method, preserve its formatting with `super()`, and prefix the result with `"Oral history: "`.|
|`OralHistoryRecord.exhibit_label()`|Return the short display label for the recording.|
|`format_catalog(records)`|Return detailed catalog entries for a list of records, preserving input order.|
|`collect_exhibit_labels(items)`|Return labels from objects that satisfy `ExhibitLabel`, preserving their order and ignoring other objects. Use `isinstance(item, ExhibitLabel)` to test each item before calling its method.|

The two concrete record classes inherit from both `CollectionRecord` and
`ExhibitLabel`. This is the assignment's limited multiple-inheritance example:
the first parent supplies shared implementation, while the protocol specifies
an additional method that the concrete class promises to provide.

## Testing and Performance Analysis

Your implementation is checked with `test_museum_catalog.py`, a suite of
`pytest` unit tests covering every required class method and function. The
tests check that:

* `CollectionRecord` cannot be instantiated directly because it has an
abstract method.
* Concrete records initialize both shared and type-specific attributes.
* Base and overridden catalog entries use the required format, including the
optional details argument.
* Object and oral-history details and exhibit labels contain the correct
information.
* Oral-history durations display correctly for both whole and fractional
minutes.
* Concrete records explicitly satisfy the protocol, and an unrelated class
with the required method satisfies it structurally.
* The catalog and label helper functions preserve order, use polymorphic
behavior, filter incompatible objects where appropriate, and handle empty
lists.

The tests are also run by `.github/workflows/classroom.yml` for GitHub Actions
autograding. They use in-memory records, so running pytest does not create or
modify catalog files.

## How to Run

1. Make sure Python 3.12 or later and `pip` are installed.
2. From this directory, install the testing dependency:

```
   pip install -r requirements.txt
   ```

3. Open `museum_catalog.py` and complete each method and function marked with
`# TODO: Implement this method` or `# TODO: Implement this function`.
4. Optionally run the sample program to inspect the catalog output:

```
   python museum_catalog.py
   ```

5. Run the automated test suite:

```
   pytest test_museum_catalog.py -v
   ```

## Expected Output

When you run `pytest test_museum_catalog.py -v`, pytest displays one line for
each test, including its test name and a `PASSED` or `FAILED` result. The tests
are grouped by the class behavior or helper function they exercise, so a
failure name (for example,
`TestConcreteRecords::test_oral_history_details_format`) identifies the
behavior and scenario that needs attention. When all required behavior is
implemented correctly, all tests report `PASSED`, followed by a summary with
the total number of passed tests and the test run time.

