# Programming Assignment 4 - Classes and Objects

## Assignment Overview

In this assignment, you will practice defining your own class in
Python, including instance variables, a class variable, encapsulation
with getter/setter methods, and dunder ("double underscore") methods
with operator overloading. All of the exercises are built around a
single `WeatherStation` class that models a weather station's current
temperature reading: tracking the temperature and how many readings
have been taken with encapsulated getters and setters, printing
stations in human-readable and developer-facing formats, comparing and
ordering stations by temperature, and merging two sensor readings from
the same station with the `+` operator.


## Learning Objectives

By the end of this assignment, you should be able to:

- Define a class with both instance variables (e.g., `self.station_id`)
  and a class variable (e.g., `WeatherStation.total_stations`) shared
  by every instance.
- Use a single leading underscore (e.g., `self._temperature`) to
  signal a pseudo-private attribute, and write getter/setter methods
  that validate input before updating it.
- Implement dunder methods `__str__`, `__repr__`, and `__eq__` to
  control how instances are printed and compared.
- Implement `__lt__` to make instances of your class sortable with
  Python's built-in `sorted()`.
- Overload the `+` operator with `__add__` to define custom, sensible
  behavior for combining two instances of your class.


## Assignment Structure

This assignment is split across a few files: a starter file containing
a class for you to complete, a test file used to automatically grade
your work, and supporting configuration for running the tests both
locally and on GitHub Actions.


### Directory Structure

```
218-pa-4/
├── README.md
├── requirements.txt
├── weather_station.py
├── test_weather_station.py
└── .github
    └── workflows
        └── classroom.yml
```


## Functions to Implement

All of the methods below live in `weather_station.py`, inside the
`WeatherStation` class. Do not change the class name, method names, or
parameter lists -- the autograder depends on these exact signatures.
Read each item's docstring carefully for the exact expected behavior
and return type.

| Method | Description |
| --- | --- |
| `__init__(station_id, temperature, reading_count=0)` | Store `station_id` publicly and `temperature`/`reading_count` as pseudo-private attributes (`_temperature`, `_reading_count`), and increment the class variable `WeatherStation.total_stations`. |
| `get_temperature(self)` / `set_temperature(self, temperature)` | Getter/setter enforcing encapsulation: `set_temperature` raises `ValueError` for readings outside -100.0 to 150.0 degrees. |
| `get_reading_count(self)` / `record_reading(self)` | Getter, and a method that increases the reading count by 1 each time it is called. |
| `__str__(self)` / `__repr__(self)` | Human-readable and developer-facing string representations. |
| `__eq__(self, other)` | Returns **True** only when `other` is a `WeatherStation` with the same `station_id` and `temperature`. |
| `__lt__(self, other)` | Orders stations by temperature (coldest to warmest), enabling `sorted()`. |
| `__add__(self, other)` | Merges two sensor readings for the same station into a **new** `WeatherStation` (averaged temperature, summed reading counts). |


## Testing and Performance Analysis

Your implementation is checked with `test_weather_station.py`, a suite
of `pytest` unit tests covering every method listed above, including
typical inputs, edge cases (out-of-range temperatures, boundary
values), and comparisons against non-`WeatherStation` objects.

This test suite is also used to **autograde** your submission through
a GitHub Actions workflow (`.github/workflows/classroom.yml`), which
automatically runs `pytest` every time you push your changes. You can
(and should) run the same tests locally before submitting.


## How to Run

1. Make sure you have Python 3 and `pip` installed.
2. Install the testing dependency:

   ```
   pip install -r requirements.txt
   ```

3. Open `weather_station.py` and complete the `WeatherStation` class,
   with each method marked with a `# TODO` comment.
4. Run the program directly to try it out interactively:

   ```
   python weather_station.py
   ```

5. Run the automated test suite to check your work:

   ```
   pytest test_weather_station.py -v
   ```


## Expected Output

When you run the test suite with `pytest test_weather_station.py -v`,
it will print one line per test case, showing the test's name followed
by `PASSED` or `FAILED`. Tests are grouped by the method they check, so
a failing test's name (for example
`TestOperatorOverloading::test_add_combines_matching_ids`) tells you
exactly which method and which scenario is not yet working correctly.
When every method has been implemented correctly, all tests should
report `PASSED`, and pytest will print a final summary line such as
`35 passed in 0.05s`.
