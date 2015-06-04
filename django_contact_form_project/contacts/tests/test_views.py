from django.test import TestCase


class ContactViewTest(TestCase):
    def test_contactView_is_accessable(self):
        url = '/contact/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



