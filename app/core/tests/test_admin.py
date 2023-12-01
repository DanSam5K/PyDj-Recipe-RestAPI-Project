"""
Tests for the admin modification
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test the admin site"""
    def setUp(self):
        """Set up the tests create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='user@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='admin@example.com',
            password='testpass123',
            name='Test user full name'
        )

    def test_users_list(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        # /admin/core/user/add
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
