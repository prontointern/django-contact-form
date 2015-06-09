from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Contact


class ContactAdminTest(TestCase):
    def setUp(self):
        User.objects.create_superuser(
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

        self.url = '/admin/contacts/contact/'

    def test_accessible_admin_contact(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_contact_admin_should_have_firstname_column(self):
        Contact.objects.create(
            firstname='John',
            lastname='Smith',
            ip='58.137.162.34',
            lat='13.754',
            lng='100.5014'
        )

        response = self.client.get(self.url)
        expected = '<div class="text"><a href="?o=1">Firstname</a></div>'
        self.assertContains(response, expected, status_code=200)

    def test_contact_admin_should_have_lastname_column(self):
        Contact.objects.create(
            firstname='John',
            lastname='Smith',
            ip='58.137.162.34',
            lat='13.754',
            lng='100.5014'
        )
        response = self.client.get(self.url)
        expected = '<div class="text"><a href="?o=2">Lastname</a></div>'
        self.assertContains(response, expected, status_code=200)

    def test_contact_admin_should_have_ip_column(self):
        Contact.objects.create(
            firstname='John',
            lastname='Smith',
            ip='58.137.162.34',
            lat='13.754',
            lng='100.5014'
        )
        response = self.client.get(self.url)
        expected = '<div class="text"><a href="?o=3">Ip</a></div>'
        self.assertContains(response, expected, status_code=200)

    def test_contact_admin_should_have_lat_column(self):
        Contact.objects.create(
            firstname='John',
            lastname='Smith',
            ip='58.137.162.34',
            lat='13.754',
            lng='100.5014'
        )
        response = self.client.get(self.url)
        expected = '<div class="text"><a href="?o=4">Lat</a></div>'
        self.assertContains(response, expected, status_code=200)

    def test_contact_admin_should_have_lng_column(self):
        Contact.objects.create(
            firstname='John',
            lastname='Smith',
            ip='58.137.162.34',
            lat='13.754',
            lng='100.5014'
        )
        response = self.client.get(self.url)
        expected = '<div class="text"><a href="?o=5">Lng</a></div>'
        self.assertContains(response, expected, status_code=200)
