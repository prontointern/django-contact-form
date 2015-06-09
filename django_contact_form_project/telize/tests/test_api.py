from mock import patch

from django.test import TestCase

from telize.api.geoip import GeoIP


class GeoIPTest(TestCase):
    @patch('telize.api.geoip.requests.get')
    def test_get_ip_lat_lng_successfully(self, mock):
        expected = {
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
        mock.return_value.json.return_value = expected

        geoip = GeoIP()
        result = geoip.getGeoIP()


        self.assertDictEqual(result, expected)

    @patch('telize.api.geoip.requests.get')
    def test_call_api_correctly(self, mock):
        geoip = GeoIP()
        geoip.getGeoIP()
        mock.assert_called_once_with('http://www.telize.com/geoip')

