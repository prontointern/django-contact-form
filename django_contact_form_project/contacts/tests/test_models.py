from django.db import IntegrityError
from django.test import TestCase

from ..models import Contact


class ContactTest(TestCase):
    def test_save_contact_data_successfully(self):
        contact = Contact()
        contact.firstname = 'John'
        contact.lastname = 'Smith'
        contact.email = 'john@smith.com'
        contact.ip = '58.137.162.34'
        contact.lat = '13.754'
        contact.lng = '100.5014'

        self.assertFalse(contact.pk)
        contact.save()
        self.assertTrue(contact.pk)

        contact = Contact.objects.get(firstname='John')
        self.assertEqual(contact.firstname, 'John')
        self.assertEqual(contact.lastname, 'Smith')
        self.assertEqual(contact.email, 'john@smith.com')
        self.assertEqual(contact.ip, '58.137.162.34')
        self.assertEqual(contact.lat, '13.754')
        self.assertEqual(contact.lng, '100.5014')

    def test_firstname_is_none_should_show_error(self):
        contact = Contact()
        contact.firstname = None
        contact.lastname = 'Smith'
        contact.email = 'john@smith.com'
        contact.ip = '58.137.162.34'
        contact.lat = '13.754'
        contact.lng = '100.5014'

        self.assertRaises(IntegrityError, contact.save)

    def test_email_is_none_should_show_error(self):
        contact = Contact()
        contact.firstname = 'John'
        contact.lastname = 'Smith'
        contact.email = None
        contact.ip = '58.137.162.34'
        contact.lat = '13.754'
        contact.lng = '100.5014'

        self.assertRaises(IntegrityError, contact.save)

    def test_lastname_is_none_should_show_error(self):
        contact = Contact()
        contact.firstname = 'John'
        contact.lastname = None
        contact.email = 'john@smith.com'
        contact.ip = '58.137.162.34'
        contact.lat = '13.754'
        contact.lng = '100.5014'
        self.assertRaises(IntegrityError, contact.save)

    def test_ip_is_none_should_not_show_error(self):
        contact = Contact()
        contact.firstname = 'John'
        contact.lastname = 'Smith'
        contact.email = 'john@smith.com'
        contact.ip = None
        contact.lat = '13.754'
        contact.lng = '100.5014'
        contact.save()
        self.assertTrue(contact.pk)

    def test_lat_and_lng_is_none_should_not_show_error(self):
        contact = Contact()
        contact.firstname = 'John'
        contact.lastname = 'Smith'
        contact.email = 'john@smith.com'
        contact.ip = '58.137.162.34'
        contact.lat = None
        contact.lng = None
        contact.save()
        self.assertTrue(contact.pk)

    def test_print_contact_object_should_be_readable(self):
        contact = Contact.objects.create(
            firstname='John',
            lastname='Smith',
            email='john@smith.com',
            ip='58.137.162.34',
            lat='13.754',
            lng='100.5014'
        )
        expected = 'John Smith'
        self.assertEqual(contact.__unicode__(), expected)
