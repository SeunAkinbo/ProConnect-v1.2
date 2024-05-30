#!/usr/bin/python3
"""Test module for the db class"""
import unittest
from models.engine.db import Database


class TestDatabase(unittest.TestCase):
    """Test database class"""
    def setUp(self):
        self.db = Database()

    def test_connect(self):
        self.assertIsNone(self.db.connect())

    def test_close(self):
        self.db.connect()
        self.assertIsNone(self.db.close())

    def test_execute_query(self):
        self.db.connect()
        query = "SELECT * FROM users"
        result = self.db.execute_query(query)
        self.assertIsInstance(result, list)
        self.db.close()

    from unittest.mock import patch


    def test_execute_invalid_query(self):
        self.db.connect()
        query = "INVALID SQL QUERY"
        with self.assertRaises(unittest.mock.MagicMock(side_effect=Exception)):
            self.db.execute_query(query)
            self.db.close()

    def test_commit_changes(self):
        try:
            self.db.connect()
        except Exception as e:
            self.fail(f"Failed to connect to the database: {e}")
        self.assertIsNone(self.db.rollback_changes())
        try:
            self.db.close()
        except Exception as e:
            self.fail(f"Failed to disconnect from the database: {e}")

    def test_rollback_changes(self):
        self.db.connect()
        self.assertIsNone(self.db.rollback_changes())
        self.db.close()
