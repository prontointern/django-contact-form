from django.db import IntegrityError
from django.test import TestCase

from ..models import Contact


class ContactTest(TestCase):
    def test_save_contact_data_successfully(self):
        contact = Contact()
        contact.firstname = 'John'
        contact.lastname = 'Smith'
        self.assertFalse(contact.pk)
        contact.save()
        self.assertTrue(contact.pk)

        contact = Contact.objects.get(firstname='John')
        self.assertEqual(contact.firstname, 'John')
        self.assertEqual(contact.lastname, 'Smith')

    def test_firstname_is_none_should_show_error(self):
        contact = Contact()
        contact.firstname = None
        contact.lastname = 'Smith'
        self.assertRaises(IntegrityError, contact.save)

    def test_lastname_is_none_should_show_error(self):
        contact = Contact()
        contact.firstname = 'John'
        contact.lastname = None
        self.assertRaises(IntegrityError, contact.save)

    def test_print_contact_object_should_be_readable(self):
        contact = Contact.objects.create(
            firstname='John',
            lastname='Smith'
        )
        expected = 'John Smith'
        self.assertEqual(contact.__unicode__(), expected)
