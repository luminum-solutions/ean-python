from django.conf import settings
import os
import urllib3
import hashlib
import time
import certifi
from resources.abstract_base import AbstractResource

try:
    import ssl
except ImportError:
    raise ImportError(
        "Your python is not compiled with SSL, please reinstall. Check https://stackoverflow.com/questions/5128845/importerror-no-module-named-ssl for more.")


class APIClient(object):
    """

    Expedia API client class.

    Request URL's are made up through the following settings that should be present either in the Django settings, or should be passed to __init__:

    Required settings:

    - `EAN_API_CID`: Your EAN API CID, available in your profile page.
    - `EAN_API_KEY`: Your EAN API key, also available in your profile page.
    - `EAN_SHARED_SECRET`: Your shared secret, this is also available in your EAN profile page.


    Optional settings:

    - `EAN_API_VERSION` (Default: 3): An integer representing the API version to use.
    - `EAN_API_DOMAIN`: (Default: `book.api.ean.com/ean-services/rs`): The EAN domain to do requests to.
    - `EAN_API_CURRENCY`: (Default: `EUR`): The currency to use in requests
    - `EAN_API_LOCALE`: (Default: `en_US`): The locale to use in requests
    """

    def __init__(self, protocol="https", domain="book.api.ean.com/ean-services/rs", api_version="3", api_key=None,
                 shared_secret=None, cid=None):

        if os.environ.get('DJANGO_SETTINGS_MODULE', None):  # If settings, get variables.
            # Optional local vars
            settings_version = getattr(settings, 'EAN_API_VERSION', None)
            settings_protocol = getattr(settings, 'EAN_API_PROTOCOL', None)  # Not documented on purpose.
            settings_domain = getattr(settings, 'EAN_API_DOMAIN', None)

            # Required instance variables
            self.cid = getattr(settings, 'EAN_API_CID', cid)
            self.api_key = getattr(settings, 'EAN_API_KEY', api_key)
            self.shared_secret = getattr(settings, 'EAN_SHARED_SECRET', shared_secret)

            # Optional instance variables
            self.locale = getattr(settings, 'EAN_API_LOCALE', 'en_US')
            self.currency = getattr(settings, 'EAN_API_CURRENCY', 'EUR')

            if self.cid is None:
                raise ValueError("No EAN_API_CID in settings, and no cid kwarg passed to APIClient()")

            if self.api_key is None:
                raise ValueError("No EAN_API_KEY in settings, and no api_key kwarg passed to APIClient()")

            if self.shared_secret is None:
                raise ValueError("No EAN_SHARED_SECRET in settings, and no shared_secret kwarg passed to APIClient()")
            urllib3.disable_warnings()

            self.http = urllib3.PoolManager(
                cert_reqs='CERT_NONE',  # Don't force certificate check.
                ca_certs=certifi.where(),  # Path to the Certifi bundle.
            )

            timestamp = str(int(time.time()))
            self.sig = hashlib.md5(self.api_key.encode('utf-8') + self.shared_secret.encode('utf-8') + timestamp.encode(
                'utf-8')).hexdigest()

            self.url = "%s://%s/__resource__/v%s" % (
                protocol or settings_protocol,
                domain or settings_domain,
                api_version or settings_version
            )

        else:
            self.url = "%s://%s/__resource__/v%s" % (protocol, domain, api_version)

    def construct_resource_url(self, resource, action=None, extra_vars={}):

        if not isinstance(resource, AbstractResource):
            raise RuntimeWarning(
                "Resource passed does not inherit from AbstractResource. Might not implement necessary methods..")

        # Construct the URL based on parameters. Use the base url defined in __init__
        request_url = "%s/%s?cid=%s&minorRev=%s&apiKey=%s&sig=%s&locale=%s&currencyCode=%s%s" % (
            self.url.replace('__resource__', str(resource)), action if action else "altProps", self.cid,
            self.minorRev if hasattr(self, "minorRev") else '99',
            self.api_key, self.sig, self.locale,
            self.currency, "" if not extra_vars else "&")

        # Add the extra variables to the URL
        for key, value in extra_vars.items() if (extra_vars is not None and len(extra_vars) > 2) else {}:
            request_url += "%s=%s&" % (key, value)

        # Strip last ampersand
        if not extra_vars == {} and extra_vars is not None:
            request_url = request_url[:-1]

        return request_url

    def request(self, request_url):
        xml = self.http.request('GET', request_url, headers={'Accept': 'application/json, */*'})
        if xml.getheader('Content-Type') == 'application/json':
            data = xml.data.decode('utf-8')
            xml.object = data
        return xml
