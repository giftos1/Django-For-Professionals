from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.forms import CustomUserCreationForm


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


class SignUpPageTests(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Haha')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)