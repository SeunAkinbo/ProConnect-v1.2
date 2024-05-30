#!/usr/bin/python3
"""Module for testing BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """TestBaseModel class"""
    def test_init_no_args(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_init_with_kwargs(self):
        kwargs = {
            'id': 'test_id',
            'created_at': datetime(2023, 1, 1, 0, 0, 0),
            'updated_at': datetime(2023, 1, 1, 0, 0, 0)
        }
        instance = BaseModel(**kwargs)
        self.assertEqual(instance.id, 'test_id')
        self.assertEqual(instance.created_at, kwargs['created_at'])
        self.assertEqual(instance.updated_at, kwargs['updated_at'])

    def test_str_representation(self):
        instance = BaseModel()
        expected_str = f"[{instance.__class__.__name__}] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_str)

    def test_save_method(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)

    def test_to_dict_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'],
                         instance.__class__.__name__)
        self.assertEqual(instance_dict['created_at'],
                         instance.created_at.isoformat())
        self.assertEqual(instance_dict['updated_at'],
                         instance.updated_at.isoformat())
