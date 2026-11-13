"""
CS 218 - Intermediate Python
Programming Assignment 4: Classes and Objects

In this assignment, you will practice defining your own class, including
instance variables, a class variable, encapsulation with getter/setter
methods, and dunder ("double underscore") methods with operator
overloading, applied to a small weather-station sensor scenario.

Complete the `WeatherStation` class below according to its docstrings.
Do NOT change the class name, method names, or parameter lists -- the
autograder (test_weather_station.py) depends on these exact signatures.

You may add helper methods of your own if you would like, but every
method listed in the README's "Functions to Implement" section must be
completed for the tests to pass.
"""


class WeatherStation:
    """
    Represents a single weather station reporting a current
    temperature reading.
    """

    # Class variable: shared by every WeatherStation instance. Tracks
    # how many WeatherStation objects have been created so far.
    total_stations: int = 0

    def __init__(self, station_id: str, temperature: float, reading_count: int = 0) -> None:
        """
        Initialize a new WeatherStation.

        Store `station_id` as a public attribute. Store `temperature`
        as the pseudo-private attribute `_temperature` (cast to
        float), and `reading_count` as the pseudo-private attribute
        `_reading_count`, both using a single leading underscore.
        Every time a new WeatherStation is constructed, increment the
        class variable `WeatherStation.total_stations` by 1.

        :param station_id: str, the station's identifier (e.g. "STN-01")
        :param temperature: float, the station's current temperature reading (°F)
        :param reading_count: int, number of readings recorded so far (default 0)
        :return: None
        """
        # TODO: Implement this method
        pass

    def get_temperature(self) -> float:
        """
        Return the station's current temperature reading (`self._temperature`).

        :return: float, the current temperature in degrees Fahrenheit
        """
        # TODO: Implement this method
        pass

    def set_temperature(self, temperature: float) -> None:
        """
        Update the station's temperature reading, enforcing
        encapsulation.

        If `temperature` is between -100.0 and 150.0 (inclusive),
        update `self._temperature` to `temperature`. Otherwise, raise
        a `ValueError` with the message
        "Temperature must be between -100.0 and 150.0 degrees.".

        :param temperature: float, the new temperature reading (°F)
        :return: None
        :raises ValueError: if temperature is out of range
        """
        # TODO: Implement this method
        pass

    def get_reading_count(self) -> int:
        """
        Return how many readings the station has recorded so far
        (`self._reading_count`).

        :return: int, the station's current reading count
        """
        # TODO: Implement this method
        pass

    def record_reading(self) -> None:
        """
        Record that the station has taken one additional temperature
        reading, by increasing `self._reading_count` by 1.

        :return: None
        """
        # TODO: Implement this method
        pass

    def __str__(self) -> str:
        """
        Return a user-facing string formatted exactly as:
        "StationID: X°F (Y readings)" with the temperature rounded to
        1 decimal place (e.g., "STN-01: 72.5°F (3 readings)").

        :return: str, the human-readable description
        """
        # TODO: Implement this method
        pass

    def __repr__(self) -> str:
        """
        Return a developer-facing representation formatted exactly as:
        "WeatherStation(station_id='ID', temperature=Temperature, reading_count=ReadingCount)"
        (e.g., "WeatherStation(station_id='STN-01', temperature=72.5, reading_count=3)").
        Use `!r` formatting for `station_id`.

        :return: str, the developer representation
        """
        # TODO: Implement this method
        pass

    def __eq__(self, other: object) -> bool:
        """
        Return True if `other` is a `WeatherStation` with the exact
        same `station_id` and the exact same temperature
        (`self._temperature`). Return `NotImplemented` if `other` is
        not an instance of `WeatherStation`.

        :param other: object, the value to compare against
        :return: bool (or NotImplemented)
        """
        # TODO: Implement this method
        pass

    def __lt__(self, other: object) -> bool:
        """
        Enable ordering (e.g. for `sorted()`) of stations by
        temperature, from coldest to warmest.

        Return True if this station's temperature is strictly less
        than `other`'s temperature. Return `NotImplemented` if `other`
        is not an instance of `WeatherStation`.

        :param other: object, the value to compare against
        :return: bool (or NotImplemented)
        """
        # TODO: Implement this method
        pass

    def __add__(self, other: object) -> "WeatherStation":
        """
        Overload the `+` operator to merge two sensor readings taken
        at the same station (for example, when a backup sensor's
        reading needs to be combined with the primary sensor's
        reading for that station).

        If `other` is a `WeatherStation` with the exact same
        `station_id`, return a brand-new `WeatherStation` instance
        with the same `station_id`, a temperature equal to the
        AVERAGE of both readings (rounded to 2 decimal places), and a
        reading count equal to the SUM of both reading counts. If
        `other` is not a `WeatherStation`, or has a different
        `station_id`, return `NotImplemented`.

        :param other: object, the value to add
        :return: a new WeatherStation instance, or NotImplemented
        """
        # TODO: Implement this method
        pass


def main():
    """
    A small console driver so you can manually exercise the class
    above. This function is not graded, but is a useful way to try
    out your implementation interactively. Otherwise, just run the
    test suite.
    """
    primary = WeatherStation("STN-01", 72.5, 3)
    backup = WeatherStation("STN-01", 75.5, 1)
    print(f"Total stations created: {WeatherStation.total_stations}")

    try:
        primary.set_temperature(-250.0)
    except ValueError as e:
        print(f"Validation Error: {e}")

    primary.record_reading()
    print(f"Primary station reading count: {primary.get_reading_count()}")

    print(f"Primary station: {primary}")
    print(f"Backup station: {backup}")

    merged = primary + backup
    print(f"Merged station: {merged}")
    print(f"Repr output: {repr(merged)}")

    other = WeatherStation("STN-02", 68.0)
    print(f"Sorted by temperature: {sorted([primary, backup, other])}")


if __name__ == "__main__":
    main()
