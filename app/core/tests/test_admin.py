from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin = get_user_model().objects.create_superuser('root@gmail.com', '123456')
        self.client.force_login(self.admin)
        self.user = get_user_model().objects.create_user('normal@gmail.com', '123456')

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_customuser_changelist')
        response = self.client.get(url)
        self.assertContains(response, self.user.email)
        self.assertContains(response, self.admin.email)

    def test_users_edit_page(self):
        """Test that user edit page works"""
        url = reverse('admin:core_customuser_change', args=[self.user.id])
        # /admin/core/user/1
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
