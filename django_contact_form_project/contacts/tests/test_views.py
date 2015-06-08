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

        expected = '<input id="id_firstname" maxlength="100" name="firstname" '
        expected += 'type="text" />'
        self.assertContains(self.response, expected, status_code=200)

    def test_contact_view_should_have_lastname_and_input(self):
        expected = '<label>Last Name:</label>'
        self.assertContains(self.response, expected, status_code=200)

        expected = '<input id="id_lastname" maxlength="100" name="lastname" '
        expected += 'type="text" />'
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

    def test_submit_contact_data_without_firstname_should_not_save_data(self):
        data = {
            'firstname': '',
            'lastname': 'Smith'
        }
        self.client.post(self.url, data=data)
        contact_count = Contact.objects.filter(lastname='Smith').count()
        self.assertEqual(contact_count, 0)

    def test_submit_contact_data_without_lastname_should_not_save_data(self):
        data = {
            'firstname': 'John',
            'lastname': ''
        }
        self.client.post(self.url, data=data)
        contact_count = Contact.objects.all().count()
        self.assertEqual(contact_count, 0)

    def test_submit_contact_data_without_firstname_should_get_error_message(
        self
    ):
        data = {
            'firstname': '',
            'lastname': 'Smith'
        }
        response = self.client.post(self.url, data=data)
        expected = 'This field is required.'
        self.assertContains(response, expected, status_code=200)

    def test_submit_contact_data_without_lastname_should_get_error_message(
        self
    ):
        data = {
            'firstname': 'John',
            'lastname': ''
        }
        response = self.client.post(self.url, data=data)
        expected = 'This field is required.'
        self.assertContains(response, expected, status_code=200)

    def test_redirect_to_thank_you_page_successfully(self):
        data = {
            'firstname': 'John',
            'lastname': 'Smith'
        }
        response = self.client.post(
            self.url,
            data=data
        )
        self.assertRedirects(
            response,
            '/thankyou/?firstname=John',
            status_code=302,
            target_status_code=200
        )

    def test_redirected_page_should_contain_firstname(self):
        data = {
            'firstname': 'John',
            'lastname': 'Smith'
        }
        response = self.client.post(
            self.url,
            data=data,
            follow=True
        )
        expected = 'Firstname: John'
        self.assertContains(response, expected, status_code=200)


class ThankYouViewTest(TestCase):
    def test_thank_you_view_is_accessible(self):
        url = '/thankyou/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_thank_you_page_should_contain_title_thank_you(self):
        url = '/thankyou/'
        response = self.client.get(url)
        expected = '<h1>Thank you</h1>'
        self.assertContains(response, expected, status_code=200)

