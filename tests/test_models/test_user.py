#!/usr/bin/python3
"""Unittest module for the user class"""
import unittest
from models.user import User


class TestUserModel(unittest.TestCase):
    """The unittest case for user model"""
    def test_user_creation(self):
        user = User(username='testuser',
                    email='test@example.com', password='password')
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('password'))

    def test_user_password_hashing(self):
        user = User(username='testuser',
                    email='test@example.com', password='password')
        self.assertNotEqual(user.password_hash, 'password')

    def test_user_password_verification(self):
        user = User(username='testuser',
                    email='test@example.com', password='password')
        self.assertTrue(user.check_password('password'))
        self.assertFalse(user.check_password('wrongpassword'))

    def test_user_avatar(self):
        user = User(username='testuser',
                    email='test@example.com', password='password')
        self.assertIsNone(user.avatar)

    def test_user_follow(self):
        user1 = User(username='user1', email='user1@example.com',
                     password='password')
        user2 = User(username='user2', email='user2@example.com',
                     password='password')
        user1.follow(user2)
        self.assertTrue(user1.is_following(user2))
        self.assertIn(user2, user1.followed)
        self.assertIn(user1, user2.followers)

    def test_user_unfollow(self):
        user1 = User(username='user1', email='user1@example.com',
                     password='password')
        user2 = User(username='user2', email='user2@example.com',
                     password='password')
        user1.follow(user2)
        user1.unfollow(user2)
        self.assertFalse(user1.is_following(user2))
        self.assertNotIn(user2, user1.followed)
        self.assertNotIn(user1, user2.followers)
