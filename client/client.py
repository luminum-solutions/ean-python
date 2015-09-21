from django.conf import settings
import os
import urllib3
import hashlib
import time
import certifi

try:
    import ssl
except ImportError:
    raise ImportError(
        "Your python is not compiled with SSL, please reinstall. Check https://stackoverflow.com/questions/5128845/importerror-no-module-named-ssl for more.")


class APIClient(object):
    def __init__(self, protocol="https", domain="book.api.ean.com/ean-services/rs", api_version="3", api_key=None,
                 shared_secret=None, cid=None):

        if os.environ.get('DJANGO_SETTINGS_MODULE', None):  # If settings, get variables.
            settings_version = getattr(settings, 'EAN_API_VERSION', None)
            settings_protocol = getattr(settings, 'EAN_API_URL', None)
            settings_domain = getattr(settings, 'EAN_API_DOMAIN', None)

            self.cid = getattr(settings, 'EAN_API_CID', cid)
            self.api_key = getattr(settings, 'EAN_API_KEY', api_key)
            self.shared_secret = getattr(settings, 'EAN_SHARED_SECRET', shared_secret)

            if self.cid is None:
                raise ValueError("No EAN_API_CID in settings, and no cid kwarg passed to APIClient()")

            if self.api_key is None:
                raise ValueError("No EAN_API_KEY in settings, and no api_key kwarg passed to APIClient()")

            if self.shared_secret is None:
                raise ValueError("No EAN_SHARED_SECRET in settings, and no shared_secret kwarg passed to APIClient()")
            urllib3.disable_warnings()
            self.http = urllib3.PoolManager(
                cert_reqs='CERT_NONE',  # Force certificate check.
                ca_certs=certifi.where(),  # Path to the Certifi bundle.
            )

            timestamp = str(int(time.time()))
            self.sig = hashlib.md5(self.api_key.encode('utf-8') + self.shared_secret.encode('utf-8') + timestamp.encode(
                'utf-8')).hexdigest()

            self.url = "%s://%s/__resource__/v%s" % (
                protocol if not settings_protocol else settings_protocol,
                domain if not settings_domain else settings_domain,
                api_version if not settings_version else settings_version
            )

        else:
            self.url = "%s://%s/__resource__/v%s" % (protocol, domain, api_version)

    def construct_xml(self, action):
        return "<HotelListRequest><city>Seattle<%2Fcity><stateProvinceCode>WA<%2FstateProvinceCode><countryCode>US<%2FcountryCode><arrivalDate>10%2F20%2F2015<%2FarrivalDate><departureDate>10%2F22%2F2015<%2FdepartureDate><RoomGroup><Room><numberOfAdults>2<%2FnumberOfAdults><%2FRoom><%2FRoomGroup><numberOfResults>25<%2FnumberOfResults><%2FHotelListRequest>"

    def construct_url(self, resource, action=None, locale='en_US', currency='EUR', extra_vars=None):

        xml = self.construct_xml(action)

        # Construct the URL based on parameters. Use the base url defined in __init__
        request_url = "%s/%s?cid=%s&minorRev=%s&apiKey=%s&locale=%s&currencyCode=%s%s%s" % (
            self.url.replace('__resource__', resource), action if action else "altProps", self.cid,
            self.minorRev if hasattr(self, "minorRev") else '99',
            self.api_key, locale,
            currency, "&xml=" + xml, "/" if not extra_vars else "&")

        # Add the extra variables to the URL
        for key, value in extra_vars if extra_vars is not None else []:
            request_url += "%s=%s&" % (key, value)

        # Strip last ampersand
        if not extra_vars:
            request_url = request_url[:-1]

        return request_url

    def request(self, request_url):
        xml = self.http.request('GET', request_url)
        print(xml)
