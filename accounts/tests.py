from django.test import TestCase
from .models import CustomUserModel

class UserManagerTests(TestCase):

    def test_create_user(self):
        user = CustomUserModel.objects.create_user(
            email='testuser@example.com',
            phone='1234567890',
            date_of_birth='2000-01-01',
            password='password123'
        )
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.phone, '1234567890')
        self.assertTrue(user.check_password('password123'))
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            CustomUserModel.objects.create_user(
                email='',
                phone='1234567890',
                date_of_birth='2000-01-01',
                password='password123'
            )

    def test_create_superuser(self):
        admin_user = CustomUserModel.objects.create_superuser(
            email='admin@example.com',
            phone='0987654321',
            date_of_birth='1990-01-01',
            password='adminpassword123'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertEqual(admin_user.phone, '0987654321')
        self.assertTrue(admin_user.check_password('adminpassword123'))
        self.assertTrue(admin_user.is_admin)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_active)
    