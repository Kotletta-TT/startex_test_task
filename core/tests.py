from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class UserManagersTests(TestCase):

    def test_create_user(self):
        """Получим модель пользователя и попытаемся с помощью этой модели создать пользователя
        с email вместо username."""

        User = get_user_model()
        user = User.objects.create_user(email='test@test.com', password='foo')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='foo')


