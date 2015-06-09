from django.test import TestCase

from ..forms import ContactForm


class ContactFormTest(TestCase):
    def test_contact_form_should_have_firstname_and_lastname_and_email_field(
        self
    ):
        form = ContactForm()

        expected_fields = ['firstname', 'lastname', 'email']
        for each in expected_fields:
            self.assertTrue(each in form.fields)

        self.assertEqual(len(form.fields), 3)

    def test_contact_form_with_valid_data_should_be_valid_and_have_no_error(
        self
    ):
        valid_data = {
            'firstname': 'John',
            'lastname': 'Smith',
            'email': 'john@smith.com'
        }
        form = ContactForm(data=valid_data)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    def test_contact_form_with_no_firstname_or_lastname_or_email_should_error(
        self
    ):
        invalid_data = [
            {
                'firstname': '',
                'lastname': 'Smith',
                'email': 'john@smith.com'
            },
            {
                'firstname': 'John',
                'lastname': '',
                'email': 'john@smith.com'
            },
            {
                'firstname': 'John',
                'lastname': 'Smith',
                'email': ''
            }
        ]

        for each in invalid_data:
            form = ContactForm(data=each)
            self.assertFalse(form.is_valid())
            self.assertTrue(form.errors)
