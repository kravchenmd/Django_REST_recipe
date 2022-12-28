"""
Tests for DB models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTetst(TestCase):
    """Tets models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = '123'

        # better to use `get_user_model.objects` to access models
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
