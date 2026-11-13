"""
CS 218 - Intermediate Python
Programming Assignment 4: Classes and Objects

Unit tests for weather_station.py

These tests are used to autograde the assignment via GitHub Actions.
Run them locally with:

    pytest test_weather_station.py -v

You should not need to modify this file.
"""
try:
    import pytest
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])
    import pytest

import weather_station as ws


class TestWeatherStationInit:
    def test_public_station_id_attribute(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        assert s.station_id == "STN-01"

    def test_temperature_stored_as_pseudo_private(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        assert s._temperature == 72.5

    def test_reading_count_stored_as_pseudo_private(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        assert s._reading_count == 3

    def test_reading_count_defaults_to_zero(self):
        s = ws.WeatherStation("STN-02", 68.0)
        assert s._reading_count == 0

    def test_temperature_is_cast_to_float(self):
        s = ws.WeatherStation("STN-01", 72, 3)
        assert isinstance(s._temperature, float)

    def test_total_stations_increments(self):
        before = ws.WeatherStation.total_stations
        ws.WeatherStation("TEMP-1", 50.0)
        ws.WeatherStation("TEMP-2", 50.0)
        after = ws.WeatherStation.total_stations
        assert after == before + 2

    def test_total_stations_shared_across_instances(self):
        s1 = ws.WeatherStation("TEMP-3", 50.0)
        s2 = ws.WeatherStation("TEMP-4", 50.0)
        assert s1.total_stations == s2.total_stations


class TestEncapsulation:
    def test_get_temperature_returns_current_value(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        assert s.get_temperature() == 72.5

    def test_set_temperature_updates_value(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        s.set_temperature(80.0)
        assert s.get_temperature() == 80.0

    def test_set_temperature_accepts_lower_boundary(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        s.set_temperature(-100.0)
        assert s.get_temperature() == -100.0

    def test_set_temperature_accepts_upper_boundary(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        s.set_temperature(150.0)
        assert s.get_temperature() == 150.0

    def test_set_temperature_rejects_below_range(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        with pytest.raises(ValueError):
            s.set_temperature(-250.0)

    def test_set_temperature_rejects_above_range(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        with pytest.raises(ValueError):
            s.set_temperature(200.0)

    def test_set_temperature_error_message(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        with pytest.raises(ValueError, match="Temperature must be between -100.0 and 150.0 degrees."):
            s.set_temperature(500.0)

    def test_set_temperature_invalid_value_unchanged(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        try:
            s.set_temperature(-250.0)
        except ValueError:
            pass
        assert s.get_temperature() == 72.5

    def test_get_reading_count_returns_current_value(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        assert s.get_reading_count() == 3

    def test_record_reading_increments_count(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        s.record_reading()
        assert s.get_reading_count() == 4

    def test_record_reading_multiple_calls(self):
        s = ws.WeatherStation("STN-01", 72.5)
        s.record_reading()
        s.record_reading()
        s.record_reading()
        assert s.get_reading_count() == 3


class TestDunderMethods:
    def test_str_format(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        assert str(s) == "STN-01: 72.5°F (3 readings)"

    def test_str_rounds_temperature(self):
        s = ws.WeatherStation("STN-01", 72.567, 3)
        assert str(s) == "STN-01: 72.6°F (3 readings)"

    def test_repr_format(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        assert repr(s) == "WeatherStation(station_id='STN-01', temperature=72.5, reading_count=3)"

    def test_eq_true_for_matching_id_and_temperature(self):
        s1 = ws.WeatherStation("STN-01", 72.5, 3)
        s2 = ws.WeatherStation("STN-01", 72.5, 9)
        assert s1 == s2

    def test_eq_false_for_different_temperature(self):
        s1 = ws.WeatherStation("STN-01", 72.5, 3)
        s2 = ws.WeatherStation("STN-01", 80.0, 3)
        assert s1 != s2

    def test_eq_false_for_different_id(self):
        s1 = ws.WeatherStation("STN-01", 72.5, 3)
        s2 = ws.WeatherStation("STN-02", 72.5, 3)
        assert s1 != s2

    def test_eq_not_implemented_for_other_types(self):
        s1 = ws.WeatherStation("STN-01", 72.5, 3)
        assert s1.__eq__("STN-01") is NotImplemented

    def test_lt_true_for_lower_temperature(self):
        cold = ws.WeatherStation("STN-01", 32.0)
        warm = ws.WeatherStation("STN-02", 90.0)
        assert cold < warm

    def test_lt_false_for_higher_temperature(self):
        cold = ws.WeatherStation("STN-01", 32.0)
        warm = ws.WeatherStation("STN-02", 90.0)
        assert not (warm < cold)

    def test_lt_not_implemented_for_other_types(self):
        s = ws.WeatherStation("STN-01", 72.5, 3)
        assert s.__lt__(5) is NotImplemented

    def test_sorted_orders_by_temperature(self):
        a = ws.WeatherStation("A", 90.0)
        b = ws.WeatherStation("B", 32.0)
        c = ws.WeatherStation("C", 60.0)
        result = sorted([a, b, c])
        assert [x.get_temperature() for x in result] == [32.0, 60.0, 90.0]


class TestOperatorOverloading:
    def test_add_combines_matching_ids(self):
        primary = ws.WeatherStation("STN-01", 72.0, 3)
        backup = ws.WeatherStation("STN-01", 76.0, 1)
        merged = primary + backup
        assert merged.station_id == "STN-01"
        assert merged.get_temperature() == 74.0
        assert merged.get_reading_count() == 4

    def test_add_rounds_average_temperature(self):
        primary = ws.WeatherStation("STN-01", 72.0, 3)
        backup = ws.WeatherStation("STN-01", 73.0, 1)
        merged = primary + backup
        assert merged.get_temperature() == 72.5

    def test_add_returns_new_instance(self):
        primary = ws.WeatherStation("STN-01", 72.0, 3)
        backup = ws.WeatherStation("STN-01", 76.0, 1)
        merged = primary + backup
        assert merged is not primary
        assert merged is not backup

    def test_add_different_ids_returns_not_implemented(self):
        primary = ws.WeatherStation("STN-01", 72.0, 3)
        other = ws.WeatherStation("STN-02", 76.0, 1)
        assert primary.__add__(other) is NotImplemented

    def test_add_non_weatherstation_returns_not_implemented(self):
        primary = ws.WeatherStation("STN-01", 72.0, 3)
        assert primary.__add__(5) is NotImplemented

    def test_add_does_not_mutate_operands(self):
        primary = ws.WeatherStation("STN-01", 72.0, 3)
        backup = ws.WeatherStation("STN-01", 76.0, 1)
        _ = primary + backup
        assert primary.get_temperature() == 72.0
        assert backup.get_temperature() == 76.0


if __name__ == "__main__":
    pytest.main(["-v", __file__])
