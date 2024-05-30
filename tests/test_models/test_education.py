#!/user/bin/python3
"""Unittest module for the user class"""
import unittest
from models.education import Education


class TestEducationModel(unittest.TestCase):
    def test_education_creation(self):
        education = Education(school='Test University', degree='Bachelor of Science',
                              field_of_study='Computer Science', start_year=2015, end_year=2019)
        self.assertIsInstance(education, Education)
        self.assertEqual(education.school, 'Test University')
        self.assertEqual(education.degree, 'Bachelor of Science')
        self.assertEqual(education.field_of_study, 'Computer Science')
        self.assertEqual(education.start_year, 2015)
        self.assertEqual(education.end_year, 2019)

    def test_education_start_year_validation(self):
        with self.assertRaises(ValueError):
            Education(school='Test University', degree='Bachelor of Science',
                      field_of_study='Computer Science', start_year=2025, end_year=2029)

    def test_education_end_year_validation(self):
        with self.assertRaises(ValueError):
            Education(school='Test University', degree='Bachelor of Science',
                      field_of_study='Computer Science', start_year=2015, end_year=2010)

    def test_education_in_progress(self):
        education = Education(school='Test University', degree='Master of Science',
                              field_of_study='Computer Science', start_year=2020, end_year=None)
        self.assertIsInstance(education, Education)
        self.assertTrue(education.in_progress)

    def test_education_duration(self):
        education = Education(school='Test University', degree='Bachelor of Science',
                              field_of_study='Computer Science', start_year=2015, end_year=2019)
        self.assertEqual(education.duration, 4)
