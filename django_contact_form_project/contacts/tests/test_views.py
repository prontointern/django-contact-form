from django.test import TestCase


class ContactViewTest(TestCase):
    def test_contact_view_is_accessible(self):
        url = '/contact/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact_view_should_have_contact_form_header(self):
        url = '/contact/'
        response = self.client.get(url)
        expected =  '<h1>Contact Form</h1>'
        self.assertContains(response, expected, status_code=200)

