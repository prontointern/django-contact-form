from django.contrib.auth.models import User
from django.test import TestCase


class ContactAdminTest(TestCase):
    def test_accessible_admin_contact(self):
        sup = User.objects.create_superuser(
            'admin',
            'admin@mail.com',
            'admin',
            first_name='Admin',
            last_name='Admin'
        )
        self.client.login(
            username='admin',
            password='admin'
        )

        url = '/admin/contacts/contact/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

