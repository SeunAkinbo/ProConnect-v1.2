#!/usr/bin/python3
"""Module for testing Log class"""
import unittest
from datetime import datetime
from models.log import Log


class TestLogCreation(unittest.TestCase):
    def test_log_creation_with_valid_data(self):
        log_data = {
            "message": "Test log message",
            "level": "INFO",
            "timestamp": datetime.now(tz=datetime.timezone.utc)
        }
        log = Log(**log_data)
        self.assertEqual(log.message, log_data["message"])
        self.assertEqual(log.level, log_data["level"])
        self.assertEqual(log.timestamp, log_data["timestamp"])

    def test_log_creation_with_missing_data(self):
        log_data = {
            "message": "Test log message",
            "level": "INFO"
        }
        with self.assertRaises(TypeError):
            Log(**log_data)

    def test_log_creation_with_invalid_level(self):
        log_data = {
            "message": "Test log message",
            "level": "INVALID",
            "timestamp": datetime.now()
        }
        with self.assertRaises(ValueError):
            Log(**log_data)

class TestLogFormatting(unittest.TestCase):
    def test_log_string_representation(self):
        log_data = {
            "message": "Test log message",
            "level": "INFO",
            "timestamp": datetime(2023, 5, 1, 12, 0, 0)
        }
        log = Log(**log_data)
        expected_str = "2023-05-01 12:00:00 [INFO] Test log message"
        self.assertEqual(str(log), expected_str)

    def test_log_json_representation(self):
        log_data = {
            "message": "Test log message",
            "level": "WARNING",
            "timestamp": datetime(2023, 5, 1, 12, 0, 0)
        }
        log = Log(**log_data)
        expected_json = {
            "message": "Test log message",
            "level": "WARNING",
            "timestamp": "2023-05-01 12:00:00"
        }
        self.assertEqual(log.to_json(), expected_json, 'Log JSON representation does not match expected values.')
