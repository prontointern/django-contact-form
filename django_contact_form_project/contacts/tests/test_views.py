from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Contact


class ContactViewTest(TestCase):
    def setUp(self):
        self.url = reverse('contact')
        self.response = self.client.get(self.url)

    def test_contact_view_is_accessible(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contact_view_should_have_form_tag(self):
        expected = '<form action="." method="post">'
        self.assertContains(self.response, expected, status_code=200)

    def test_contact_view_should_have_firstname_input(self):
        expected = '<label>Firstname: '
        self.assertContains(self.response, expected, status_code=200)

        expected = '<input type="text" name="firstname">'
        self.assertContains(self.response, expected, status_code=200)

    def test_contact_view_should_have_lastname_and_input(self):
        expected = '<label>Last Name:</label>'
        self.assertContains(self.response, expected, status_code=200)

        expected = '<input type="text" name="lastname">'
        self.assertContains(self.response, expected, status_code=200)

    def test_contact_view_should_have_submit_button(self):
        expected = '<input type="submit" value="Submit">'
        self.assertContains(self.response, expected, status_code=200)

    def test_contact_view_should_accessible_by_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)

    def test_submit_contact_data_successfully(self):
        data = {
            'firstname': 'John',
            'lastname': 'Smith'
        }
        self.client.post(self.url, data=data)
        contact = Contact.objects.get(firstname='John')
        self.assertEqual(contact.firstname, 'John')
        self.assertEqual(contact.lastname, 'Smith')
