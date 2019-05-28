from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'firmino9@gmail.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email for a new user is normalized"""
        email = 'VNSCRIPTKID@gMaIl.com'
        user = get_user_model().objects.create_user(email=email, password='123456')
        self.assertEqual(user.email, email.lower())

    def test_new_user_missing_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='123456')

    def test_new_user_missing_password(self):
        email = 'mosalah@gmail.com'
        try:
            user = get_user_model().objects.create_user(email=email, password=None)
        except ValueError as error:
            self.assertEqual(error.args[0], 'missing password')

    def test_new_user_default_props(self):
        email = 'mosalah@gmail.com'
        user = get_user_model().objects.create_user(email=email, password='123456')
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_active, True)

    def test_new_user_email_normalized_strip_spaces(self):
        email = '   mosalah@gmail.com  '
        user = get_user_model().objects.create_user(email=email, password='123456')
        self.assertEqual(user.email, email.strip())

    def test_create_superuser(self):
        email = 'superpower@gmail.com'
        password = '123456'
        user = get_user_model().objects.create_superuser(email, password)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
