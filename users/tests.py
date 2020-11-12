from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def setUp(self):
        self.login = {
            "email": "testUser@me.com",
            "password": "password@2015"
        }

        self.register = {
            "email": "testUser@me.com",
            "first_name": "Steve",
            "last_name": "jobs",
            "password": "password@2015",
            "password2": "password@2015"
        }
        self.user = get_user_model()
        self.user.objects.create_superuser(**self.login)

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_login(self):
        response = self.client.post('/accounts/login/', self.login)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.post('/accounts/signup/', self.register, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testUser@me.com")
        self.assertContains(response, "Steve")
        self.assertContains(response, "jobs")
        self.assertNotContains(response, "Eminem")

    def test_logout(self):
        response = self.client.post('/accounts/logout/', self.login, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_active)
