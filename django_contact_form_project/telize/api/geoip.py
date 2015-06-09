import requests


class GeoIP(object):
    def getGeoIP(self):
        response = requests.get('http://www.telize.com/geoip')
        return response.json()
