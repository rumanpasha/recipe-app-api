from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

	def test_create_user_with_email_successful(self):
		email = 'test@test.com'
		password = 'passwd'

		user = get_user_model().objects.create_user(email=email, password=password)

		self.assertEqual(user.email, email)

		self.assertTrue(user.check_password(password))

	def test_new_user_normalized(self):
		email = 'test@RUMANPASHA.COM'

		user = get_user_model().objects.create_user(email, 'abc123')

		self.assertEqual(user.email, email.lower())

	def test_user_email_validation(self):
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None, 'pass123')

	def test_create_superuser(self):
		user = get_user_model().objects.create_superuser('test124@test.com', '123')

		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)