from django.contrib.auth import get_user_model
from django.test import TestCase


# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        user = get_user_model()
        create_user = user.objects.create(
            username='Paul',
            email='paul@gmail.com',
            password='pass123'
        )

        self.assertEqual(create_user.username, 'Paul')
        self.assertEqual(create_user.email, 'paul@gmail.com')
        self.assertTrue(create_user.is_active)
        self.assertFalse(create_user.is_staff)
        self.assertFalse(create_user.is_superuser)

    def test_create_superuser(self):
        user = get_user_model()
        create_superuser = user.objects.create_superuser(
            username='John',
            email='john@gmail.com',
            password='test321',
        )
        self.assertEqual(create_superuser.username, 'John')
        self.assertEqual(create_superuser.email, 'john@gmail.com')
        self.assertTrue(create_superuser.is_active)
        self.assertTrue(create_superuser.is_staff)
        self.assertTrue(create_superuser.is_superuser)


