from mock import patch

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

    def test_contact_view_should_have_email_and_input(self):
        expected = '<label>Email:</label>'
        self.assertContains(self.response, expected, status_code=200)

        expected = '<input id="id_email" maxlength="100" name="email" '
        expected += 'type="email" />'
        self.assertContains(self.response, expected, status_code=200)

    def test_contact_view_should_have_submit_button(self):
        expected = '<input type="submit" value="Submit">'
        self.assertContains(self.response, expected, status_code=200)

    def test_contact_view_should_accessible_by_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)

    @patch('contacts.views.GeoIP')
    def test_submit_contact_data_successfully(self, mock):
        mock.return_value.getGeoIP.return_value = {
            "longitude": 100.5014,
            "latitude": 13.754,
            "asn": "AS4750",
            "offset": "7",
            "ip": "58.137.162.34",
            "area_code": "0",
            "continent_code": "AS",
            "dma_code": "0",
            "city": "Bangkok",
            "timezone": "Asia/Bangkok",
            "region": "Krung Thep",
            "country_code": "TH",
            "isp": "CS LOXINFO PUBLIC COMPANY LIMITED",
            "country": "Thailand",
            "country_code3": "THA",
            "region_code": "40"
        }
        data = {
            'firstname': 'John',
            'lastname': 'Smith',
            'email': 'john@smith.com'
        }

        self.client.post(self.url, data=data)
        contact = Contact.objects.get(firstname='John')
        self.assertEqual(contact.firstname, 'John')
        self.assertEqual(contact.lastname, 'Smith')
        self.assertEqual(contact.email, 'john@smith.com')
        self.assertEqual(contact.ip, '58.137.162.34')
        self.assertEqual(contact.lat, '13.754')
        self.assertEqual(contact.lng, '100.5014')

    def test_submit_contact_data_without_firstname_should_not_save_data(self):
        data = {
            'firstname': '',
            'lastname': 'Smith',
            'email': 'john@smith.com'
        }
        self.client.post(self.url, data=data)
        contact_count = Contact.objects.filter(lastname='Smith').count()
        self.assertEqual(contact_count, 0)

    def test_submit_contact_data_without_lastname_should_not_save_data(self):
        data = {
            'firstname': 'John',
            'lastname': '',
            'email': 'john@smith.com'
        }
        self.client.post(self.url, data=data)
        contact_count = Contact.objects.all().count()
        self.assertEqual(contact_count, 0)

    def test_submit_contact_data_without_email_should_not_save_data(self):
        data = {
            'firstname': 'John',
            'lastname': 'Smith',
            'email': ''
        }
        self.client.post(self.url, data=data)
        contact_count = Contact.objects.filter(lastname='Smith').count()
        self.assertEqual(contact_count, 0)

    def test_submit_contact_data_without_firstname_should_get_error_message(
        self):
        data = {
            'firstname': '',
            'lastname': 'Smith',
            'email': 'john@smith.com'
        }
        response = self.client.post(self.url, data=data)
        expected = 'This field is required.'
        self.assertContains(response, expected, status_code=200)

    def test_submit_contact_data_without_email_should_get_error_message(
        self
    ):
        data = {
            'firstname': 'John',
            'lastname': 'Smith',
            'email': ''
        }
        response = self.client.post(self.url, data=data)
        expected = 'This field is required.'
        self.assertContains(response, expected, status_code=200)

    def test_submit_contact_data_without_lastname_should_get_error_message(
        self
    ):
        data = {
            'firstname': 'John',
            'lastname': '',
            'email': 'john@smith.com'
        }
        response = self.client.post(self.url, data=data)
        expected = 'This field is required.'
        self.assertContains(response, expected, status_code=200)

    @patch('contacts.views.GeoIP')
    def test_redirect_to_thank_you_page_successfully(self, mock):
        mock.return_value.getGeoIP.return_value = {
            "longitude": 100.5014,
            "latitude": 13.754,
            "asn": "AS4750",
            "offset": "7",
            "ip": "58.137.162.34",
            "area_code": "0",
            "continent_code": "AS",
            "dma_code": "0",
            "city": "Bangkok",
            "timezone": "Asia/Bangkok",
            "region": "Krung Thep",
            "country_code": "TH",
            "isp": "CS LOXINFO PUBLIC COMPANY LIMITED",
            "country": "Thailand",
            "country_code3": "THA",
            "region_code": "40"
        }
        data = {
            'firstname': 'John',
            'lastname': 'Smith',
            'email': 'john@smith.com'
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

    @patch('contacts.views.GeoIP')
    def test_redirected_page_should_contain_firstname(self, mock):
        mock.return_value.getGeoIP.return_value = {
            "longitude": 100.5014,
            "latitude": 13.754,
            "asn": "AS4750",
            "offset": "7",
            "ip": "58.137.162.34",
            "area_code": "0",
            "continent_code": "AS",
            "dma_code": "0",
            "city": "Bangkok",
            "timezone": "Asia/Bangkok",
            "region": "Krung Thep",
            "country_code": "TH",
            "isp": "CS LOXINFO PUBLIC COMPANY LIMITED",
            "country": "Thailand",
            "country_code3": "THA",
            "region_code": "40"
        }
        data = {
            'firstname': 'John',
            'lastname': 'Smith',
            'email': 'john@smith.com'
        }
        response = self.client.post(
            self.url,
            data=data,
            follow=True
        )
        expected = 'Firstname: John'
        self.assertContains(response, expected, status_code=200)

    @patch('contacts.views.GeoIP')
    def test_thank_you_page_should_contain_lastname(self, mock):
        mock.return_value.getGeoIP.return_value = {
            "longitude": 100.5014,
            "latitude": 13.754,
            "asn": "AS4750",
            "offset": "7",
            "ip": "58.137.162.34",
            "area_code": "0",
            "continent_code": "AS",
            "dma_code": "0",
            "city": "Bangkok",
            "timezone": "Asia/Bangkok",
            "region": "Krung Thep",
            "country_code": "TH",
            "isp": "CS LOXINFO PUBLIC COMPANY LIMITED",
            "country": "Thailand",
            "country_code3": "THA",
            "region_code": "40"
        }
        data = {
            'firstname': 'lnwBoss',
            'lastname': 'yong',
            'email': 'john@smith.com'
        }
        response = self.client.post(self.url, data=data, follow=True)
        expected = 'Lastname: yong'
        self.assertContains(response, expected, status_code=200)

    @patch('contacts.views.GeoIP')
    def test_call_geoip_api_successfully(self, mock):
        mock.return_value.getGeoIP.return_value = {
            "longitude": 100.5014,
            "latitude": 13.754,
            "asn": "AS4750",
            "offset": "7",
            "ip": "58.137.162.34",
            "area_code": "0",
            "continent_code": "AS",
            "dma_code": "0",
            "city": "Bangkok",
            "timezone": "Asia/Bangkok",
            "region": "Krung Thep",
            "country_code": "TH",
            "isp": "CS LOXINFO PUBLIC COMPANY LIMITED",
            "country": "Thailand",
            "country_code3": "THA",
            "region_code": "40"
        }
        data = {
            'firstname': 'John',
            'lastname': 'Smith',
            'email': 'john@smith.com'
        }
        response = self.client.post(
            self.url,
            data=data
        )
        mock.return_value_getGeoIP.assert_once_with()

    @patch('contacts.views.GeoIP')
    def test_thank_you_page_should_contain_ip(self, mock):
        mock.return_value.getGeoIP.return_value = {
            "longitude": 100.5014,
            "latitude": 13.754,
            "asn": "AS4750",
            "offset": "7",
            "ip": "58.137.162.34",
            "area_code": "0",
            "continent_code": "AS",
            "dma_code": "0",
            "city": "Bangkok",
            "timezone": "Asia/Bangkok",
            "region": "Krung Thep",
            "country_code": "TH",
            "isp": "CS LOXINFO PUBLIC COMPANY LIMITED",
            "country": "Thailand",
            "country_code3": "THA",
            "region_code": "40"
        }
        data = {
            'firstname': 'lnwBoss',
            'lastname': 'yong',
            'email': 'john@smith.com'
        }
        response = self.client.post(self.url, data=data, follow=True)
        expected = 'IP: 58.137.162.34'
        self.assertContains(response, expected, status_code=200)

    @patch('contacts.views.GeoIP')
    def test_thank_you_page_should_contain_lat(self, mock):
        mock.return_value.getGeoIP.return_value = {
            "longitude": 100.5014,
            "latitude": 13.754,
            "asn": "AS4750",
            "offset": "7",
            "ip": "58.137.162.34",
            "area_code": "0",
            "continent_code": "AS",
            "dma_code": "0",
            "city": "Bangkok",
            "timezone": "Asia/Bangkok",
            "region": "Krung Thep",
            "country_code": "TH",
            "isp": "CS LOXINFO PUBLIC COMPANY LIMITED",
            "country": "Thailand",
            "country_code3": "THA",
            "region_code": "40"
        }
        data = {
            'firstname': 'lnwBoss',
            'lastname': 'yong',
            'email': 'john@smith.com'
        }
        response = self.client.post(self.url, data=data, follow=True)
        expected = 'Lat: 13.754'
        self.assertContains(response, expected, status_code=200)

    @patch('contacts.views.GeoIP')
    def test_thank_you_page_should_contain_lng(self, mock):
        mock.return_value.getGeoIP.return_value = {
            "longitude": 100.5014,
            "latitude": 13.754,
            "asn": "AS4750",
            "offset": "7",
            "ip": "58.137.162.34",
            "area_code": "0",
            "continent_code": "AS",
            "dma_code": "0",
            "city": "Bangkok",
            "timezone": "Asia/Bangkok",
            "region": "Krung Thep",
            "country_code": "TH",
            "isp": "CS LOXINFO PUBLIC COMPANY LIMITED",
            "country": "Thailand",
            "country_code3": "THA",
            "region_code": "40"
        }
        data = {
            'firstname': 'lnwBoss',
            'lastname': 'yong',
            'email': 'john@smith.com'
        }
        response = self.client.post(self.url, data=data, follow=True)
        expected = 'Lng: 100.5014'
        self.assertContains(response, expected, status_code=200)

    @patch('contacts.views.GeoIP')
    def test_thank_you_page_should_contain_email(self, mock):
        mock.return_value.getGeoIP.return_value = {
            "longitude": 100.5014,
            "latitude": 13.754,
            "asn": "AS4750",
            "offset": "7",
            "ip": "58.137.162.34",
            "area_code": "0",
            "continent_code": "AS",
            "dma_code": "0",
            "city": "Bangkok",
            "timezone": "Asia/Bangkok",
            "region": "Krung Thep",
            "country_code": "TH",
            "isp": "CS LOXINFO PUBLIC COMPANY LIMITED",
            "country": "Thailand",
            "country_code3": "THA",
            "region_code": "40"
        }
        data = {
            'firstname': 'lnwBoss',
            'lastname': 'yong',
            'email': 'john@smith.com'
        }
        response = self.client.post(self.url, data=data, follow=True)
        expected = 'Email: john@smith.com'
        self.assertContains(response, expected, status_code=200)


class ThankYouViewTest(TestCase):
    def setUp(self):
        self.url = reverse('thankyou')
        self.response = self.client.get(self.url)

    def test_thank_you_view_is_accessible(self):
        self.assertEqual(self.response.status_code, 200)

    def test_thank_you_page_should_contain_title_thank_you(self):
        expected = '<h1>Thank you</h1>'
        self.assertContains(self.response, expected, status_code=200)

